#pragma once

#include "edge.h"

class Link : public Edge {
    friend class XMLFactory;
    friend class Switch;
public:
    enum Attributes {
        NONE = 0
    };

private:
    Link() : Edge() {
        type = LINK;
    } 

    virtual bool typeCheck(const Element * other) const {
        return Element::isLink(other);
    }

    virtual bool attributeCheck(const Element * other) const {
        Link * link = other->toLink();
        return (attributes & link->attributes) == link->attributes;
    } 

    virtual bool physicalCheck(const Element * other) const {
        Link * link = other->toLink();
        if ( throughput < link->throughput ) return false;
        return true;
    }

    virtual void decreaseResources(const Element * other) {
        Link * link = other->toLink();
        throughput -= link->throughput;
    }

    virtual void restoreResources(const Element * other) {
        Link * link = other->toLink();
        throughput += link->throughput;
    }

private:
    Attributes attributes;
    long throughput;
};