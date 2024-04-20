#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import math 

rospy.init_node('topic_publisher')
pub = rospy.Publisher('counter', Float32, queue_size=50)
rate = rospy.Rate(2)
a =  float(input("Enter values of a:"))
b =  float(input("Enter values of b:"))
c =  float(input("Enter values of c:"))
x1=(-b+math.sqrt(b*b-4*a*c))/2*a
x2=(-b-math.sqrt(b*b-4*a*c))/2*a
while not rospy.is_shutdown():
    pub.publish(x1)
    pub.publish(x2)
    #count += 1
    rate.sleep()
