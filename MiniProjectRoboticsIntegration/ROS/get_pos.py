#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import sys
import requests
robot_x = 0


def pose_callback(pose):
	global robot_x
	#time.sleep(2)
	url = 'https://abdullah97ahmed.pythonanywhere.com/insertCoordinates'
	myobj = {'x': pose.x, 
		'y':pose.y,
		'theta':pose.theta}
	
	x = requests.post(url, json = myobj)
	rospy.loginfo(x.text) 
	robot_x = pose.x


def move_turtle(lin_vel,ang_vel):

    global robot_x
    rospy.init_node('move_turtle', anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  
    rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
    rate = rospy.Rate(10) # 10hz
 
    vel = Twist()
    while not rospy.is_shutdown():
        
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

       #rospy.loginfo("Linear Vel = %f: Angular Vel = %f",lin_vel,ang_vel)

        pub.publish(vel)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle(float(sys.argv[1]),float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass