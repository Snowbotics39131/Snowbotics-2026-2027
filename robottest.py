#This is a test of drivebase precision based on a Hilbert curve.
#The robot should end up 300mm forward from where it started and should not have changed position horizontally.
#Make sure to control for battery voltage and speed.
from PortMapUltimate import *
drivebase.straight(100)
drivebase.turn(90)
drivebase.straight(100)
drivebase.turn(90)
drivebase.straight(100)
drivebase.turn(-90)
drivebase.straight(200)
drivebase.turn(-90)
drivebase.straight(100)
drivebase.turn(-90)
drivebase.straight(100, then=Stop.NONE)

#Reverse which code is commented and uncommented if you don't want to test arcs.
#drivebase.turn(90)
#drivebase.straight(100)
#drivebase.turn(90)
drivebase.arc(50, 180, then=Stop.NONE)

#drivebase.straight(100)
#drivebase.turn(-90)
#drivebase.straight(100)
#drivebase.turn(-90)
#drivebase.straight(200)
drivebase.arc(-50, 180, then=Stop.NONE)
drivebase.straight(100)

drivebase.turn(-90)
drivebase.straight(100)
drivebase.turn(90)
drivebase.straight(100)
drivebase.turn(90)
drivebase.straight(100)