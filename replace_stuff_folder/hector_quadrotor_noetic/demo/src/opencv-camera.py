#! /usr/bin/env python3

# add the line below to put_robot_in_world.launch
# <node pkg="hector_quadrotor_demo" type="opencv-camera.py" name="start_camera" output="screen"/>

import yolov5_detection
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from PIL import Image as PIL_img

bridge = CvBridge()

def img_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    real_image = PIL_img.fromarray(bgr2rgb)
    yolov5_detection.run_detection(real_image)
    print("Camera booted!")
    cv2.imshow("Raw Image", cv_image)
    cv2.waitKey(3)

def main():
    print("Camera feed starting up.....")
    rospy.init_node('start_camera')
    img_sub = rospy.Subscriber("/front_cam/camera/image", Image, img_callback)
    rospy.spin()

main()