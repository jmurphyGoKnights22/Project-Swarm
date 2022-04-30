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
homedir = str(et.io.HOME)
# Set device to cuda or CPU, Load custom YOLOv5 model and weights, Link device to loaded model
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load('ultralytics/yolov5', 'custom', path= homedir + "/catkin_ws/src/Project-Swarm/src/3-25V5Best.pt", force_reload=True)
model.to(device)
pub = None

def img_callback(data):
    global pub
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    real_image = PIL_img.fromarray(bgr2rgb)
    found_bb8, results, squint_bb8 = yolov5_detection.run_detection(real_image, model, -1)
    possible_bounding_boxes = results.xyxyn[0][:,:-1]
    for i in possible_bounding_boxes:
        # cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
        cv2.rectangle(cv_image, (int(i[0]*512), int(i[1]*512)), (int(i[2]*512), int(i[3]*512)), (255, 0, 0), 2)
    cv2.imshow("Raw Image", cv_image)
    cv2.waitKey(3)

def main():
    print("Camera feed starting up.....")
    rospy.init_node('start_camera')
    global pub 
    pub = rospy.Publisher('/found_bb8', Bool, queue_size=5)
    pub.publish(Bool(False))
    img_sub = rospy.Subscriber("uav1/front_cam/camera/image", Image, img_callback)
    rospy.spin()


main()