import xml.dom.minidom
from Core.AbstractGraph import AbstractGraph

class Storage:
    number = -1
    def __init__(self, id, volume, type):
        self.id = id
        self.volume = volume
        self.type = type

class Computer:
    number = -1
    def __init__(self, id, speed):
        self.id = id
        self.speed = speed

class Router:
    number = -1
    def __init__(self, id):
        self.id = id

class Link:
    def __init__(self, e1, e2, capacity):
        self.e1 = e1
        self.e2 = e2
        self.capacity = capacity

class ResourceGraph(AbstractGraph):
    def __init__(self):
        AbstractGraph.__init__(self)
        self.LoadFromXML("assets/resources.xml")

    def ExportToXml(self):
        dom = xml.dom.minidom.Document()
        root = dom.createElement("resources")
        dom.appendChild(root)
        for v in self.vertices:
            if isinstance(v, Computer):
                tag = dom.createElement("computer")
                tag.setAttribute("speed", str(v.speed))
            elif isinstance(v, Storage):
                tag = dom.createElement("storage")
                tag.setAttribute("volume", str(v.volume))
                tag.setAttribute("type", str(v.type))
            if isinstance(v, Router):
                tag = dom.createElement("router")
            tag.setAttribute("number", str(v.number))
            tag.setAttribute("name", str(v.id))
            root.appendChild(tag)
        for v in self.edges:
            tag = dom.createElement("link")
            tag.setAttribute("from", str(v.e1.number))
            tag.setAttribute("to", str(v.e2.number))
            tag.setAttribute("capacity", str(v.capacity))
            root.appendChild(tag)
        return dom.toprettyxml()

    def LoadFromXML(self, filename):
        ''' Load edges and vertices from XML
        
        .. warning:: Describe XML format here'''
        f = open(filename, "r")
        dom = xml.dom.minidom.parse(f)
        self.vertices = []
        self.edges = []
        for node in dom.childNodes:
            if node.tagName == "resources":
                #Parse vertices
                for vertex in node.childNodes:
                    if isinstance(vertex, xml.dom.minidom.Text):
                        continue
                    if vertex.nodeName == "link":
                        continue
                    name = vertex.getAttribute("name")
                    number = int(vertex.getAttribute("number"))
                    if vertex.nodeName == "computer":
                        speed = int(vertex.getAttribute("speed"))
                        v = Computer(name, speed)
                    elif vertex.nodeName == "storage":
                        volume = int(vertex.getAttribute("volume"))
                        type = int(vertex.getAttribute("type"))
                        v = Storage(name, volume, type)
                    elif vertex.nodeName == "router":
                        v = Router(name)
                    v.number = number
                    self.vertices.append(v)

                self.vertices.sort(key=lambda x: x.number)
                    
                #Parse edges
                for edge in node.childNodes:
                    if edge.nodeName == "link":
                        source = int(edge.getAttribute("from"))
                        destination = int(edge.getAttribute("to"))
                        cap = int(edge.getAttribute("capacity"))
                        e = Link(self.vertices[source-1], self.vertices[destination-1], cap)
                        self.edges.append(e)
        f.close()