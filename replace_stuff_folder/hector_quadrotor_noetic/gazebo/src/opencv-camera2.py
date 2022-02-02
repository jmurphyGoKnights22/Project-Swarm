#! /usr/bin/env python3

# add the line below to put_robot_in_world.launch
# <node pkg="hector_quadrotor_demo" type="opencv-camera.py" name="start_camera" output="screen"/>


import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def img_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    print("Camera booted!")
    cv2.imshow("Raw Image2", cv_image)
    cv2.waitKey(3)

def main():
    print("Camera feed starting up.....")
    rospy.init_node('start_camera__')
    img_sub = rospy.Subscriber("/uav2/front_cam/camera/image", Image, img_callback)
    rospy.spin()

main()