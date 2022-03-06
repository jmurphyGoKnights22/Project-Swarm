#! /usr/bin/env python3

# add the line below to put_robot_in_world.launch
# <node pkg="hector_quadrotor_demo" type="opencv-camera.py" name="start_camera" output="screen"/>


import yolov5_detection
import rospy
# from std_msgs.msg import Bool
from std_msgs.msg import Int16
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
homedir = str(et.io.HOME)
# instantiate publisher for reporting finding bb8, or almost finding
shoot_him_pub = None
squint_at_him_pub = None
# Set device to cuda or CPU, Load custom YOLOv5 model and weights, Link device to loaded model
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load('ultralytics/yolov5', 'custom', path= homedir + "/catkin_ws/src/hector_quadrotor_noetic/hector_quadrotor/hector_quadrotor_gazebo/launch/src/bestPizza500.pt", force_reload=True)
model.to(device)

def img_callback(data, cam_num):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    real_image = PIL_img.fromarray(bgr2rgb)
    found_bb8 = yolov5_detection.run_detection(real_image, model, cam_num, squint_at_him_pub)
    if found_bb8:
        shoot_him_pub.publish(Int16(cam_num))
        print("BB* found on cam " + str(cam_num) + "!!")
    # print("Camera booted!")
    # cv2.imshow("Raw Image 1", cv_image)
    # cv2.waitKey(3)

def main():
    print("Camera feed starting up.....")
    rospy.init_node('object_detection')

    # prep shoot him pub
    global shoot_him_pub 
    shoot_him_pub = rospy.Publisher('/uav1/found_bb8', Int16, queue_size=10)
    shoot_him_pub.publish(Int16(-1))
    # prep squint at him pub
    global squint_at_him_pub 
    squint_at_him_pub = rospy.Publisher('/uav1/found_bb8', Int16, queue_size=10)
    squint_at_him_pub.publish(Int16(-1))
    # create subscribers to the cameras to keep an eye out for him
    img_sub1 = rospy.Subscriber("/uav1/front_cam/camera/image", Image, img_callback, 1)
    img_sub2 = rospy.Subscriber("/uav2/front_cam/camera/image", Image, img_callback, 2)
    img_sub3 = rospy.Subscriber("/uav3/front_cam/camera/image", Image, img_callback, 3)
    img_sub4 = rospy.Subscriber("/uav4/front_cam/camera/image", Image, img_callback, 4)
    img_sub5 = rospy.Subscriber("/uav5/front_cam/camera/image", Image, img_callback, 5)
    # prevents node from dying until explicitly killed
    rospy.spin()

main()