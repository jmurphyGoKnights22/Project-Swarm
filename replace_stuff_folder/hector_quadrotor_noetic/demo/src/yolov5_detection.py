#! /usr/bin/env python3

import sys
sys.path.append("./yolov5/models/")
import torch
import os
from  PIL import Image
import numpy as np

def run_detection(real_image):
    # Globals    
    SCORE_THRESHOLD = 0.5

    # Verify our current Directory, Check if cuda is available for NVIDIA GPUs, else CPU (RIP AMD)
    print("Current Directory Scope: " + os.getcwd() + "\n")
    print("cuda is availible?: " + str(torch.cuda.is_available()))

    # Set device to cuda or CPU, Load custom YOLOv5 model and weights, Link device to loaded model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.hub.load('ultralytics/yolov5', 'custom', path="bestPizza500.pt", force_reload=True)
    model.to(device)

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

    # Below might have a better option to reduce runtime for a O(1) comparison instead of doing a type conversion first

    # If we get a True Negative, feature map confidence to negative
    if str(confidence) == "tensor([])":
        confidence = -1
    
    # Print the boolean result if we have a score > SCORE_THRESHOLD.
    print("Did we find BB8?: " + (str(True) if confidence > SCORE_THRESHOLD else str(False)))

