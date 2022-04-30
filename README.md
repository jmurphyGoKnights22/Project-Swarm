# Project-Swarm

## About the Project

UCF Senior Design Project - Sponsored by Lockheed Martin

A simulated swarm of drones is shown to search a virtual urban environment to locate and identify a BB8 unit

## Getting Started

### For Those Who Already Know What They're Doing

This project is a single ROS package to be put in a catkin workspace. It also relies on a few other packages If you understand what a package is and how to use one in your own project, you can likely skip the rest of this readme since you probably already know what its telling you to do and why.

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
git clone https://github.com/ros-geographic-info/geographic_info.git
git clone https://github.com/ros-geographic-info/unique_identifier.git
git clone https://github.com/RAFALAMAO/hector-quadrotor-noetic.git
git clone https://github.com/ros-teleop/teleop_twist_keyboard.git
git clone https://github.com/ultralytics/yolov5.git
cd ~/catkin_ws
catkin_make
source devel/setup.sh
cd ~/catkin_ws/src
apt install curl
curl -sSL http://get.gazebosim.org | sh
cp ./autonomous_search_with_ai/worlds/urban.world /usr/share/gazebo-11/worlds
```

Now, you will need to build your workspace by navigating to the top level directory of the workspace and running the command `catkin_make` and then `source devel/setup.sh`. You can launch the world file to take a look around with the command `roslaunch Project-Swarm bb8_and_world.launch`. You can use the mouse to change your view in the envrionment. Left click and drag pans the camera, right click and drag zooms the camera, and middle click and drag rotates the camera. It may sound childish, but if you select BB-8 with a left click, then right click on him, you can open the "apply forces" panel and kick him around. This is way more entertaining than you think, and if you've made it this far, you owe it to yourself to try it.

### Installing Pytorch and CUDA

You will need to install [Pytorch](https://pytorch.org/) for the YOLO object detection to work. You will also need to install (CUDA)[https://developer.nvidia.com/cuda-toolkit] for your machine to utilize your Nividia GPU when running the YOLO object detection model. You will need to match the version of CUDA with the version of Pytorch. One team member used version 10 and another used version 11. CUDA will not work if you dont have a Nividia GPU, and Pytorch is not compadible with the AMD version of CUDA, so if you have an AMD card, or no GPU at all, then download the CPU version of Pytorch and hope your CPU is able to run it all on its own. It probably wont be able to, but you may try if you want to. 

We used [this video tutorial](https://www.youtube.com/watch?v=4gcqGxBIUnc&ab_channel=PinkLAB) when installing CUDA on ubuntu. It is much easier on windows than Ubuntu, but unfortunately, Gazebo is only availible on ubuntu at the time of this project.

### Problems We Had

If you are getting a blue or black screen of death when trying to install ubuntu as a dual boot, then you probably picked the wrong graphics driver when installing. Start over and try the option you havent picked yet. If you have an AMD card, then I'm sorry for the pain you are sure to go through.

If your grass texture looks like yellow and black hazzard stripes, you are either missing a file in the Gazebo Models and Worlds github repo, or your .bashrc file is missing a reference to the correct folders in there. If that's the case, I probably made a mistake in the setup script. I appologize for that error, and good luck fixing it, at least you know where to look.

If a command just refuses to run, then you're probably missing a package, and I forgot to add it to the setup script. Look through the console output, find what package it is complaining about not having, and apt-get install it. Going off of [this example](https://blog.600mb.com/a?ID=01800-a3c81eca-b2f6-41fe-884f-2d000ea6d767), if the output says something like `missing package octomap_ros` then you would run the command `sudo apt-get install ros-noetic-octomap-ros`

## Running the Simulation

Look in `launch_order.txt` for details. Run each command in its own terminal. If a command fails, read the output because it is more than likely a problem with missing a package. See what package that is, and then apt-get install it.

In the main branch, each drone is using a 2d lidar and each drone is using its own seperate map, which is why the drones split off into two groups of two. In a perfect world, each drone would get 3d lidar and use a shared map, or we would use an exploration method more advanced than frontier exploration. See our final [presentation slide deck](https://docs.google.com/presentation/d/1PWhfTugKgx9f0reRl2K4_v7WLaGd90y1/edit?usp=sharing&ouid=115624224016993919786&rtpof=true&sd=true) or our [final document](https://docs.google.com/document/d/1u-xSLncPzKlJlmf7ioMSbY1enhuWiMwWg3c17DYGGAo/edit?usp=sharing) for details. If those links are broken, see the powerpoint and pdf files included in this github.

BB8 is hiding behind a car and mailbox up the road from where the drones spawn in. In our final recorded run, the swarm found them in 2:39. You can see that [video here.](https://www.youtube.com/watch?v=FG9_wvGdJ7g&ab_channel=sounderdiscISW)

## Branches of the Github

Main the branch where we did our final recorded timed search for BB8. feature/3dLidarSLAM has our failed attempt to run 3d lidar on all the drones, but none of our computers were beefy enough to run more than two drones at a time. feature/onRails is our unfinished work on sending each drone on a preset flight path instead of doing anything intelligent in searching or exploration. This branch is included because some files provide another example on how to work with multiple topics and move drones around in the simulation.

## Team Members

James Murphy (Project Lead, Computer Vision & YOLO Object Detection)
Matthew Hubbs (Gazebo & Simulation, Computer Vision & YOLO Object Detection)
Bobby Pappas (Computer Vision & YOLO Object Detection)
Andrew Borg (Pathfinding & Mapping, Swarm Algorithms)
Sebastian Almeida (Swarm Algorithms, Pathfinding & Mapping)
