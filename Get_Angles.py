# Written by Auguste Brown
# Get_Angles.py solves for inverse kinematics of target points and exports motor angles

import numpy as np
import ikpy.utils.plot as plot_utils
import matplotlib.pyplot as plt
from Curves import *
from Arm import *

curves = getCurves('AHB.json', 10, -4.5) # specify coordinates file you want to generate curves for

motor_angles = [[0.0, -0.1471976441450741, 0.8169028730345268, 0.0, -2.7110679613488156, 0.0, 0.0, 0.0]] # Placeholder angles to help inverse kinematics solver
lift_height = 2 # cm off page

for i, curve in enumerate(curves):
    x0 = curve[0][0]
    y0 = curve[0][1]

    if i % 2 == 1: # if curve number is odd, pen is down
        for h in np.linspace(pen_length + lift_height, pen_length, lift_height*5): # move pen down
            prev_angles = motor_angles[len(motor_angles) - 1]
            target_pos = [x0, y0, h]
            motor_angles.append(arm.inverse_kinematics(target_position=target_pos, initial_position=prev_angles))
        
        height = pen_length
    else:
        for h in np.linspace(pen_length, pen_length + lift_height, lift_height*5): # pick pen up
            prev_angles = motor_angles[len(motor_angles) - 1]
            target_pos = [x0, y0, h]
            motor_angles.append(arm.inverse_kinematics(target_position=target_pos, initial_position=prev_angles))

        height = pen_length + lift_height # lift pen off page
    
    for point in curve: # draw curve
        prev_angles = motor_angles[len(motor_angles) - 1]

        target_pos = [point[0], point[1], height]
        motor_angles.append(arm.inverse_kinematics(target_position=target_pos, initial_position=prev_angles))

motor_angles.pop(0) # Remove placeholder angles

motor_angles = [angles.tolist() for angles in motor_angles] # compile all curves into one list

with open('AHB_angles.json', 'w') as f: # write to json file to export to RPi
    json.dump(motor_angles, f)

