#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sensor_msgs.msg
import random
import numpy as np
from geometry_msgs.msg import Twist
from itertools import *
from operator import itemgetter
import os

def LaserScanProcess(data):
    lidar_scan = np.array(data.ranges)
    # get the value for linear and angular velocities
    linear_x = ???
    angular_z = ???

def controller():
    rospy.init_node('listener', anonymous=True)

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("scan", sensor_msgs.msg.LaserScan , LaserScanProcess)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        command = Twist()
        command.linear.x = linear_x
        command.angular.z = angular_z
        pub.publish(command)
        rate.sleep()

def main():
    os.system('gnome-terminal -x ' 'roslaunch hackathon level2.launch')    ##open the map with the bot and the world
    # time.sleep(5)
    try:
        controller()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    linear_x = 0
    angular_z = 0
    PI = 3.14
    main()
