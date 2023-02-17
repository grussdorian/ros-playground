#!/usr/bin/env python3

import rospy

if __name__ == "__main__":
    rospy.init_node("test_node")
    rospy.loginfo("Test node has been started")
    # rospy.logwarn("A warning")
    # rospy.logerr("Test error")

    # rospy.sleep(1.0)
    # rospy.loginfo("end of program")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("hello ")
        rate.sleep()