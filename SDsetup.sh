#!/bin/sh
# This script is to be run on a fresh ubuntu install. if you already have things installed, there could be trouble.
apt update
apt install git
apt install ros-noetic-desktop-full

source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/catkin_ws/src/gazebo_models_worlds_collection/models" >> ~/.bashrc

source ~/.bashrc # source should do the same thing as closeing and reopening the terminal to make changes in .bashrc take effect.

rosdep init # possibly redundent, but won't hurt anything to do it again
rosdep update

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash

cd ~/catkin_ws/src
git clone https://github.com/patrick1bauer/autonomous_search_with_ai.git
git clone https://github.com/chaolmu/gazebo_models_worlds_collection.git
cd ~/catkin_ws
catkin_make
source devel/setup.sh

cd ~/catkin_ws/src
apt install curl
curl -sSL http://get.gazebosim.org | sh
cp ./autonomous_search_with_ai/worlds/urban.world /usr/share/gazebo-11/worlds
