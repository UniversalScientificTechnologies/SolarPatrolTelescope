# Control system of solar patrol telescope

The control system was developed during the modernization of the solar patrol telescope of [Astronomical Institute of CAS](http://www.asu.cas.cz/en/about/about-the-institute). The aim of Solar patrol is provide daily observation of the sun for many (not only) scientifics purposes. 

![20210827_095833](https://user-images.githubusercontent.com/5196729/137342953-5a7304ff-793c-4e57-895f-c33158f182ff.jpg)

Company [UST](ust.cz) has modernized control system of Partrola's telescope system. The aim of this upgrade was for the telescope to by able to perform all-day solar observations with minimal intervention by observer and to produce highly qualitative images and solar drawings.


## Technical details
Control and power electronics is based on the MLAB kit. System is controlled by Odroid C2 one-board computer. The software is built on the framework ROS and AROM, which allow easy expansion with new features. 


### Controlled elements
 * Mount
   * Ra/Dec axis
   * Time axis
 * Telesope dust caps
 * Automatic dome control
 * Telescope control
   * Focuser
   * Iris clone
 * Pointing
   * Sun detection in image
   * Detection of solar axis
   * Mount control

_Equipment for solar detection is in [own branch](https://github.com/UniversalScientificTechnologies/SolarPatrolTelescope/tree/ControlSystem)._





### I2C zařízení

0x2C - I2CSPI - DECmotor \
0x28 - I2CSPI - RAmotor \
0x2D - I2CSPI - TimeMachine \
0x2E - I2CSPI - CLARK + ZEISS
