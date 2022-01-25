# Written by Auguste Brown
# Write.py is run on RPi to actuate servos

import time
import json
from math import pi
from PCA9685 import *

def mapAngle(desired_angle, theta1, theta2, dc1, dc2):
    slope = float(dc2 - dc1) / float(theta2 - theta1)
    delta_angle = desired_angle - theta1

    return delta_angle * slope + dc1

angles_file = open('AHB_angles.json')
motor_angles = json.load(angles_file)

# Actuate:
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)
m1_chan, m2_chan, m3_chan, m4_chan = 15, 0, 1, 2


for position in motor_angles:
    m1_ang, m2_ang, m3_ang = position[1]*180/pi, position[2]*180/pi, position[4]*180/pi
    m4_ang = -90 - m2_ang - m3_ang # set motor4 position so it is always facing pen straight down

    pwm.setServoPulse(m1_chan, mapAngle(m1_ang, 0, 90, 1280, 2150))
    pwm.setServoPulse(m2_chan, mapAngle(m2_ang, 0, 90, 670, 1450))
    pwm.setServoPulse(m3_chan, mapAngle(m3_ang, 0, -90, 560, 1550))
    pwm.setServoPulse(m4_chan, mapAngle(m4_ang, 0, -90, 600, 1480))
    time.sleep(0.04)

