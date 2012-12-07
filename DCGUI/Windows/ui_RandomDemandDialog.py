
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RandomDemandDialog(object):
    def setupUi(self, RandomDemandDialog):
        RandomDemandDialog.setObjectName(_fromUtf8("RandomDemandDialog"))
        RandomDemandDialog.resize(377, 405)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RandomDemandDialog.sizePolicy().hasHeightForWidth())
        RandomDemandDialog.setSizePolicy(sizePolicy)
        RandomDemandDialog.setStyleSheet(_fromUtf8("QWidget, QMenuBar::item {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #c5d8ef, stop: 1 #89a5c3);\n"
"}\n"
"\n"
"QLabel, QSlider {\n"
"    background-color: transparent;\n"
"}"))
        RandomDemandDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(RandomDemandDialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.centralwidget = QtGui.QWidget(RandomDemandDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.n = QtGui.QLineEdit(self.centralwidget)
        self.n.setObjectName(_fromUtf8("n"))
        self.verticalLayout_2.addWidget(self.n)
        self.vms = QtGui.QLineEdit(self.centralwidget)
        self.vms.setObjectName(_fromUtf8("vms"))
        self.verticalLayout_2.addWidget(self.vms)
        self.t1 = QtGui.QLineEdit(self.centralwidget)
        self.t1.setObjectName(_fromUtf8("t1"))
        self.verticalLayout_2.addWidget(self.t1)
        self.t2 = QtGui.QLineEdit(self.centralwidget)
        self.t2.setObjectName(_fromUtf8("t2"))
        self.verticalLayout_2.addWidget(self.t2)
        self.storages = QtGui.QLineEdit(self.centralwidget)
        self.storages.setObjectName(_fromUtf8("storages"))
        self.verticalLayout_2.addWidget(self.storages)
        self.v1 = QtGui.QLineEdit(self.centralwidget)
        self.v1.setObjectName(_fromUtf8("v1"))
        self.verticalLayout_2.addWidget(self.v1)
        self.v2 = QtGui.QLineEdit(self.centralwidget)
        self.v2.setObjectName(_fromUtf8("v2"))
        self.verticalLayout_2.addWidget(self.v2)
        self.cc1 = QtGui.QLineEdit(self.centralwidget)
        self.cc1.setObjectName(_fromUtf8("cc1"))
        self.verticalLayout_2.addWidget(self.cc1)
        self.cc2 = QtGui.QLineEdit(self.centralwidget)
        self.cc2.setObjectName(_fromUtf8("cc2"))
        self.verticalLayout_2.addWidget(self.cc2)
        self.c1 = QtGui.QLineEdit(self.centralwidget)
        self.c1.setObjectName(_fromUtf8("c1"))
        self.verticalLayout_2.addWidget(self.c1)
        self.c2 = QtGui.QLineEdit(self.centralwidget)
        self.c2.setObjectName(_fromUtf8("c2"))
        self.verticalLayout_2.addWidget(self.c2)
        self.starttime = QtGui.QLineEdit(self.centralwidget)
        self.starttime.setObjectName(_fromUtf8("starttime"))
        self.verticalLayout_2.addWidget(self.starttime)
        self.endtime = QtGui.QLineEdit(self.centralwidget)
        self.endtime.setObjectName(_fromUtf8("endtime"))
        self.verticalLayout_2.addWidget(self.endtime)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.OK = QtGui.QPushButton(self.centralwidget)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.horizontalLayout.addWidget(self.OK)
        self.Cancel = QtGui.QPushButton(self.centralwidget)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))
        self.horizontalLayout.addWidget(self.Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.centralwidget)

        self.retranslateUi(RandomDemandDialog)
        QtCore.QObject.connect(self.OK, QtCore.SIGNAL(_fromUtf8("clicked()")), RandomDemandDialog.accept)
        QtCore.QObject.connect(self.Cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), RandomDemandDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RandomDemandDialog)

    def retranslateUi(self, RandomDemandDialog):
        RandomDemandDialog.setWindowTitle(QtGui.QApplication.translate("RandomDemandDialog", "Create Random Request", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RandomDemandDialog", "Number of requests", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("RandomDemandDialog", "Number of VMs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RandomDemandDialog", "Mimimal performance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RandomDemandDialog", "Maximal performance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("RandomDemandDialog", "Number of storages", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("RandomDemandDialog", "Minimal capacity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("RandomDemandDialog", "Maximal capacity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("RandomDemandDialog", "Minimal Consistency bandwidth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("RandomDemandDialog", "Maximal Consistency bandwidth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("RandomDemandDialog", "Mininal bandwidth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("RandomDemandDialog", "Maximal bandwidth", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("RandomDemandDialog", "Starting time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("RandomDemandDialog", "End time", None, QtGui.QApplication.UnicodeUTF8))
        self.n.setText(QtGui.QApplication.translate("RandomDemandDialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.vms.setText(QtGui.QApplication.translate("RandomDemandDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.t1.setText(QtGui.QApplication.translate("RandomDemandDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.t2.setText(QtGui.QApplication.translate("RandomDemandDialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.storages.setText(QtGui.QApplication.translate("RandomDemandDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.v1.setText(QtGui.QApplication.translate("RandomDemandDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.v2.setText(QtGui.QApplication.translate("RandomDemandDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.cc1.setText(QtGui.QApplication.translate("RandomDemandDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cc2.setText(QtGui.QApplication.translate("RandomDemandDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.c1.setText(QtGui.QApplication.translate("RandomDemandDialog", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.c2.setText(QtGui.QApplication.translate("RandomDemandDialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.starttime.setText(QtGui.QApplication.translate("RandomDemandDialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.endtime.setText(QtGui.QApplication.translate("RandomDemandDialog", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.OK.setText(QtGui.QApplication.translate("RandomDemandDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel.setText(QtGui.QApplication.translate("RandomDemandDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

