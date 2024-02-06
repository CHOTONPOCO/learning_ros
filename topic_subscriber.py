#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    print(msg.data)

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('counter', Int32, callback)
rospy.spin()