#!/bin/sh
apt-get update
apt-get install git
curl -sSL http://get.gazebosim.org | sh
git clone https://github.com/patrick1bauer/autonomous_search_with_ai.git
git clone https://github.com/chaolmu/gazebo_models_worlds_collection.git
echo "export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:<path to this repo>/worlds" >> ~/.bashrc
source ~/.bashrc
cp ./autonomous_search_with_ai/worlds/urban.world /usr/share/gazebo-11/worlds
