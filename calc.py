# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(321, 480)
        MainWindow.setMinimumSize(QtCore.QSize(321, 480))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: #171717;\n"
"border-radius: 10px;\n"
"\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(298, 28, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background-color:  #171717;\n"
"    color: #bfbfbf;\n"
"    font: 87 15pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color:  #171717;\n"
"    color: white;\n"
"    font: 87 20pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(298, 58, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_percent.sizePolicy().hasHeightForWidth())
        self.pushButton_percent.setSizePolicy(sizePolicy)
        self.pushButton_percent.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 0, 1, 1, 1)
        self.pushButton_CE = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_CE.sizePolicy().hasHeightForWidth())
        self.pushButton_CE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_CE.setFont(font)
        self.pushButton_CE.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_CE.setObjectName("pushButton_CE")
        self.gridLayout.addWidget(self.pushButton_CE, 0, 0, 1, 1)
        self.pushButton_division = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_division.sizePolicy().hasHeightForWidth())
        self.pushButton_division.setSizePolicy(sizePolicy)
        self.pushButton_division.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_division.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 22pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_division.setObjectName("pushButton_division")
        self.gridLayout.addWidget(self.pushButton_division, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_degree = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_degree.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_degree.sizePolicy().hasHeightForWidth())
        self.pushButton_degree.setSizePolicy(sizePolicy)
        self.pushButton_degree.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_degree.setObjectName("pushButton_degree")
        self.gridLayout.addWidget(self.pushButton_degree, 1, 0, 1, 1)
        self.pushButton_bracketopen = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bracketopen.sizePolicy().hasHeightForWidth())
        self.pushButton_bracketopen.setSizePolicy(sizePolicy)
        self.pushButton_bracketopen.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_bracketopen.setObjectName("pushButton_bracketopen")
        self.gridLayout.addWidget(self.pushButton_bracketopen, 1, 1, 1, 1)
        self.pushButton_root = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_root.sizePolicy().hasHeightForWidth())
        self.pushButton_root.setSizePolicy(sizePolicy)
        self.pushButton_root.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_root.setObjectName("pushButton_root")
        self.gridLayout.addWidget(self.pushButton_root, 0, 2, 1, 1)
        self.pushButton_erase = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_erase.sizePolicy().hasHeightForWidth())
        self.pushButton_erase.setSizePolicy(sizePolicy)
        self.pushButton_erase.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_erase.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/erase.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_erase.setIcon(icon)
        self.pushButton_erase.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_erase.setObjectName("pushButton_erase")
        self.gridLayout.addWidget(self.pushButton_erase, 0, 3, 1, 1)
        self.pushButton_bracketclose = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bracketclose.sizePolicy().hasHeightForWidth())
        self.pushButton_bracketclose.setSizePolicy(sizePolicy)
        self.pushButton_bracketclose.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 18pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_bracketclose.setObjectName("pushButton_bracketclose")
        self.gridLayout.addWidget(self.pushButton_bracketclose, 1, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_multiply.sizePolicy().hasHeightForWidth())
        self.pushButton_multiply.setSizePolicy(sizePolicy)
        self.pushButton_multiply.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton_multiply.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 22pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 2, 3, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy)
        self.pushButton_plus.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 22pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)
        self.pushButton_fact = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_fact.sizePolicy().hasHeightForWidth())
        self.pushButton_fact.setSizePolicy(sizePolicy)
        self.pushButton_fact.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_fact.setObjectName("pushButton_fact")
        self.gridLayout.addWidget(self.pushButton_fact, 5, 0, 1, 1)
        self.pushButton_point = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy)
        self.pushButton_point.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout.addWidget(self.pushButton_point, 5, 2, 1, 1)
        self.pushButton_equally = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_equally.sizePolicy().hasHeightForWidth())
        self.pushButton_equally.setSizePolicy(sizePolicy)
        self.pushButton_equally.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 22pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_equally.setObjectName("pushButton_equally")
        self.gridLayout.addWidget(self.pushButton_equally, 5, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        self.pushButton_minus.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color:#171717;\n"
"    font: 75 22pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_minus.setCheckable(False)
        self.pushButton_minus.setChecked(False)
        self.pushButton_minus.setAutoRepeat(False)
        self.pushButton_minus.setAutoExclusive(False)
        self.pushButton_minus.setAutoDefault(False)
        self.pushButton_minus.setDefault(False)
        self.pushButton_minus.setFlat(False)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setStyleSheet("QPushButton{\n"
"    width: 50px;\n"
"    height: 40px;\n"
"    color: white;\n"
"    background-color: black;\n"
"    font: 75 16pt \"Segoe UI\";\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  #292929;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #383838;\n"
"    width: 59px;\n"
"    height: 39px;\n"
"}\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????3000"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_CE.setText(_translate("MainWindow", "CE"))
        self.pushButton_division.setText(_translate("MainWindow", "??"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_degree.setText(_translate("MainWindow", "^"))
        self.pushButton_bracketopen.setText(_translate("MainWindow", "("))
        self.pushButton_root.setText(_translate("MainWindow", "???"))
        self.pushButton_bracketclose.setText(_translate("MainWindow", ")"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_multiply.setText(_translate("MainWindow", "??"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_fact.setText(_translate("MainWindow", "n!"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_equally.setText(_translate("MainWindow", "="))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_minus.setText(_translate("MainWindow", "???"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
