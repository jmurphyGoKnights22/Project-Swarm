#! /usr/bin/env python3

# run this python file with either rosrun or with python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16

def track1():
    print("Begining arise 1 in begin_arise.py")
    pub = rospy.Publisher('uav1/cmd_vel', Twist, queue_size=10)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    # up 2.0 meters in 1 second
    twist = Twist()
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 3.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1) # Sleeps for 1 sec
    # halt 2 seconds
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(2)

def track2():
    print("Begining arise 2 in begin_arise.py")
    pub = rospy.Publisher('uav2/cmd_vel', Twist, queue_size=10)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    # up 2.5 meters in 1 second
    twist = Twist()
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 3.5
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1) # Sleeps for 1 sec
    # halt 2 seconds
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(2)

def track3():
    print("Begining arise 3 in begin_arise.py")
    pub = rospy.Publisher('uav3/cmd_vel', Twist, queue_size=10)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    # up 3 meters in 1 second
    twist = Twist()
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 4.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1) # Sleeps for 1 sec
    # halt 2 seconds
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(2)

def track4():
    print("Begining arise 4 in begin_arise.py")
    pub = rospy.Publisher('uav4/cmd_vel', Twist, queue_size=10)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    # up 3.5 meters in 1 second
    twist = Twist()
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 4.5
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(1) # Sleeps for 1 sec
    # halt 2 seconds
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.sleep(2)

