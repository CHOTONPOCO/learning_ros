#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	rospy.init_node("draw_circle")
	rospy.loginfo("Started")

	pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

	rate = rospy.Rate(5)

	while not rospy.is_shutdown():
		msg = Twist()
		msg.linear.x =2
		msg.angular.z=2
		#msg.linear.y =2
		#msg.angular.z=1/2
		#msg.linear.x = -2
        #msg.linear.y = -2
		pub.publish(msg)
		rate.sleep()
