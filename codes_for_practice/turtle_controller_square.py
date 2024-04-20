#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose  # A representation of pose in free space, composed of position and orientation. 
from geometry_msgs.msg import Twist # This expresses velocity in free space broken into its linear and angular parts.
from math import radians

def pose_callback(xpose):
    
    cmdl = Twist()
    
    r= rospy.Rate(5)

    cmdl.linear.x = 1
    cmdl.linear.y = 0
    cmdl.angular.z = 0 

    if xpose.x > 9 :
        cmdl.linear.x = 0
        cmdl.linear.y = 1
        cmdl.angular.z = radians(30)

    if xpose.y >= 9 :
        cmdl.linear.x = 0
        cmdl.linear.y = 1
        cmdl.angular.z = radians(45)

    if xpose.x <= 5.5:
        cmdl.linear.x = 0
        cmdl.linear.y = 1
        cmdl.angular.z = radians(45)

    if xpose.y <= 5.5:
        cmdl.linear.x = 0
        cmdl.linear.y = 1
        cmdl.angular.z = radians(45)
            
      
    pub.publish(cmdl)
   
  
   
if __name__=='__main__':
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback)
    rospy.loginfo("node has been started")
    rospy.spin()
