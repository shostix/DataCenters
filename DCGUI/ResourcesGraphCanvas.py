import math
from Core.Resources import Computer, Storage, Router, Link
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QPointF, QRect
from PyQt4.QtGui import QImage, QWidget, QPainter, QPainterPath, QColor, QCursor, QDialog, QIntValidator, QTableWidgetItem
from DCGUI.Windows.ui_ComputerDialog import Ui_ComputerDialog
from DCGUI.Windows.ui_RouterDialog import Ui_RouterDialog
from DCGUI.Windows.ui_EdgeDialog import Ui_EdgeDialog
from DCGUI.Windows.ui_StorageDialog import Ui_StorageDialog

class ComputerDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_ComputerDialog()
        self.ui.setupUi(self)
        self.valid = QIntValidator(0, 1000000, self)
        self.ui.speed.setValidator(self.valid)
        self.ui.ram.setValidator(self.valid)
        
    def Load(self, v):
        self.ui.id.setText(v.id)
        self.ui.speed.setText(str(v.speed))
        self.ui.ram.setText(str(v.ram))
        
    def SetResult(self, v):
        v.id = self.ui.id.text()
        v.speed = int(self.ui.speed.text())
        v.ram = int(self.ui.ram.text())

class StorageDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_StorageDialog()
        self.ui.setupUi(self)
        self.valid = QIntValidator(0, 1000000, self)
        self.ui.volume.setValidator(self.valid)
        
    def Load(self, v):
        self.ui.id.setText(v.id)
        self.ui.volume.setText(str(v.volume))
        self.ui.type.setText(str(v.type))
        
    def SetResult(self, v):
        v.id = self.ui.id.text()
        v.volume = int(self.ui.volume.text())
        v.type = self.ui.type.text()

class RouterDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_RouterDialog()
        self.ui.setupUi(self)
        
    def Load(self, v):
        self.ui.id.setText(v.id)
        self.ui.capacity.setText(str(v.capacity))
        
    def SetResult(self, v):
        v.id = self.ui.id.text()
        v.capacity = int(self.ui.capacity.text())
        

class EdgeDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_EdgeDialog()
        self.ui.setupUi(self)
        self.valid = QIntValidator(0, 1000000, self)
        self.ui.capacity.setValidator(self.valid)

    def Load(self, e):
        self.ui.capacity.setText(str(e.capacity))

    def SetResult(self, e):
        e.capacity = int(self.ui.capacity.text())

class State:
    ''' Enum representing current editing mode '''
    Select = 0
    Computer = 1
    Storage = 2
    Router = 3
    Edge = 4

