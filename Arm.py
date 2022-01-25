# Written by Auguste Brown
# Arm.py defines the robot arm model using our DH parameters

from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
from math import pi

motor_1_height = 6.8 # distance from ground to motor 1 shaft
d1 = 2.1 # vertical distance from motor 1 shaft to motor 2 shaft
a1 = 3.1 # horizontal distance from motor 1 shaft to arm 1 linkage
d2 = 1.24 # horizontal distance from arm 1 linkage to arm 2 linkage
d3 = 2.3 # horizontal distance from arm 2 linkage to pen
arm_1_length = 8.95
arm_2_length = 9.94
pen_length = 6.6

arm = Chain(name='Arm', active_links_mask=[False, True, True, False, True, False, True, False], links=[
    OriginLink(),
    URDFLink(
      name="Motor 1",
      origin_translation=[0, 0, motor_1_height], # The translation vector from the last joint to this joint
      origin_orientation=[0, 0, 0], # The rotation from the last joint to this joint
      rotation=[0, 0, 1], # The rotation axis of the link
      joint_type="revolute"
    ),
    URDFLink(
      name="Motor 2",
      origin_translation=[0, 0, d1],
      origin_orientation=[pi/2, 0, 0],
      rotation=[0, 0, 1],
      joint_type="revolute"
    ),
    URDFLink(
      name="Arm 1 Linkage",
      origin_translation=[0, 0, a1],
      origin_orientation=[0, 0, 0],
      rotation=[0, 0, 0],
      joint_type="revolute"
    ),
    URDFLink(
      name="Motor 3",
      origin_translation=[arm_1_length, 0, 0],
      origin_orientation=[0, 0, 0],
      rotation=[0, 0, 1],
      joint_type="revolute"
    ),
    URDFLink(
      name="Arm 2 Linkage",
      origin_translation=[0, 0, -d2],
      origin_orientation=[0, 0, 0],
      rotation=[0, 0, 0],
      joint_type="revolute"
    ),
    URDFLink(
      name="Motor 4",
      origin_translation=[arm_2_length, 0, 0],
      origin_orientation=[0, 0, 0],
      rotation=[0, 0, 1],
      joint_type="revolute"
    ),
    URDFLink(
      name="Pen Linkage",
      origin_translation=[0, 0, -d3],
      origin_orientation=[0, 0, 0],
      rotation=[0, 0, 0],
      joint_type="revolute"
    )
])