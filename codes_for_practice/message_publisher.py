#!/usr/bin/env python3
import rospy
from my_robot_tutorials.msg import Complex
from random import random
rospy.init_node('message_publisher')
pub = rospy.Publisher('complex', Complex, queue_size=10)
rate = rospy.Rate(2)
a =  float(input("Enter values of a:"))
b =  float(input("Enter values of b:"))
while not rospy.is_shutdown():
   msg = Complex()
   msg.real = a
   msg.imaginary = b
   pub.publish(msg)
   rate.sleep()
