#! /usr/bin/env python3

# This starts the timer, starts the 5 rails scripts, and stops the timer when bb8 is found

import clock
import os
# import single_drone_rails1
# import single_drone_rails2
# import single_drone_rails3
# import single_drone_rails4
# import single_drone_rails5
import threading
import rospy
from std_msgs.msg import Int16
from train_station import track1, track2, track3, track4, track5

# def found_callback(message):
#     print("drone " + message + " found bb8!")
    # stop the clock here
    # master_detection is rigged such that when we find the drone it ought to open up the camera feed and draw a box around our hit

def main():
    # found_sub = rospy.Subscriber("found_bb8_shoot", Int16, found_callback)
    # start the clock here. I think it needs to be put in a thread so that it doesnt hog the cpu

    rospy.init_node('five_rails_search')

    # I was told this was the right way to do this: https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another
    t1 = threading.Thread(target=track1)
    t2 = threading.Thread(target=track2)
    t3 = threading.Thread(target=track3)
    t4 = threading.Thread(target=track4)
    t5 = threading.Thread(target=track5)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print("All rails scripts have finished")


if __name__=="__main__":
    main()