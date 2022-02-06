#! /usr/bin/env python3

# add the line below to put_robot_in_world.launch
# <node pkg="hector_quadrotor_demo" type="opencv-camera.py" name="start_camera" output="screen"/>


import rospy
import cv2
from PIL import Image as PIL_img
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
image_counter = 107

def img_callback(data):
    global image_counter
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    real_image = PIL_img.fromarray(bgr2rgb)
    cv2.imshow("Tab in here and press Space to save image", cv_image)
    key_code = cv2.waitKey(1)
    if key_code % 256 == 32:
        file_name = "ProjectSwarmTrainingImages/bb8_sample{}.png".format(image_counter)
        real_image.save(file_name)
        print(file_name + " has been saved!")
        image_counter += 1
        


def main():
    print("Camera feed starting up.....")
    rospy.init_node('start_camera')
    img_sub = rospy.Subscriber("/front_cam/camera/image", Image, img_callback)
    rospy.spin()

main()