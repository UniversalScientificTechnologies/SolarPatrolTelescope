# Control system of the solar patrol telescope

![063A8564](https://user-images.githubusercontent.com/5196729/137354598-276ea1cb-fd52-44a2-a261-055f154d87cf.jpg)

The control system was developed during the modernization of the solar patrol telescope of [Astronomical Institute of CAS](http://www.asu.cas.cz/en/about/about-the-institute). The aim of the Solar patrol is to provide daily observation of the sun serving many (not only) scientifics purposes.

The observatory is equipped with several telescopes (refractors):

 * 210/3430, details
 * 205/2801, details
 * 150/750, Full disc, Wl, Pointing telescope
 * 150/750, Full disc, Ha
 * 63/840, For drawing

![20210827_095833](https://user-images.githubusercontent.com/5196729/137342953-5a7304ff-793c-4e57-895f-c33158f182ff.jpg)

[UST](ust.cz) company has modernized the control system of Partrola's telescope system. The aim of this upgrade was for the telescope to by able to perform all-day solar observations with a minimal need for interventions by observer and to produce high-quality images and solar drawings.


## Technical details
Control and power electronics is based on the MLAB kit. System is controlled by Odroid C2 one-board computer. The software is built on the framework ROS and AROM, which allow easy expansion with new features. 


## Control interface

### Remote control
The system is primarily controlled via web interface. The advantage is that the system is independent of the operator's computer and it is also platform independent. 
![obrazek](https://user-images.githubusercontent.com/5196729/137350272-df36ca79-79c8-41cf-a33f-86da230990f5.png)

### Local control
The telescope is equipped with a local (wired) controller, which allows basic tasks such as moving the mount, opening and closing the caps/shutters or focusing the telescopes. 

### Controlled elements
 * Mount
   * Ra/Dec axis
   * Time axis
 * Telesope dust caps
 * Automatic dome control
 * Telescope control
   * Focuser
   * Iris shutter
 * Pointing
   * Sun detection in image
   * Detection of solar axis
   * Mount control
 * Variable power source
   * Multiple outputs

<hr>

_Equipment for solar detection is in [own branch](https://github.com/UniversalScientificTechnologies/SolarPatrolTelescope/tree/ControlSystem)._





### I2C Device addresses

0x2C - I2CSPI - DECmotor \
0x28 - I2CSPI - RAmotor \
0x2D - I2CSPI - TimeMachine \
0x2E - I2CSPI - CLARK + ZEISS
