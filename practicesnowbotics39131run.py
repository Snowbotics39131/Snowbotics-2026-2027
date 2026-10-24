# two units from the red arc on the left base on the edge of the thick black line.
from QuadBotPortMap import *
drivebase.settings(straight_acceleration=1700, straight_speed=900)
drivebase.straight(300)
drivebase.turn(90)
drivebase.straight(1900)

# two units from the blue ark on thick line
drivebase.settings(straight_acceleration=1700, straight_speed=900)
drivebase.straight(300)
drivebase.turn(-90)
drivebase.straight(1900)
