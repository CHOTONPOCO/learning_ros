#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('topic_publisher')
pub = rospy.Publisher('counter', Int32, queue_size=10)
rate = rospy.Rate(2)
count=0
while not rospy.is_shutdown():
    count += 1
    pub.publish(count)
    rate.sleep()
