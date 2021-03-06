#include "networkManager.h"

#include "common/element.h"
#include "common/network.h"
#include "common/node.h"
#include "common/store.h"
#include "common/link.h"
#include "common/assignment.h"
#include "routing/dijkstrarouter.h"

#include <iostream>

using std::cerr;
using std::endl;

NetworkManager::NetworkManager(Network & n)
:
    network(n),
    depthSearcher(0)
{

}

void NetworkManager::setSearchSpace(const Nodes & nodes)
{
    rejectedNodes.clear();
    rejectedStores.clear();

    Elements elements;
    for (Nodes::iterator i = nodes.begin(); i != nodes.end(); i++)
    {
        elements.insert(*i);
    }
    depthSearcher = new DepthSearcher(network, elements);
}

Nodes NetworkManager::getNodeCandidates()
{
    Nodes result;

    while ( !depthSearcher->isExhausted() )
    {
        Elements elements = depthSearcher->getElementCandidates();
        cerr << "[NM]\tDepth search returned " << elements.size() << endl;

        for ( Elements::iterator i = elements.begin(); i != elements.end(); i++ )
        {
            Element * element = *i;
            if ( ! element->isNode() )
                continue;

            Node * node = (Node *) element;
            if ( rejectedNodes.find(node) != rejectedNodes.end() )
                continue;

            result.insert(node);
        }

        depthSearcher->increaseSearchSpace();

        if ( !result.empty() )
            break;
    }

    rejectedNodes.insert(result.begin(), result.end());
    cerr << "[NM]\tPrepared " << result.size() << " candidates" << endl;
    return result;
}

Stores NetworkManager::getStoreCandidates()
{
    Stores result;

    while( !depthSearcher->isExhausted() )
    {
        Elements elements = depthSearcher->getElementCandidates();
        cerr << "[NM]\tDepth search returned " << elements.size() << endl;

        for ( Elements::iterator i = elements.begin(); i != elements.end(); i++ )
        {
            Element * element = *i;
            if ( ! element->isStore() )
                continue;

            Store * store = (Store *) element;
            
            if ( rejectedStores.find(store) != rejectedStores.end() )
                continue;
            
            result.insert(store);
        }

        depthSearcher->increaseSearchSpace();

        if ( !result.empty()  )
            break;
    }

    rejectedStores.insert(result.begin(), result.end());
    cerr << "[NM]\tPrepared " << result.size() << " candidates" << endl;
    return result;
}

Algorithm::Result NetworkManager::buildPath(Element * from, Element * to, Link * vlink, Assignment * assignment)
{
    if ( from == to )
        return Algorithm::SUCCESS;

    cerr << "[NM]\tBuilding path" << endl;
    Link * dummy = new Link("dummy", vlink->getCapacity(), vlink->getMaxCapacity());
    dummy->bindElements(from, to);

    DijkstraRouter router(dummy, &network);
    bool result = router.route();
    // NetPath path = VirtualLinkRouter::routeDejkstra(dummy, &network);
    delete dummy;

    if ( !result )
        return Algorithm::FAILURE;

    NetPath path = router.getPath();
    addAssignment(vlink, path);
    assignment->AddAssignment(vlink, path);
    cerr << "[NM]\tPath building succedeed" << endl;
    return Algorithm::SUCCESS;
}

void NetworkManager::cleanUpLinks(Links & links, Assignment * assignment)
{
    for ( Links::iterator l = links.begin(); l != links.end(); l++ )
    {
        NetPath path = assignment->GetAssignment(*l);
        if ( !path.empty() )
            removeAssignment(*l, path);

        assignment->RemoveAssignment(*l);
    }
}

void NetworkManager::removeAssignment(Link * vlink, NetPath & netPath)
{
    for ( NetPath::iterator i = netPath.begin(); i != netPath.end(); i++ )
        (*i)->RemoveAssignment(vlink);
}

void NetworkManager::addAssignment(Link * vlink, NetPath & netPath)
{
    for ( NetPath::iterator i = netPath.begin(); i != netPath.end(); i++ )
        (*i)->assign(*vlink);
}
