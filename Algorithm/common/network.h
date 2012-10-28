#ifndef NETWORK_H
#define NETWORK_H

#include "publicdefs.h"

// Class representing a physical resources model of the data center
class Network
{
public:
   // constructor
   Network();
   // copy constructor
   Network(const Network & n);
   // destructor
   ~Network();

   // operator=
   Network& operator=(const Network & n);

   // Getters/Setters
   const Nodes& getNodes() const;
   const Stores& getStores() const;
   const Switches& getSwitches() const;
   const Links& getLinks() const;
   Nodes& getNodes();
   Stores& getStores();
   Switches& getSwitches();
   Links& getLinks();

   Node* addNode(Node * node);
   Store* addStore(Store * store);
   Switch* addSwitch(Switch* sw);
   Link* addLink(Link * link);
private:
   // members
   Nodes nodes;
   Stores stores;
   Switches switches;
   Links links;
};

#endif // NETWORK_H
