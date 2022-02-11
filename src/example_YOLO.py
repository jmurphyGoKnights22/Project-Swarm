#! /usr/bin/env python3


import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def img_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    # I imagine detect(img) is the method that runs the yolo model on the image passed as a parameter 
    # detect(bgr2rgb)
        


def main():
    print("YOLO feeds starting up.....")
    rospy.init_node('image_detector_YOLO')
    img_sub1 = rospy.Subscriber("uav1/front_cam/camera/image", Image, img_callback)
    img_sub2 = rospy.Subscriber("uav2/front_cam/camera/image", Image, img_callback)
    img_sub3 = rospy.Subscriber("uav3/front_cam/camera/image", Image, img_callback)
    img_sub4 = rospy.Subscriber("uav4/front_cam/camera/image", Image, img_callback)
    img_sub5 = rospy.Subscriber("uav5/front_cam/camera/image", Image, img_callback)
    rospy.spin()

main()