class ResourcesGraphCanvas(QWidget):
    resources = None
    vertices = {}
    edges = {}
    selectedVertex = None
    pressed = False
    edgeDraw = False
    curEdge = None
    selectedEdge = None
    state = State.Select
    size = 25.0

    colors = {
              "line": QColor(10, 34, 200),
              "selected": QColor(1, 200, 1),
              }

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.computericon = QImage(":/pics/pics/computer.png")
        self.storageicon = QImage(":/pics/pics/storage.png")
        self.routericon = QImage(":/pics/pics/router.png")
        self.computerselectedicon = QImage(":/pics/pics/computer_selected.png")
        self.storageselectedicon = QImage(":/pics/pics/storage_selected.png")
        self.routerselectedicon = QImage(":/pics/pics/router_selected.png")
        
    def paintEvent(self, event):
        if not self.resources:
            return
        paint = QPainter(self)
        for e in self.resources.edges:
                if e == self.selectedEdge:
                    paint.setPen(self.colors["selected"])
                else:
                    paint.setPen(self.colors["line"])
                self.drawArrow(paint, self.vertices[e.e1].x() + self.size / 2, self.vertices[e.e1].y() + self.size / 2,
                             self.vertices[e.e2].x() + self.size / 2, self.vertices[e.e2].y() + self.size / 2)
        for v in self.vertices.keys():
            if isinstance(v, Computer):
                if self.selectedVertex != self.vertices[v]:
                    paint.drawImage(self.vertices[v], self.computericon)
                else:
                    paint.drawImage(self.vertices[v], self.computerselectedicon)
            elif isinstance(v, Storage):
                if self.selectedVertex != self.vertices[v]:
                    paint.drawImage(self.vertices[v], self.storageicon)
                else:
                    paint.drawImage(self.vertices[v], self.storageselectedicon)
            elif isinstance(v, Router):
                if self.selectedVertex != self.vertices[v]:
                    paint.drawImage(self.vertices[v], self.routericon)
                else:
                    paint.drawImage(self.vertices[v], self.routerselectedicon)
        paint.setPen(self.colors["line"])
        if self.edgeDraw:
            self.drawArrow(paint, self.curEdge[0].x() + self.size / 2, self.curEdge[0].y() + self.size / 2,
                           QCursor.pos().x() - self.mapToGlobal(self.geometry().topLeft()).x(),
                           QCursor.pos().y() - self.mapToGlobal(self.geometry().topLeft()).y())
        paint.end()

    def Visualize(self, r):
        self.resources = r
        for v in self.resources.vertices:
            rect = QtCore.QRect(v.x - self.size / 2, v.y - self.size / 2, self.size, self.size)
            self.vertices[v] = rect
        self.ResizeCanvas()
        self.repaint()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Delete:
            if self.selectedVertex != None:
                v = next(v for v in self.vertices.keys() if self.vertices[v] == self.selectedVertex)
                del self.vertices[v]
                self.resources.DeleteVertex(v)
                del self.selectedVertex
                self.selectedVertex = None
                self.changed = True
                self.repaint()
            elif self.selectedEdge != None:
                self.resources.DeleteEdge(self.selectedEdge)
                self.selectedEdge = None
                self.changed = True
                self.repaint()
        elif e.key() == QtCore.Qt.Key_Return:
            if self.selectedVertex != None:
                v = next(v for v in self.vertices.keys() if self.vertices[v] == self.selectedVertex)
                self.EditVertex(v)
                self.repaint()
            elif self.selectedEdge != None:
                self.EditEdge(self.selectedEdge)
                self.repaint()

    def ResizeCanvas(self):
        maxx = 0
        maxy = 0
        for r in self.vertices.values():
            if r.topRight().x() > maxx:
                maxx = r.topRight().x()
            if r.bottomRight().y() > maxy:
                maxy = r.bottomRight().y()
        self.setGeometry(0, 0, max(maxx + 10, self.parent().width()), max(maxy + 10, self.parent().height()))

    def drawArrow(self, paint, x1, y1, x2, y2):
        m = paint.worldMatrix()
        paint.translate(x1,y1)
        pi = 3.1415926
        if abs(x2 - x1) > 0:
            alpha = math.atan(abs(y2-y1)/abs(x2-x1)) * 180 / pi
        else:
            alpha = 90
        if y2 > y1:
            if x2 > x1:
                paint.rotate(alpha)
            else:
                paint.rotate(180-alpha)
        else:
            if x2 > x1:
                paint.rotate(-alpha)
            else:
                paint.rotate(alpha-180)
        endcoord = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        p1 = QPointF(endcoord , 0)
        paint.drawLine(0, 0, p1.x(), 0)
        paint.setWorldMatrix(m)

    def mousePressEvent(self, e):
        if self.state == State.Select:
            for v in self.vertices.keys():
                if self.vertices[v].contains(e.pos()):
                    self.selectedVertex = self.vertices[v]
                    self.selectedEdge = None
                    self.repaint()
                    self.pressed = True
                    return
            for ed in self.resources.edges:
                a = self.vertices[ed.e1].center()
                b = self.vertices[ed.e2].center()
                c = e.pos()
                ab = math.sqrt((a.x() - b.x())**2 + (a.y() - b.y())**2)
                inner = QtCore.QRect(a, b)
                if inner.contains(c):
                    bc = math.sqrt((c.x() - b.x())**2 + (c.y() - b.y())**2)
                    ac = math.sqrt((a.x() - c.x())**2 + (a.y() - c.y())**2)
                    p = (ab + bc + ac) / 2.0
                    area = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
                    if area < ab:
                        self.selectedEdge = ed
                        self.selectedVertex = None
                        self.repaint()
                        return
            self.selectedEdge = None
            self.selectedVertex = None
            self.repaint()
            return
        elif self.state == State.Computer:
            rect = QtCore.QRect(e.x() - self.size / 2, e.y() - self.size / 2, self.size, self.size)
            computer = Computer("id", 0, 0)
            self.vertices[computer] = rect
            self.resources.AddVertex(computer)
            self.changed = True
            self.ResizeCanvas()
            self.repaint()
        elif self.state == State.Storage:
            rect = QtCore.QRect(e.x() - self.size / 2, e.y() - self.size / 2, self.size, self.size)
            storage = Storage("id", 0, 0)
            self.vertices[storage] = rect
            self.resources.AddVertex(storage)
            self.changed = True
            self.ResizeCanvas()
            self.repaint()
        elif self.state == State.Router:
            rect = QtCore.QRect(e.x() - self.size / 2, e.y() - self.size / 2, self.size, self.size)
            router = Router("id", 0)
            self.vertices[router] = rect
            self.resources.AddVertex(router)
            self.changed = True
            self.ResizeCanvas()
            self.repaint()
        elif self.state == State.Edge:
            for v in self.vertices.keys():
                if self.vertices[v].contains(e.pos()):
                    self.edgeDraw = True
                    self.curEdge = []
                    self.curEdge.append(self.vertices[v])
                    self.curEdge.append(v)
                    self.repaint()

    def mouseMoveEvent(self, e):
        if (self.state == State.Computer) or (self.state == State.Storage) or (self.state == State.Router):
            return
        elif self.state == State.Select:
            if self.pressed:
                self.selectedVertex.moveTo(e.pos().x() - self.size / 2, e.pos().y() - self.size / 2)
                self.ResizeCanvas()
                self.repaint()
        elif self.state == State.Edge:
            if self.edgeDraw:
                self.repaint()

    def mouseReleaseEvent(self, e):
        self.pressed = False
        if self.edgeDraw:
            for v in self.vertices.keys():
                if self.vertices[v].contains(e.pos()):
                    ne = Link(self.curEdge[1], v, 0)
                    self.resources.AddLink(ne)
            self.edgeDraw = False
            self.curEdge = None 
            self.changed = True    
            self.repaint()

    def mouseDoubleClickEvent(self, e):
        if self.selectedVertex != None:
            v = next(v for v in self.vertices.keys() if self.vertices[v] == self.selectedVertex)
            self.EditVertex(v)
            self.repaint()
        elif self.selectedEdge != None:
            self.EditEdge(self.selectedEdge)
            self.repaint()

    def EditEdge(self, e):
        d = EdgeDialog()
        d.Load(e)
        d.exec_()
        if d.result() == QDialog.Accepted:
            d.SetResult(e)
            self.changed = True

    def EditVertex(self, v):
        if isinstance(v, Computer):
            d = ComputerDialog()
            d.Load(v)
            d.exec_()
            if d.result() == QDialog.Accepted:
                d.SetResult(v)
        if isinstance(v, Storage):
            d = StorageDialog()
            d.Load(v)
            d.exec_()
            if d.result() == QDialog.Accepted:
                d.SetResult(v)
        if isinstance(v, Router):
            d = RouterDialog()
            d.Load(v)
            d.exec_()
            if d.result() == QDialog.Accepted:
                d.SetResult(v)
        self.changed = True

    def Clear(self):
        self.vertices = {}
        self.edges = {}
        self.selectedVertex = None
        self.pressed = False
        self.edgeDraw = False
        self.curEdge = None
        self.selectedEdge = None

    def updatePos(self):
        for v in self.vertices.keys():
            rect = self.vertices[v]
            v.x = rect.x() + self.size/2
            v.y = rect.y() + self.size/2