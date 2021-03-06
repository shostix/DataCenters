#ifndef VIRTUAL_LINK_ROUTER_H_
#define VIRTUAL_LINK_ROUTER_H_

#include "common/publicdefs.h"
#include <iostream>
#include <vector>

// struct containing an element and its weight in terms of dijkstra's algorithm
struct ElementWeight
{
public:
    Element * element;
    long weight;

    ElementWeight(Element * e, long w)
    : element(e)
    , weight(w)
    {
    }

    ElementWeight()
    : element(NULL)
    , weight(0)
    {
    }

    bool operator==(const ElementWeight& e2) const { return element == e2.element; }
};

struct WeightCompare
{
    bool operator() (const ElementWeight& e1, const ElementWeight& e2) const
    {
        if (e1.element == e2.element)
            return false;
        if (e1.weight == e2.weight)
            return e1.element < e2.element;
        return e1.weight < e2.weight;
    }
};

// Class VirtualLinkRouter, which provides the algorithms of routing the
// virtual link in the resource network.
// Two algorithms are used: dijkstra algorithm and k shortest path algorithm
// (which uses dijkstra as it's substep). The static method route may be used
// for routing the virtual link by one of these two variants.
//
class VirtualLinkRouter
{
public:
    // The algorithm used for finding route
    //
    enum SearchPathAlgorithm
    {
        NONE = 0,
        DEJKSTRA,
        K_SHORTEST_PATHS,
        K_SHORTEST_PATHS_ALL
    };

private:
    // Class with just static criterias represented,
    // with different implementations of criterias proposed.
    VirtualLinkRouter() {}
    virtual ~VirtualLinkRouter() {}

public:
    // Static function, which provides the algorithm of routing 
    // the virtual link in the network.
    // Returns the fact that the route is found.
    //
    static NetPath route(VirtualLink * virtualLink, Network * network, SearchPathAlgorithm algorithm, std::vector<NetPath> * pathStorage = NULL);

//private:
public:
    // The sub-algorithms used by the main routing method.

    // Dejkstra algorithm.
    // If there is no path, returns the empty NetPath var.
    static NetPath searchPathDejkstra(VirtualLink * virtualLink, Network * network, SearchPathAlgorithm algorithm);

    // Routing algorithm based on k shortest path search.
    // If there is no path, returns the empty NetPath var.
    static NetPath routeKShortestPaths(VirtualLink * virtualLink, Network * network);

    // Same as previous one, but storages all the paths found
    static NetPath routeKShortestPathsALL(VirtualLink * virtualLink, Network * network, std::vector<NetPath> * pathStorage);

    // Routing algorithm based on modified dejkstra algorithm.
    // If there is no path, returns the empty NetPath var.
    static NetPath routeDejkstra(VirtualLink * virtualLink, Network * network);

private:
    // Methods used in the sub-algorithms

    // The weight of the edge of the network used by the dejkstra algorithm.
    // Note: the order of the elements in the link may make sense: the weight
    // may be calculated according to the step of going from the first element
    // of the link to the second one.
    static long getEdgeWeigth(Link& link, Network * network, SearchPathAlgorithm algorithm);

    // The weight of the path.
    // Used in the alogorithm of k shortest paths.
    static long calculateKShortestPathWeight(NetPath& path);

    // Decreasing link's and switch's capacities by the value
    // of the virtualLink capacity, removing elements with the zero
    // or negative capacity (and save them to restore later)
    static void decreaseCapacities(VirtualLink * virtualLink, Network * network, Links * removedLinks, 
        Switches * removedSwitches);

    // Restore removed links and switches and their capacities.
    static void restoreCapacities(VirtualLink * virtualLink, Network * network, Links * removedLinks, 
        Switches * removedSwitches);
};

#endif
