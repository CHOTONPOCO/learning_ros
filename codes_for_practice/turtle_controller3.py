#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist 
#from geometry_msgs.msg import Pose
#from geometry_msgs.msg import Pose
def pose_callback(xpose):
    cmd = Twist()
    if xpose.x > 5.54 and xpose.x < 8.54 :
        cmd.linear.x = 1.0
        cmd.linear.y = 0.0
    if xpose.x > 8.54 and xpose.y < 7.04:
        cmd.linear.x = 1.0
        cmd.linear.y = 1.0
    if xpose.y > 7.04 and xpose.y < 8.54:
        cmd.linear.x = -1.0
        cmd.linear.y = 1.0
    if  xpose.y > 8.54 and xpose.x > 5.54:
        cmd.linear.x = -1.0
        cmd.linear.y = 0.0
    if  xpose.x < 5.54 and xpose.y >7.04:
        cmd.linear.x = -1.0
        cmd.linear.y = -1.0
    if  xpose.x < 5.54 and xpose.y < 7.04:
        cmd.linear.x = 1.0
        cmd.linear.y = -1.0
  
    pub.publish(cmd)
    #pub.publish(msg)
    #sub.subscribe(msg)        

    # cmd.linear.x= 5.0
    # cmd.angular.z= 0.0
  


    
if __name__=='__main__':
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback)
    rospy.loginfo("node has been started")
    rospy.spin()
