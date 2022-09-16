#!/usr/bin/env python

from dynamixel_workbench_msgs.srv import  DynamixelCommand,DynamixelCommandRequest
import rospy
import sys
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from dynamixel_workbench_msgs.msg import DynamixelStateList
from std_msgs.msg import String
import math
from std_srvs.srv import Empty
from std_msgs.msg import Int32
from std_msgs.msg import Float64MultiArray
import numpy as np
import csv
desired_value1=0
desired_value2=0
control_value=0
total_val=0
u=0
pos=[]
pos_array=[]
vel_array=[]
rospy.wait_for_service('/dynamixel_workbench/dynamixel_command')
service = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command',DynamixelCommand)
kk=DynamixelCommandRequest()
kk.command=''
kk.id=0
i=1
old_desired_value=0
#rostopic echo /dynamixel_workbench/dynamixel_state/dynamixel_state[0]
def feed():	
	rospy.Subscriber('/dynamixel_workbench/dynamixel_state', DynamixelStateList,callback)
	rospy.Subscriber('/linear',Float64MultiArray,callback2)
def callback(message):
	b1 = message.dynamixel_state[0]
	pos.append(b1.present_position)
	ema(float(pos[0]))

def callback2(pos_message):
	global desired_value1,desired_value2
	desired_value1=pos_message.data[0]
	desired_value2=pos_message.data[1]
	print(desired_value1,desired_value2)

def ema(pos):
	global total_val
	total_val=desired_value1

	kk.addr_name='Goal_Position'

	total_val=np.clip(total_val, -20000, 20000)
	dyn_val=total_val+pos
	kk.value=dyn_val
	result=service(kk)
	#print(total_val,pos)

if __name__ == '__main__':
	while not rospy.is_shutdown():
	    try:  
		rospy.init_node('dynamixel_workbench_server1')
		feed ()
	        rospy.spin()
	    except rospy.ROSInterruptException:
		rospy.loginfo("node terminated.")
		pass
	
