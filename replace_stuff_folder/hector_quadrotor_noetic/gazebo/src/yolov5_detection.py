#! /usr/bin/env python3

import rospy

import earthpy as et
import rospy
# from std_msgs.msg import Bool
from std_msgs.msg import Int16
import sys
sys.path.append("./yolov5/models/")
import torch
import os
from  PIL import Image
import numpy as np

homedir = str(et.io.HOME)
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load('ultralytics/yolov5', 'custom', path= homedir + "/catkin_ws/src/hector_quadrotor_noetic/hector_quadrotor/hector_quadrotor_gazebo/launch/src/bestPizza500.pt", force_reload=True)
model.to(device)

def run_detection(real_image, model, droneId, publisher=None):
    # Globals    
    SCORE_THRESHOLD = 0.5

    # Verify our current Directory, Check if cuda is available for NVIDIA GPUs, else CPU (RIP AMD)
    # print("Current Directory Scope: " + os.getcwd() + "\n")
    # print("cuda is availible?: " + str(torch.cuda.is_available()))

    # Set device to cuda or CPU, Load custom YOLOv5 model and weights, Link device to loaded model

    # load an image. in the real thing, this would be a parameter
    # Toggle a True Positive and True Negative below

    # im_frame = Image.open("bb8_sample28.png") # true positive, bb8 is in this picture
    # im_frame = Image.open("bb8_paint_true_neg.png") # true negative, bb8 is not in this image

    fromPILtoNp = np.array(real_image)

    # change to be tensor with axes to be (batch, channels, height, width)
    np_frame = np.transpose(fromPILtoNp, axes=[2,0,1])

    # Run the yolov5 Model {input dtype : nparray(R,G,B), output(Detections)} 
    result = model(np_frame)

    
    # If it detected a True Positive, shows vertices for prediction, confidence score, class, name
    # If it detected a True Negative, it will be an empty tensor instead
    # print(result.pandas().xyxy[0])

    # Isolate the confidence score
    confidence = result.xyxyn[0][:, -2]
    print("Confidence Score Tensor: " + str(confidence))
    print("Drone Id: " + str(droneId))

    # If we get a True Negative, return false since we arent even looking at something that *might* be bb8
    if len(confidence) == 0:
        print("\n")
        found_bb8 = False # redundant, but self documenting line
        return found_bb8
    
    # This will break if we see more than one thing with a non zero confididence of it being bb8. will only take the first item
    extracted_confidence = confidence[0]
    if extracted_confidence >= 0.5:
        # publisher.publish(Bool(True))
        print("KILL HIM! KILL HIM NOW! (cam " + str(droneId) + ")\n")
        found_bb8 = True
        return found_bb8
    else: 
        publisher.publish(Int16(droneId)) # SEBASIAN LOOK AT THIS THIS WHERE U SUBSCRIBE TO KNOW IF YOU DO YOUR NAVIGATION SEQUENCE BREAK
        print("HAHA, I'M IN DANGER (cam " + str(droneId) + ")\n")
        found_bb8 = False
        return False
    

