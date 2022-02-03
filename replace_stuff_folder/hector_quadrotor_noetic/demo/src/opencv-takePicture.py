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
    cv2.imshow("Raw Image", cv_image)
    key_code = cv2.waitKey(1)
    if key_code % 256 == 32:
        file_name = "~/catkin_ws/src/hector_quadrotor_noetic/hector_quadrotor/hector_quadrotor_demo/launch/src/images/bb8_sample.jpg"
        cv2.imwrite(file_name, cv_image)
        print(file_name + " has been saved!")
        


def main():
    print("Camera feed starting up.....")
    rospy.init_node('start_camera')
    img_sub = rospy.Subscriber("/front_cam/camera/image", Image, img_callback)
    rospy.spin()

main()