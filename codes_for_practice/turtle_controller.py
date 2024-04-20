#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def pose_callback(pose):
    cmd = Twist()
    if pose.x > 2.0 or pose.x<2.0 or pose.y > 2.0 or pose.y<2.0 :
        cmd.linear.x=0.0
        cmd.angular.z=0.0
    else:
        cmd.linear.x = 5.0
        cmd.angular.z=0.0
    pub.publish(cmd)
            

    # cmd.linear.x= 5.0
    # cmd.angular.z= 0.0
    # pub.publish(cmd)


    
if __name__=='__main__':
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback)
    rospy.loginfo("node has been started")
    rospy.spin()