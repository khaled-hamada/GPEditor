# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baymaxGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import rospy
import actionlib
from move_base_msgs.msg import *
import time
import os
import signal
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import PoseStamped
from PyQt4 import QtCore, QtGui

location_position = dict()
location_position[0] = (-0.031, 0.038, 0.3)
location_position[1] = (0.599, 1.03, 1 )
location_position[2] = (4.415, 0.645, 3.14 )
location_position[3] = (7.409, 0.812, -3.14)
location_position[4] = (1.757, 4.377, -4)
location_position[5] = (1.757, 4.377, 4.5)


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



#########################################################################################################3

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(791, 648)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 140, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 190, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 230, 99, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 300, 99, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 140, 99, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 190, 99, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 240, 99, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(40, 160, 131, 151))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setMaximum(5)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 120, 161, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 300, 99, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 260, 99, 27))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))

        self.retranslateUi(Form)

        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.update_position)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.home)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stop_move)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cancel_goal)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.go_to_goal)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_robot)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.build_map)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.teleop)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.shutdown)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_map)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #variables related to functions global
        self.location_no = 0
        self.current_location_position = 0
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.goal = MoveBaseGoal()

#########################################################################################################3

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "run robot", None))
        self.pushButton_2.setText(_translate("Form", "build a map", None))
        self.pushButton_3.setText(_translate("Form", "move robot m.", None))
        self.pushButton_4.setText(_translate("Form", "shut down", None))
        self.pushButton_5.setText(_translate("Form", "go ", None))
        self.pushButton_6.setText(_translate("Form", "cancel", None))
        self.pushButton_7.setText(_translate("Form", "stop", None))
        self.label.setText(_translate("Form", "enter numbers from 1-5", None))
        self.pushButton_8.setText(_translate("Form", "Home", None))
        self.pushButton_9.setText(_translate("Form", "save map ", None))



#########################################################################################################3

    def update_position(self):
        self.location_no = self.spinBox.value()
    	self.current_location_position = location_position[self.location_no]
    	print self.current_location_position
        print 'got a new position to go to '


#########################################################################################################3
# we will edit this as when we call go_to_goal we will pass it three arguments x,y and theta
    def go_to_goal(self):
        print 'go_to_goal'
        self.goal.target_pose.pose.position.x=float(self.current_location_position[0])
        self.goal.target_pose.pose.position.y=float(self.current_location_position[1])
        self.goal.target_pose.pose.position.z=0.0
        #rotation
        q = quaternion_from_euler(0, 0, self.current_location_position[2], 'sxyz')
        self.goal.target_pose.pose.orientation.x = q[0]
        self.goal.target_pose.pose.orientation.y = q[1]
        self.goal.target_pose.pose.orientation.z = q[2]
        self.goal.target_pose.pose.orientation.w = q[3]

        self.goal.target_pose.header.frame_id= 'map'
        self.goal.target_pose.header.stamp = rospy.Time.now()
        #start listner
        rospy.loginfo("Waiting for server")
        #self.client.wait_for_server()


        rospy.loginfo("Sending Goals")
        self.client.send_goal(self.goal)

        rospy.loginfo("Waiting for result")
        #finish
        wait = self.client.wait_for_result()
        #if succed return 1 or true  else return 0 or false
        # If the result doesn't arrive, assume the Server is not available
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
        # Result of executing the action true or false
            return self.client.get_result()


######################################################################3
# both stop_move and cancel_goal do the same finction
    def stop_move(self):

        print 'stop robot movement '
        self.client.cancel_all_goals()


#########################################################################################################3

    def cancel_goal(self):
        print 'stop robot'
        self.client.cancel_all_goals()
################################################################

    def home(self):

        print 'go to home '
        self.current_location_position = location_position[0]
        self.go_to_goal()

##################################################################################3
# these five functions are the main functions required for operation

    def run_robot(self):
        print 'robot start running '
        #we will add & at the end of the line after debugging
        #os.system("gnome-terminal  -x   roslaunch  baymaxrobot  navigation.launch ")
        os.system("roslaunch  baymaxrobot  navigation.launch &")
        #os.kill(os.getppid(), signal.SIGHUP)

#########################################################################################################3

    def build_map(self):
        print 'build the map '
        #we will add & at the end of the line after debugging
        #os.system("gnome-terminal  -x   roslaunch  baymaxrobot  mapping.launch  ")
        os.system("roslaunch  baymaxrobot  mapping.launch & ")
        #os.kill(os.getppid(), signal.SIGHUP)

#########################################################################################################3


    def save_map(self):
        print 'saving the map '
        #we will add & at the end of the line after debugging
        os.system("rosrun map_server map_saver -f ~/baymax_ws2/src/baymaxrobot/maps/hospital & ")
        #os.kill(os.getppid(), signal.SIGHUP)
#########################################################################################################3


    #open telop only in a separete terminal
    def teleop(self):
        print 'moving the robot manually'
        os.system("gnome-terminal  -x rosrun teleop_twist_keyboard teleop_twist_keyboard.py ")
        #os.kill(os.getppid(), signal.SIGHUP)

#########################################################################################################3

    def shutdown(self):
        #search how to close all opend terminal using a python script
        print 'الروبوت غير متاح حاليا من فضلك روح وتعالا بكرة بدرى '
        os.kill(os.getppid(), signal.SIGHUP)
        #search how to close all opend terminal using a python script
		#print 'الروبوت غير متاح حاليا من فضلك روح وتعالا بكرة بدرى '

#########################################################################################################3







if __name__ == "__main__":
    import sys
    #open serial port first
    os.system("echo %CIC@S18 | sudo -S sudo chmod 666 /dev/ttyACM0")
    #start rosocre master fro nodes to start running
    os.system("roscore & ")
    rospy.init_node('robot_gui')
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
