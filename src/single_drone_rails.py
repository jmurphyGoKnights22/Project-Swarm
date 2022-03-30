#! /usr/bin/env python3

# run this python file with either rosrun or with python3
import rospy
from geometry_msgs.msg import Twist

def main():
    print("Begining rails search in single_drone_rails.py")
    rospy.init_node('single_rails_search')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    while (True):
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 2.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)

if __name__=="__main__":
    main()