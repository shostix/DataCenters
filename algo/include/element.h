#pragma once

#include "defs.h"

class Element {
public:
    enum Type {
        NONE            = 0x0,
        COMPUTER        = 0x1,
        STORE           = COMPUTER << 1,
        SWITCH          = STORE << 1,
        LINK            = SWITCH << 1,
        COMPUTATIONAL   = COMPUTER | STORE,
        NETWORK         = SWITCH | LINK,
        NODE            = COMPUTATIONAL | SWITCH
    };
protected:    
    Element() : type(NONE), assignee(0) {}

    virtual bool typeCheck(const Element * other) const = 0;
    virtual bool physicalCheck(const Element * other) const = 0;
    virtual bool attributeCheck(const Element * other) const = 0;

    virtual void decreaseResources(const Element * other) = 0;
    virtual void restoreResources(const Element * other) = 0;
public:
    virtual ~Element() {}

    void setAvailable(bool available = true) {
        this->available = available; 
    } 
    
    bool canHostAssignment(const Element * other ) const {
        if ( isVirtual() ) return false;
        if ( !other->isVirtual() ) return false;

        if ( !isAvailable() ) return false;
        
        if ( !typeCheck(other) ) return false;
        if ( !attributeCheck(other) ) return false;
        if ( !physicalCheck(other) ) return false;

        return true;
    }

    Element * getAssignee() const {
        return assignee;
    }

    const Elements & getAssignments() const {
        return assignments; 
    }

    virtual bool assign(Element * other) {
        if ( !canHostAssignment(other) )
          return false;

        decreaseResources(other);
        
        other->assignee = this;
        assignments.insert(other);
        return true;
    }

    virtual void removeAssignment(Element * other) {
        Elements::iterator a = assignments.find(other);
        if ( a == assignments.end() )
            return;

        restoreResources(other);

        other->assignee = 0;
        assignments.erase(a);
    }
public:
    inline bool isComputer() const { return type & COMPUTER; }
    inline bool isStore() const { return type & STORE;}
    inline bool isSwitch() const { return type & SWITCH; }
    inline bool isLink() const { return type & LINK; }
    inline bool isComputational() const { return type & COMPUTATIONAL; }
    inline bool isNetwork() const { return type & NETWORK; }
    inline bool isNode() const { return type & NODE; }
    inline bool isEdge() const { return isLink(); }
    inline bool isPhysical() const { return physical; }
    inline bool isVirtual() const { return !physical; }
    inline bool isAvailable() const { return isPhysical() && available; }
    inline bool isAssigned() const { return isVirtual() && assigned; }

    inline Computer * toComputer() const {
        if ( !isComputer() )
           return 0;
        return (Computer *)this; 
    }

    inline Store * toStore() const {
        if ( !isStore() )
            return 0;
        return (Store *)this;
    }

    inline Switch * toSwitch() const {
        if ( !isSwitch() )
            return 0;
        return (Switch *)this;
    }

    inline Link * toLink() const {
        if ( !isLink() )
            return 0;
        return (Link *)this;
    }
protected:
    Type type;
    bool physical;
    bool available;
    bool assigned;
    Element * assignee;
    Elements assignments;
};
