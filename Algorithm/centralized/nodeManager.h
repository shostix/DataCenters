#ifndef NODEMANAGER_H
#define NODEMANAGER_H

#include "publicdefs.h"

class NodeManager
{
public:
    NodeManager(Nodes &);
private:
    Nodes nodes;
};

#endif // NODEMANAGER_H