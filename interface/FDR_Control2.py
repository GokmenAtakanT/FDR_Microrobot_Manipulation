# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FDR_Control2.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import rospy, time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from dynamixel_workbench_msgs.msg import DynamixelStateList
from sensor_msgs.msg import JointState
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty
from dynamixel_workbench_msgs.srv import  DynamixelCommand,DynamixelCommandRequest
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Header
import pickle 
import cv2
import numpy as np
control_val=0
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1186, 883)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Desktop/Despacho_U_M_V0.1/Imagens/dump-truck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget_12 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_12.setGeometry(QtCore.QRect(170, 90, 341, 301))
        self.formLayoutWidget_12.setObjectName(_fromUtf8("formLayoutWidget_12"))
        self.formLayout_23 = QtGui.QFormLayout(self.formLayoutWidget_12)
        self.formLayout_23.setMargin(0)
        self.formLayout_23.setObjectName(_fromUtf8("formLayout_23"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_23.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_23.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_23.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(8)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_23.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.formLayoutWidget_13 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_13.setGeometry(QtCore.QRect(170, 410, 339, 161))
        self.formLayoutWidget_13.setObjectName(_fromUtf8("formLayoutWidget_13"))
        self.formLayout_24 = QtGui.QFormLayout(self.formLayoutWidget_13)
        self.formLayout_24.setMargin(0)
        self.formLayout_24.setObjectName(_fromUtf8("formLayout_24"))
        self.label_6 = QtGui.QLabel(self.formLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(8)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_24.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_24.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_24.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem4)
        self.formLayoutWidget_14 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_14.setGeometry(QtCore.QRect(170, 590, 339, 161))
        self.formLayoutWidget_14.setObjectName(_fromUtf8("formLayoutWidget_14"))
        self.formLayout_25 = QtGui.QFormLayout(self.formLayoutWidget_14)
        self.formLayout_25.setMargin(0)
        self.formLayout_25.setObjectName(_fromUtf8("formLayout_25"))
        self.label_25 = QtGui.QLabel(self.formLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.label_25.setFont(font)
        self.label_25.setLineWidth(8)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_25.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_25)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_25.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_25.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem6)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 511, 61))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(15)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(170, 570, 921, 20))
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(170, 390, 921, 20))
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.Stop = QtGui.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(510, 590, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Stop.setFont(font)
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.Initial = QtGui.QPushButton(self.centralwidget)
        self.Initial.setGeometry(QtCore.QRect(510, 680, 581, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Initial.setFont(font)
        self.Initial.setObjectName(_fromUtf8("Initial"))
        self.Current = QtGui.QPushButton(self.centralwidget)
        self.Current.setGeometry(QtCore.QRect(510, 504, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Current.setFont(font)
        self.Current.setObjectName(_fromUtf8("Current"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(520, 340, 148, 28))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_14.setLineWidth(11)
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(510, 260, 581, 20))
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 290, 91, 59))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.Angle1 = QtGui.QLineEdit(self.centralwidget)
        self.Angle1.setGeometry(QtCore.QRect(630, 300, 131, 51))
        self.Angle1.setObjectName(_fromUtf8("Angle1"))
        self.Angle2 = QtGui.QLineEdit(self.centralwidget)
        self.Angle2.setGeometry(QtCore.QRect(880, 300, 151, 51))
        self.Angle2.setObjectName(_fromUtf8("Angle2"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(780, 290, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(170, 70, 921, 20))
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(170, 760, 921, 20))
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(510, 670, 581, 20))
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(780, 100, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.Lin2 = QtGui.QLineEdit(self.centralwidget)
        self.Lin2.setGeometry(QtCore.QRect(890, 100, 151, 51))
        self.Lin2.setObjectName(_fromUtf8("Lin2"))
        self.Lin1 = QtGui.QLineEdit(self.centralwidget)
        self.Lin1.setGeometry(QtCore.QRect(630, 100, 131, 51))
        self.Lin1.setObjectName(_fromUtf8("Lin1"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 100, 101, 59))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Linear = QtGui.QPushButton(self.centralwidget)
        self.Linear.setGeometry(QtCore.QRect(510, 170, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Linear.setFont(font)
        self.Linear.setObjectName(_fromUtf8("Linear"))
        self.Current_2 = QtGui.QLineEdit(self.centralwidget)
        self.Current_2.setGeometry(QtCore.QRect(720, 430, 131, 51))
        self.Current_2.setObjectName(_fromUtf8("Current_2"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(540, 420, 101, 59))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.Control_2 = QtGui.QLineEdit(self.centralwidget)
        self.Control_2.setGeometry(QtCore.QRect(790, 10, 131, 51))
        self.Control_2.setObjectName(_fromUtf8("Control_2"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(630, 10, 141, 59))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

	self.Linear.clicked.connect(self.Linear_Motion)
	#self.Rotate.clicked.connect(self.Rotate_Motion)
	self.Current.clicked.connect(self.Current_Coil)
	self.Stop.clicked.connect(self.Stop_Motion)
	self.Initial.clicked.connect(self.Initial_Motion)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ROS + PyQT GUI Example", None))
        self.label_2.setText(_translate("MainWindow", "Manipulation", None))
        self.label_6.setText(_translate("MainWindow", "Operation Mode", None))
        self.label_25.setText(_translate("MainWindow", "Debugging Mode", None))
        self.label_4.setText(_translate("MainWindow", "FDR MANIPULATION", None))
        self.Stop.setText(_translate("MainWindow", "System Stop", None))
        self.Initial.setText(_translate("MainWindow", "Send System To Initial", None))
        self.Current.setText(_translate("MainWindow", "Activate Current", None))
        self.label_7.setText(_translate("MainWindow", "Angle 1", None))
        self.Angle1.setText(_translate("MainWindow", "0", None))
        self.Angle2.setText(_translate("MainWindow", "0", None))
        self.label_9.setText(_translate("MainWindow", "Angle 2", None))
        self.label_10.setText(_translate("MainWindow", "Linear 2", None))
        self.Lin2.setText(_translate("MainWindow", "0", None))
        self.Lin1.setText(_translate("MainWindow", "0", None))
        self.label_8.setText(_translate("MainWindow", "Linear 1", None))
        self.Linear.setText(_translate("MainWindow", "Activate Linear Mechanism", None))
        self.Current_2.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Current", None))
        self.Control_2.setText(_translate("MainWindow", "0", None))
        self.label_12.setText(_translate("MainWindow", "Controller", None))

    def Initial_Motion(self):
	#global des_pos,last_pos,valx,valy,des_pos_old,in_x,in_y

        datab=Float64MultiArray()
	pub = rospy.Publisher('Initial', Float64MultiArray, queue_size=10)
	rate = rospy.Rate(10) # 10hz
        datab.data=[0,0]
	rospy.loginfo(datab)
	pub.publish(datab)
	rate.sleep()

    def Current_Coil(self):
	#global des_pos,last_pos,valx,valy,des_pos_old,in_x,in_y

	datab=Float64MultiArray()
	pub = rospy.Publisher('arduino_pub', Float64MultiArray, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	val4=float(self.Control_2.text())
	val2=float(self.Angle1.text())
	val3=float(self.Angle2.text())
	val1=float(self.Current_2.text())
	datab.data=[val1,val2,val3,val4]
	rospy.loginfo(datab)
	pub.publish(datab)
	rate.sleep()



    def Stop_Motion(self):
	#global des_pos,last_pos,valx,valy,des_pos_old,in_x,in_y

	datab=Float64MultiArray()
	pub = rospy.Publisher('current', Float64MultiArray, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	datab.data=[0,0]
	rospy.loginfo(datab)
	pub.publish(datab)
	rate.sleep()

    def Linear_Motion(self):
	#global des_pos,last_pos,valx,valy,des_pos_old,in_x,in_y
	datab=Float64MultiArray()
	pub = rospy.Publisher('linear', Float64MultiArray, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	val1=float(self.Lin1.text())
	val2=float(self.Lin2.text())
	datab.data=[(val1),(val2)]
	rospy.loginfo(datab)
	pub.publish(datab)
	rate.sleep()

if __name__ == "__main__":
    import sys
    rospy.init_node('FDR', anonymous=True)
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

