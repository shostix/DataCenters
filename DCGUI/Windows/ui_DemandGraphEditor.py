
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DemandGraphEditor(object):
    def setupUi(self, DemandGraphEditor):
        DemandGraphEditor.setObjectName(_fromUtf8("DemandGraphEditor"))
        DemandGraphEditor.setWindowModality(QtCore.Qt.ApplicationModal)
        DemandGraphEditor.resize(443, 338)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/graph.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DemandGraphEditor.setWindowIcon(icon)
        DemandGraphEditor.setStyleSheet(_fromUtf8("QWidget, QMenuBar::item {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #c5d8ef, stop: 1 #89a5c3);\n"
"}\n"
"\n"
"QLabel, QSlider {\n"
"    background-color: transparent;\n"
"}"))
        self.centralwidget = QtGui.QWidget(DemandGraphEditor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.startTime = QtGui.QLineEdit(self.centralwidget)
        self.startTime.setObjectName(_fromUtf8("startTime"))
        self.gridLayout.addWidget(self.startTime, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.endTime = QtGui.QLineEdit(self.centralwidget)
        self.endTime.setObjectName(_fromUtf8("endTime"))
        self.gridLayout.addWidget(self.endTime, 0, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphArea = QtGui.QScrollArea(self.centralwidget)
        self.graphArea.setWidgetResizable(False)
        self.graphArea.setObjectName(_fromUtf8("graphArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 230))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.graphArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.graphArea)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        DemandGraphEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DemandGraphEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        DemandGraphEditor.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(DemandGraphEditor)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        DemandGraphEditor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelect = QtGui.QAction(DemandGraphEditor)
        self.actionSelect.setCheckable(True)
        self.actionSelect.setChecked(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect.setIcon(icon1)
        self.actionSelect.setObjectName(_fromUtf8("actionSelect"))
        self.actionVM = QtGui.QAction(DemandGraphEditor)
        self.actionVM.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/computer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVM.setIcon(icon2)
        self.actionVM.setObjectName(_fromUtf8("actionVM"))
        self.actionEdge = QtGui.QAction(DemandGraphEditor)
        self.actionEdge.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/edge.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdge.setIcon(icon3)
        self.actionEdge.setObjectName(_fromUtf8("actionEdge"))
        self.actionNew_System = QtGui.QAction(DemandGraphEditor)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/page.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_System.setIcon(icon4)
        self.actionNew_System.setObjectName(_fromUtf8("actionNew_System"))
        self.actionOpen_System = QtGui.QAction(DemandGraphEditor)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_System.setIcon(icon5)
        self.actionOpen_System.setObjectName(_fromUtf8("actionOpen_System"))
        self.actionSave_System = QtGui.QAction(DemandGraphEditor)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/cd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_System.setIcon(icon6)
        self.actionSave_System.setObjectName(_fromUtf8("actionSave_System"))
        self.actionSave_System_As = QtGui.QAction(DemandGraphEditor)
        self.actionSave_System_As.setObjectName(_fromUtf8("actionSave_System_As"))
        self.actionExit = QtGui.QAction(DemandGraphEditor)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDemandStorage = QtGui.QAction(DemandGraphEditor)
        self.actionDemandStorage.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/storage.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDemandStorage.setIcon(icon7)
        self.actionDemandStorage.setObjectName(_fromUtf8("actionDemandStorage"))
        self.menuFile.addAction(self.actionNew_System)
        self.menuFile.addAction(self.actionOpen_System)
        self.menuFile.addAction(self.actionSave_System)
        self.menuFile.addAction(self.actionSave_System_As)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionNew_System)
        self.toolBar.addAction(self.actionOpen_System)
        self.toolBar.addAction(self.actionSave_System)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelect)
        self.toolBar.addAction(self.actionVM)
        self.toolBar.addAction(self.actionDemandStorage)
        self.toolBar.addAction(self.actionEdge)

        self.retranslateUi(DemandGraphEditor)
        QtCore.QObject.connect(self.actionSelect, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.toggleSelect)
        QtCore.QObject.connect(self.actionVM, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.toggleVM)
        QtCore.QObject.connect(self.actionEdge, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.toggleEdge)
        QtCore.QObject.connect(self.actionNew_System, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.New)
        QtCore.QObject.connect(self.actionOpen_System, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.Open)
        QtCore.QObject.connect(self.actionSave_System, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.Save)
        QtCore.QObject.connect(self.actionSave_System_As, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.SaveAs)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.close)
        QtCore.QObject.connect(self.actionDemandStorage, QtCore.SIGNAL(_fromUtf8("triggered()")), DemandGraphEditor.toggleDemandStorage)
        QtCore.QObject.connect(self.startTime, QtCore.SIGNAL(_fromUtf8("editingFinished()")), DemandGraphEditor.changeTime)
        QtCore.QObject.connect(self.endTime, QtCore.SIGNAL(_fromUtf8("editingFinished()")), DemandGraphEditor.changeTime)
        QtCore.QMetaObject.connectSlotsByName(DemandGraphEditor)
        DemandGraphEditor.setTabOrder(self.graphArea, self.startTime)
        DemandGraphEditor.setTabOrder(self.startTime, self.endTime)

    def retranslateUi(self, DemandGraphEditor):
        DemandGraphEditor.setWindowTitle(QtGui.QApplication.translate("DemandGraphEditor", "Request Graph Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DemandGraphEditor", "Starting Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DemandGraphEditor", "End Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("DemandGraphEditor", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("DemandGraphEditor", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect.setText(QtGui.QApplication.translate("DemandGraphEditor", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Alt+1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVM.setText(QtGui.QApplication.translate("DemandGraphEditor", "Add VM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVM.setToolTip(QtGui.QApplication.translate("DemandGraphEditor", "Add VM", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVM.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Alt+2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdge.setText(QtGui.QApplication.translate("DemandGraphEditor", "Add Virtual Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdge.setToolTip(QtGui.QApplication.translate("DemandGraphEditor", "Add Virtual Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdge.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Alt+3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_System.setText(QtGui.QApplication.translate("DemandGraphEditor", "New Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_System.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_System.setText(QtGui.QApplication.translate("DemandGraphEditor", "Open Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_System.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_System.setText(QtGui.QApplication.translate("DemandGraphEditor", "Save Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_System.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_System_As.setText(QtGui.QApplication.translate("DemandGraphEditor", "Save Graph As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_System_As.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("DemandGraphEditor", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDemandStorage.setText(QtGui.QApplication.translate("DemandGraphEditor", "Add Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDemandStorage.setToolTip(QtGui.QApplication.translate("DemandGraphEditor", "Add Storage", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDemandStorage.setShortcut(QtGui.QApplication.translate("DemandGraphEditor", "Alt+4", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
