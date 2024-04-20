#!/usr/bin/env python3
import rospy
from my_robot_tutorials.msg import Complex
def callback(msg):
    print ('Real:', msg.real)
    print ('Imaginary:', msg.imaginary)
    print
rospy.init_node('message_subscriber')
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin()
