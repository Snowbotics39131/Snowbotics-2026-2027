#This is the newest revision of code for the right half of the field for the current robot.
#It pushes the and in, knocks the soil door thing down, and should drop the block in the trees.
#The first two of those are quite consistent; the third is untested.
#Alignment: the right corner of the robot, third thick line from the blue arc on the right home base fifth line up
from QuadBotPortMap import *
drivebase.straight(550)
drivebase.turn(-90)
drivebase.straight(450)
drivebase.turn(-45)
drivebase.straight(-150)
drivebase.settings(straight_speed=75)
drivebase.straight(-100)
drivebase.straight(120)
drivebase.turn(90)
drivebase.straight(-200)
drivebase.straight(150)
drivebase.settings(straight_speed=200)
drivebase.turn(135)
drivebase.straight(290)
drivebase.turn(-45)
drivebase.straight(200)