#! /usr/bin/env python3

# add the line below to put_robot_in_world.launch
# <node pkg="hector_quadrotor_demo" type="opencv-camera.py" name="start_camera" output="screen"/>


import yolov5_detection
import rospy
from std_msgs.msg import Bool
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from PIL import Image as PIL_img
import sys
sys.path.append("./yolov5/models/")
import torch
import os
import earthpy as et

bridge = CvBridge()
print("Current Directory Scope: " + os.getcwd() + "\n")
# homedir = str(et.io.HOME)
# Set device to cuda or CPU, Load custom YOLOv5 model and weights, Link device to loaded model
# torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = torch.hub.load('ultralytics/yolov5', 'custom', path= homedir + "/catkin_ws/src/hector_quadrotor_noetic/hector_quadrotor/hector_quadrotor_gazebo/launch/src/bestPizza500.pt", force_reload=True)
# model.to(device)
pub = None

def img_callback(data):
    rate = rospy.Rate(1)
    global pub
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    real_image = PIL_img.fromarray(bgr2rgb)
    # yolov5_detection.run_detection(real_image, yolov5_detection.model, pub, 1)
    # print("Camera booted!")
    cv2.imshow("Raw Image 1", cv_image)
    cv2.waitKey(3)
    rate.sleep()

def main():
    print("Camera feed starting up.....")
    rospy.init_node('object_detection')
    global pub 
    pub = rospy.Publisher('/uav1/found_bb8', Bool, queue_size=5)
    pub.publish(Bool(False))
    img_sub = rospy.Subscriber("/uav1/front_cam/camera/image", Image, img_callback)
    rospy.spin()

main()