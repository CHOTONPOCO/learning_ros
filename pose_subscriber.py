#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

#def pose_callback(msg):
def pose_callback(msg):
    rospy.loginfo(msg)
    #rospy.loginfo("(" + str(msg.x) + "," + str(msg.y) + ")" )
    #"(" + str(msg.x) + "," + str(msg.y) + ")" 
if __name__ == '__main__':
    rospy.init_node("pose_subscriber")
    sub=rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("Node has been started")
    rospy.spin()

