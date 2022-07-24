# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1517, 799)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #eff9fe;\n"
"\n"
"}\n"
" #frame_11{\n"
"    background-color: #2596be;\n"
"}\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    color: #2596be;\n"
"}\n"
"#searchFrame{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"#appHeader{\n"
"    color: #2596be;\n"
"}\n"
"#card1, #card2, #card3, #card4 {\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#pushButton, #pushButton_2{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_4, #widget_5, #profileCont, #frame_15{\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#headerFrame{\n"
"    background-color: #fefeff;\n"
"}\n"
"#pushButton_3{\n"
"    background-color: #fefeff;\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"    border-top-left-radius: 20px ;\n"
"}\n"
"QPushButton{\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(-1, -1, 11, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setStyleSheet("#leftMenu {\n"
"background-color:#48C9B0;\n"
"}")
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.leftMenu)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_27 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_14.addWidget(self.label_27, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_9)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_9.addWidget(self.timeEdit)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btnHome = QtWidgets.QPushButton(self.frame_10)
        self.btnHome.setMinimumSize(QtCore.QSize(0, 0))
        self.btnHome.setSizeIncrement(QtCore.QSize(0, 0))
        self.btnHome.setStyleSheet("#btnHome{\n"
"    background-color: #F7F9F9;\n"
"    color: #283747;\n"
"    border-radius: 10px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon)
        self.btnHome.setObjectName("btnHome")
        self.verticalLayout_10.addWidget(self.btnHome)
        self.btnCreate = QtWidgets.QPushButton(self.frame_10)
        self.btnCreate.setStyleSheet("#btnCreate{\n"
"    background-color: #F7F9F9;\n"
"    color: #283747;\n"
"    border-radius: 10px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/rss.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCreate.setIcon(icon1)
        self.btnCreate.setObjectName("btnCreate")
        self.verticalLayout_10.addWidget(self.btnCreate)
        self.btnB = QtWidgets.QPushButton(self.frame_10)
        self.btnB.setStyleSheet("#btnB{\n"
"    background-color: #F7F9F9;\n"
"    color: #283747;\n"
"    border-radius: 10px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/package.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnB.setIcon(icon2)
        self.btnB.setObjectName("btnB")
        self.verticalLayout_10.addWidget(self.btnB)
        self.btnA = QtWidgets.QPushButton(self.frame_10)
        self.btnA.setStyleSheet("#btnA{\n"
"    background-color: #F7F9F9;\n"
"    color: #283747;\n"
"    border-radius: 10px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnA.setIcon(icon3)
        self.btnA.setObjectName("btnA")
        self.verticalLayout_10.addWidget(self.btnA)
        self.verticalLayout_9.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addWidget(self.frame_9)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.horizontalLayout.addWidget(self.leftMenu)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.widget)
        self.menuBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon4)
        self.menuBtn.setIconSize(QtCore.QSize(30, 30))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_3.addWidget(self.menuBtn)
        self.appHeader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.appHeader.setFont(font)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_3.addWidget(self.appHeader)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_2 = QtWidgets.QWidget(self.headerFrame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/search.svg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.searchFrame = QtWidgets.QFrame(self.widget_2)
        self.searchFrame.setMinimumSize(QtCore.QSize(400, 0))
        self.searchFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFrame.setObjectName("searchFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_4.addWidget(self.searchFrame)
        self.horizontalLayout_2.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.accountBtn = QtWidgets.QPushButton(self.widget_3)
        self.accountBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accountBtn.setIcon(icon5)
        self.accountBtn.setIconSize(QtCore.QSize(30, 30))
        self.accountBtn.setObjectName("accountBtn")
        self.horizontalLayout_6.addWidget(self.accountBtn, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.cardsFrame = QtWidgets.QWidget(self.mainBody)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cardsFrame.setFont(font)
        self.cardsFrame.setObjectName("cardsFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.card1 = QtWidgets.QFrame(self.cardsFrame)
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.card1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/message-square.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_4 = QtWidgets.QLabel(self.card1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_7.addWidget(self.card1)
        self.card4 = QtWidgets.QWidget(self.cardsFrame)
        self.card4.setObjectName("card4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.card4)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.label_11 = QtWidgets.QLabel(self.card4)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.horizontalLayout_7.addWidget(self.card4)
        self.card2 = QtWidgets.QFrame(self.cardsFrame)
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.card2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label_5 = QtWidgets.QLabel(self.card2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_7.addWidget(self.card2)
        self.card3 = QtWidgets.QFrame(self.cardsFrame)
        self.card3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.card3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.card3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.label_8 = QtWidgets.QLabel(self.card3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_7.addWidget(self.card3)
        self.verticalLayout.addWidget(self.cardsFrame)
        self.mainFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mainFrame.setFont(font)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_4 = QtWidgets.QWidget(self.mainFrame)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14, 0, QtCore.Qt.AlignLeft)
        self.btnReload = QtWidgets.QPushButton(self.frame_5)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/refresh-ccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReload.setIcon(icon6)
        self.btnReload.setIconSize(QtCore.QSize(40, 40))
        self.btnReload.setObjectName("btnReload")
        self.horizontalLayout_13.addWidget(self.btnReload, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setStyleSheet("#pushButton {\n"
"    background-color: #F7F9F9;\n"
"    color: #283747;\n"
"    border-radius: 10px;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_13.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.tableStudentInfo = QtWidgets.QTableWidget(self.frame_6)
        self.tableStudentInfo.setMinimumSize(QtCore.QSize(600, 400))
        self.tableStudentInfo.setMaximumSize(QtCore.QSize(600, 600))
        self.tableStudentInfo.setObjectName("tableStudentInfo")
        self.tableStudentInfo.setColumnCount(7)
        self.tableStudentInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStudentInfo.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableStudentInfo, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.horizontalLayout_9.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.mainFrame)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_12 = QtWidgets.QFrame(self.widget_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.frame_12)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_12)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/target.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_15.addWidget(self.pushButton_2)
        self.verticalLayout_13.addWidget(self.frame_12, 0, QtCore.Qt.AlignTop)
        self.frame_train = QtWidgets.QFrame(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_train.sizePolicy().hasHeightForWidth())
        self.frame_train.setSizePolicy(sizePolicy)
        self.frame_train.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_train.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_train.setObjectName("frame_train")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_train)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_11 = QtWidgets.QFrame(self.frame_train)
        self.frame_11.setStyleSheet("#frame_11{\n"
"    background-color: #FADBD8;\n"
"    border-radius: 20px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.comboBox = QtWidgets.QComboBox(self.frame_11)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 321, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_17 = QtWidgets.QLabel(self.frame_11)
        self.label_17.setGeometry(QtCore.QRect(20, 120, 55, 16))
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.frame_11)
        self.label_16.setGeometry(QtCore.QRect(20, 10, 55, 16))
        self.label_16.setObjectName("label_16")
        self.path = QtWidgets.QLineEdit(self.frame_11)
        self.path.setGeometry(QtCore.QRect(20, 150, 321, 31))
        self.path.setAutoFillBackground(False)
        self.path.setStyleSheet("#path {\n"
"color: black;\n"
"background-color: #FBFCFC\n"
"}")
        self.path.setObjectName("path")
        self.verticalLayout_14.addWidget(self.frame_11)
        self.frame_13 = QtWidgets.QFrame(self.frame_train)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.frame_13)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_15.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.frame_13)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.frame_13)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_15.addWidget(self.label_20)
        self.verticalLayout_14.addWidget(self.frame_13)
        self.verticalLayout_13.addWidget(self.frame_train)
        self.horizontalLayout_9.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout.addWidget(self.mainBody)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.profileCont = QtWidgets.QFrame(self.widget_6)
        self.profileCont.setMinimumSize(QtCore.QSize(100, 0))
        self.profileCont.setAutoFillBackground(False)
        self.profileCont.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profileCont.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profileCont.setObjectName("profileCont")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.profileCont)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_29 = QtWidgets.QLabel(self.profileCont)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_11.addWidget(self.label_29, 0, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.profileCont)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_11.addWidget(self.label_28, 0, QtCore.Qt.AlignHCenter)
        self.btnProfile = QtWidgets.QPushButton(self.profileCont)
        self.btnProfile.setIcon(icon5)
        self.btnProfile.setObjectName("btnProfile")
        self.verticalLayout_11.addWidget(self.btnProfile)
        self.btnLogout = QtWidgets.QPushButton(self.profileCont)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/greenIcons24/assets/green24/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon9)
        self.btnLogout.setObjectName("btnLogout")
        self.verticalLayout_11.addWidget(self.btnLogout)
        self.verticalLayout_12.addWidget(self.profileCont)
        self.horizontalLayout.addWidget(self.widget_6, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1517, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_27.setText(_translate("MainWindow", "Management Exam"))
        self.btnHome.setText(_translate("MainWindow", "Home"))
        self.btnCreate.setText(_translate("MainWindow", "Training Model"))
        self.btnB.setText(_translate("MainWindow", "Exam Room"))
        self.btnA.setText(_translate("MainWindow", "Group Info"))
        self.appHeader.setText(_translate("MainWindow", "Dashboard"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search information..."))
        self.label_3.setText(_translate("MainWindow", "Messages"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "List of Students"))
        self.btnReload.setText(_translate("MainWindow", "Reload"))
        self.pushButton.setText(_translate("MainWindow", "View Detail"))
        item = self.tableStudentInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableStudentInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tableStudentInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fullname"))
        item = self.tableStudentInfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tableStudentInfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableStudentInfo.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableStudentInfo.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Model"))
        self.label_15.setText(_translate("MainWindow", "Training Model"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Training"))
        self.label_17.setText(_translate("MainWindow", "Path file"))
        self.label_16.setText(_translate("MainWindow", "Model"))
        self.path.setPlaceholderText(_translate("MainWindow", "Enter path here..."))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_29.setText(_translate("MainWindow", "Group 3"))
        self.label_28.setText(_translate("MainWindow", "Thien Nguyen"))
        self.btnProfile.setText(_translate("MainWindow", "My Profile"))
        self.btnLogout.setText(_translate("MainWindow", "Log out"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
