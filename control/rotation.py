#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16MultiArray
from std_msgs.msg import Header
from std_msgs.msg import Float64MultiArray
import numpy as np
import time
desired_value=0
control_value=0
def feed():	
	rospy.Subscriber('/arduino_pub',Float64MultiArray,callback)

def callback(pos_message):

    	control=float(pos_message.data[3])
	angle1=float(pos_message.data[1])
	angle1=np.clip(angle1,-20.0,20.0)
	angle2=float(pos_message.data[2])
	angle2=np.clip(angle2,-20.0,20.0)
	rot_1=0.19454 *float(angle1)**2 + 125.33653*float(angle1)-4.33521
	rot_2=-0.11131 *float(angle2)**2 + 122.99948*float(angle2)-33.69701
	current=float(pos_message.data[0])

    	datab=Float64MultiArray()
    	topic='/step'
    	pub=rospy.Publisher(topic,Float64MultiArray,queue_size=10)
    	r=rospy.Rate(10)
    	datab.data=[current,rot_1,rot_2,control]
    	pub.publish(datab)
    	print(datab.data)



if __name__=='__main__':
	while not rospy.is_shutdown():
	    try:  
   		rospy.init_node('catheter_publisher')
		feed ()
	        rospy.spin()
	    except rospy.ROSInterruptException:
		rospy.loginfo("node terminated.")
		pass
	
