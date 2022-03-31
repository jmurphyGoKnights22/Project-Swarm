#! /usr/bin/env python3

# run this python file with either rosrun or with python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16
isFound = False

def found_callback(message):
    isFound = True

def track1():
    print("Begining rails search 1 in train_station.py")
    rospy.init_node('single_rails_search')
    pub = rospy.Publisher('uav1/cmd_vel', Twist, queue_size=10)
    # this will stop the search when something is found
    found_sub = rospy.Subscriber("found_bb8_shoot", Int16, found_callback)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    global isFound
    while (not isFound):
        print("maneuver 1, up 2.5 meters in 1 second")
        # up 2.5 meters in 1 second
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 2.5
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1) # Sleeps for 1 sec
        print("maneuver 2, forward 10 meters in 5 seconds")
        # forward 10 meters in 5 seconds
        twist.linear.x = 2.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)
        print("maneuver 3, pivot turn right 90 degrees in 1 second")
        # pivot turn right 90 degrees in 1 second
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = -3.8
        pub.publish(twist)
        rospy.sleep(1)
        print("maneuver 4, halt 5 seconds")
        # halt 5 seconds
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)

    # hover in place, but dont kill the process
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.spin()

def track2():
    print("Begining rails search 2 in train_station.py")
    rospy.init_node('single_rails_search')
    pub = rospy.Publisher('uav2/cmd_vel', Twist, queue_size=10)
    # this will stop the search when something is found
    found_sub = rospy.Subscriber("found_bb8_shoot", Int16, found_callback)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    global isFound
    while (not isFound):
        print("maneuver 1, up 2.5 meters in 1 second")
        # up 2.5 meters in 1 second
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 2.5
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1) # Sleeps for 1 sec
        print("maneuver 2, forward 10 meters in 5 seconds")
        # forward 10 meters in 5 seconds
        twist.linear.x = 2.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)
        print("maneuver 3, pivot turn right 90 degrees in 1 second")
        # pivot turn right 90 degrees in 1 second
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = -3.8
        pub.publish(twist)
        rospy.sleep(1)
        print("maneuver 4, halt 5 seconds")
        # halt 5 seconds
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)

    # hover in place, but dont kill the process
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.spin()

def track3():
    print("Begining rails search 3 in train_station.py")
    rospy.init_node('single_rails_search')
    pub = rospy.Publisher('uav3/cmd_vel', Twist, queue_size=10)
    # this will stop the search when something is found
    found_sub = rospy.Subscriber("found_bb8_shoot", Int16, found_callback)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    global isFound
    while (not isFound):
        print("maneuver 1, up 2.5 meters in 1 second")
        # up 2.5 meters in 1 second
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 2.5
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1) # Sleeps for 1 sec
        print("maneuver 2, forward 10 meters in 5 seconds")
        # forward 10 meters in 5 seconds
        twist.linear.x = 2.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)
        print("maneuver 3, pivot turn right 90 degrees in 1 second")
        # pivot turn right 90 degrees in 1 second
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = -3.8
        pub.publish(twist)
        rospy.sleep(1)
        print("maneuver 4, halt 5 seconds")
        # halt 5 seconds
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)

    # hover in place, but dont kill the process
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.spin()

def track4():
    print("Begining rails search 4 in train_station.py")
    rospy.init_node('single_rails_search')
    pub = rospy.Publisher('uav4/cmd_vel', Twist, queue_size=10)
    # this will stop the search when something is found
    found_sub = rospy.Subscriber("found_bb8_shoot", Int16, found_callback)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    global isFound
    while (not isFound):
        print("maneuver 1, up 2.5 meters in 1 second")
        # up 2.5 meters in 1 second
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 2.5
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1) # Sleeps for 1 sec
        print("maneuver 2, forward 10 meters in 5 seconds")
        # forward 10 meters in 5 seconds
        twist.linear.x = 2.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)
        print("maneuver 3, pivot turn right 90 degrees in 1 second")
        # pivot turn right 90 degrees in 1 second
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = -3.8
        pub.publish(twist)
        rospy.sleep(1)
        print("maneuver 4, halt 5 seconds")
        # halt 5 seconds
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)

    # hover in place, but dont kill the process
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.spin()

def track5():
    print("Begining rails search 5 in train_station.py")
    rospy.init_node('single_rails_search')
    pub = rospy.Publisher('uav5/cmd_vel', Twist, queue_size=10)
    # this will stop the search when something is found
    found_sub = rospy.Subscriber("found_bb8_shoot", Int16, found_callback)
    # warm up the topic? idk?
    for i in range(10):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(0.1)
    # linear is m/s and angular is rad/s. length of large block is something like 41- -11 = 52 meters. small is 30 meters. 85 meters total
    # block is about 85 meters wide too
    global isFound
    while (not isFound):
        print("maneuver 1, up 2.5 meters in 1 second")
        # up 2.5 meters in 1 second
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 2.5
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(1) # Sleeps for 1 sec
        print("maneuver 2, forward 10 meters in 5 seconds")
        # forward 10 meters in 5 seconds
        twist.linear.x = 2.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)
        print("maneuver 3, pivot turn right 90 degrees in 1 second")
        # pivot turn right 90 degrees in 1 second
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = -3.8
        pub.publish(twist)
        rospy.sleep(1)
        print("maneuver 4, halt 5 seconds")
        # halt 5 seconds
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
        rospy.sleep(5)

    # hover in place, but dont kill the process
    twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
    twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
    pub.publish(twist)
    rospy.spin()