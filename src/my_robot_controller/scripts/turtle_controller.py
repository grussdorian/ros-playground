#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist
import random
prev_x = 0

def call_set_pen_service(r, g, b, width, off):
  try:
    set_pen = rospy.ServiceProxy("/turtle1/set_pen",SetPen )
    response = set_pen(r, g, b, width, off)
    # rospy.loginfo(response)
  except rospy.ServiceException as e:
    rospy.logwarn(e)

def pose_callback(pose: Pose):
  s = random.uniform(0, 1)
  a = random.uniform(-1,1)
  cmd = Twist()
  if pose.x > 9.0 or pose.x<2 or pose.y>9 or pose.y<2: 
    cmd.linear.x = 1.0 + s*5
    cmd.angular.z = a*2  +0.7
  else:
    cmd.linear.x = 10.0
    cmd.angular.z = 0.0
  pub.publish(cmd)  

  global prev_x
  if pose.x >= 5.5 and prev_x < 5.5:
    rospy.logwarn("Set colour to red")
    call_set_pen_service(255,0,0,3, 0)
  elif pose.x < 5.5 and prev_x >= 5.5: 
    rospy.logwarn("Set colour to green")
    call_set_pen_service(0,255,0,3, 0)
  prev_x = pose.x

if __name__ == "__main__":
  rospy.init_node("turtle_controller")
  rospy.wait_for_service("/turtle1/set_pen")
  # call_set_pen_service(255,0,0,3, 0)
  pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10 )
  sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
  rospy.loginfo("controller node has been started")
  rospy.spin()