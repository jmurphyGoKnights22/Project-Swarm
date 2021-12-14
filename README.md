# Project-Swarm

## About the Project

UCF Senior Design Project - Sponsored by Lockheed Martin

A simulated swarm of drones is shown to search a virtual urban environment to locate and identify a BB8 unit

## Getting Started

### For Those Who Already Know What They're Doing

This project is a single ROS package to be put in a catkin workspace. If you understand what a package is and how to use one in your own project, you can likely skip the rest of this readme since you probably already know what its telling you to do and why.

### Setting up Ubuntu 20.04 LTS

The simulated environment runs inside of a software called Gazebo, and relies heavily on a software called Robot Operating System, or ROS. Gazebo is only availible for Linux, and the version of ROS we are using specifically takes Ubuntu 20.04 LTS. Since almost everyone has a windows computer, our first step will be to get the correct operating system running. 

We recomend dual booting because it allows you to fully utilize the same computer hardware you probably already have, and you don't have to say goodbye to Windows. However, if you have a massively powerful graphics card, you may be able to run this project in a virtual machine. Virtual Machines are almost trivially easy to set up, but do not have very good GPU passthrough.

#### Virtual Machine

Again, we highly recomend dual booting over using a virtual machine, but in case you happen to have an industral grade GPU in your computer, you can set up a virtual machine to run our project. At the time of writing, VMware appears to have the best GPU passthrough. You can download [VMWare here](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html), find the [Ubuntu 20.04 LTS ISO here](https://ubuntu.com/download/desktop), and see a demonstarion of how to set up a virtual machine with VMware[this video.](https://youtu.be/BZE6WhOa7GM?t=119) Your virtual Machine will want about 30 GB of storage space. 

#### Dual Boot

As before, you can find the [Ubuntu 20.04 LTS ISO here.](https://ubuntu.com/download/desktop) Where setting up a virtual machine was simply downloading and using a seftware, dual booting will have you make a new partiaon, boot to an installation media with the Ubuntu ISO installed to it, and then boot to your choice of windows or Ubuntu through the BIOS boot menu when you power on your computer. In case dual booting or installing new operating sytems is new to you, you can follow [this guide.](https://youtu.be/CWQMYN12QD0) You will want to give your partition about 30 GB.

If you have the issue of a frozen purple or black screen when loading into ubuntu for the first time, try reinistalling Ubuntu and selecting the open source graphics driver instead of the proprietary graphics driver when installing. Later, if you have issues with weird, ghostly looking textures in Gaxebo, try updating to the correct proprietary driver for you GPU through the system settings menu. 

### Installing Gazebo and Looking Around the Virtual Environment


Run our script named `SDsetup.sh` with the command `sudo bash SDsetup.sh` from whatever directory you downloaded the script to. This script will add to your .bashrc file, set up a catkin workspace, and place our github repo inside of it alongside a few other github repos. If you don't want to run the script, you can run each individual command found in the script one by one in your terminal with sudo permissions instead. Those commands are coppied below for your convenience.

```
apt update
apt install git
apt install ros-noetic-desktop-full
source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
echo "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/catkin_ws/src/gazebo_models_worlds_collection/models" >> ~/.bashrc
source ~/.bashrc 
rosdep init 
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
```

Now, you will need to build your workspace by navigating to the top level directory of the workspace and running the command `catkin_make` and then `source devel/setup.sh`. You can launch the world file to take a look around with the command `roslaunch Project-Swarm only_world.launch` and you can spawn a BB-8 model into the world using the command `roslaunch Project-Swarm only_bb8.launch`. You can use the mouse to change your view in the envrionment. Left click and drag pans the camera, right click and drag zooms the camera, and middle click and drag rotates the camera. It may sound childish, but if you select BB-8 with a left click, then right click on him, you can open the "apply forces" panel and kick him around. This is way more entertaining than you think, and if you've made it this far, you owe it to yourself to try it.


## Running the Simulation

Coming to a senior design 2 presentation near you in Spring 2022!

## Team Members

Andrew Borg (AI & Pathfinding, CNN & Computer Vision, Machine Learning)
Bobby Pappas (AI & Pathfinding, CNN & Computer Vision, Machine Learning)
James Murphy (Project Lead, AI & Pathfinding, CNN & Computer Vision, Machine Learning)
Matthew Hubbs (AI & Pathfinding, Gazebo & Simulation, Machine Learning)
Sebastian Almeida (CNN/Computer Vision, Gazebo & Simulation, Machine Learning)
