#!/usr/bin/env python3

import rospy
import math 
#import numpy as np
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
if __name__ == '__main__':
	rospy.init_node("draw_circle")
	rospy.loginfo("Started")
    
	pub1 = rospy.Publisher("/turtle1/pose", Pose, queue_size=10)

	pub2 = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

	rate = rospy.Rate(5)

	while not rospy.is_shutdown():
		msg = Twist()
		msg1= Pose()
		#msg.angular.z=2
		#msg1.theta=3.14/18
		#for t in range(0, 18):
		# msg1.linear_velocity = 2
		# msg1.angular_velocity = 2
		msg1.theta=3.14
		msg.angular.z=1
		msg.linear.x =-2*msg.angular.z*math.sin(msg1.theta)
		msg.linear.y =0#*msg.angular.z*math.cos(msg1.theta)
		#msg.angular.z=1
		#msg.linear.x = -2
        #msg.linear.y = -2
		pub2.publish(msg)
		rate.sleep()
