#!/bin/bash
source /opt/ros/kinetic/setup.bash
source /home/odroid/arom_ws/devel/setup.bash

rosrun arom pymlab_bridge /home/odroid/arom_ws/src/SolarPatrolTelescope/config/patrola.json
