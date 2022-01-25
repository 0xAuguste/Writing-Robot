# Written by Auguste Brown
# Curves.py is a helper function to turn the intials coords into coordinates suitable for the IK solver

# This function  finds locations where the pen should lift off the paper, scales the letters, shifts them
# to an appropriate location, and rotates them into the correct frame

import json
import numpy as np

def getCurves(filename, x0=0, y0=0):
	coordinate_file = open(filename)
	coords_raw = json.load(coordinate_file)

	# Manipulate coordinates into correct scale
	scale = 40
	x_min = min([c[0] for c in coords_raw])
	y_init = coords_raw[0][1]
	# Scale the coords, shift them to zero location, perform coordinate rotation to align with robot frame:
	coords = [[(c[1] - y_init)/scale + x0, (c[0] - x_min)/scale + y0] for c in coords_raw]

	# Find pen lift locations
	dist_thresh = 1 # cm

	rest = [4, 0] # resting point which the robot starts from and returns to
	dist = np.linalg.norm(np.array(rest)-np.array(coords[0]))
	curves = [np.linspace(rest, coords[0], int(dist*5)).tolist(), []] # initialize with path to starting point
	curve_num = 1

	for i in range(len(coords) - 1):
	    current = np.array(coords[i])
	    target = np.array(coords[i + 1])

	    curves[curve_num].append(coords[i]) # add point to current curve

	    dist = np.linalg.norm(target-current)
	    if (dist > dist_thresh): # distance between points is greater than threshold
	        line = np.linspace(current, target, int(dist*5)).tolist() # create line joining 2 points (where pen will be raised)
	        curves.append(line) # add pen lift line to new curve
	        curves.append([]) # start a new curve for drawing
	        curve_num += 2

	dist = np.linalg.norm(np.array(rest)-np.array(coords[0]))
	curves.append(np.linspace(coords[-1], rest, int(dist*5)).tolist()) # add coords for robot to return to rest

	return curves