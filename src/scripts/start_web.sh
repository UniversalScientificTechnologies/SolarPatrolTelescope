#!/bin/bash
source /opt/ros/kinetic/setup.bash
source /home/odroid/arom_ws/devel/setup.bash

cd /home/odroid/repos/arom-web_ui/src/aromweb/

roslaunch rosbridge_server rosbridge_websocket.launch &
python web.py
