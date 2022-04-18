#! /usr/bin/env python3

import rospy


import rospy
from std_msgs.msg import Bool
import sys
sys.path.append("./yolov5/models/")
import torch
import os
from  PIL import Image
import numpy as np

def run_detection(real_image, model, cam_num):
    # Globals    
    SCORE_THRESHOLD = 0.85
    print_results = False

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
    if print_results:
        print("Confidence Score Tensor: " + str(confidence))

    # If we get a True Negative, return false since we arent even looking at something that *might* be bb8
    if len(confidence) == 0:
        found_bb8 = False # redundant, but self documenting line
        squint_bb8 = False
        return found_bb8, result, squint_bb8

    # This will break if we see more than one thing with a non zero confididence of it being bb8. will only take the first item
    extracted_confidence = confidence[0]
    if extracted_confidence >= SCORE_THRESHOLD:
        if print_results: 
            print("Drone " + cam_num + ": KILL HIM! KILL HIM NOW!" + ")\n")
        found_bb8 = True
        squint_bb8 = False
        return found_bb8, result, squint_bb8
    else: 
        if print_results: 
            print("Drone " + cam_num + ": HAHA, I'M IN DANGER " + ")\n")
        found_bb8 = False
        squint_bb8 = True
        return False, result, squint_bb8
    

