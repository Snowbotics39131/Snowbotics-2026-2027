#This is a test of drivebase precision based on a Hilbert curve.
#The robot should end up in the same place it started in the same orientation.
#Make sure you control for the following things:
#- Everything in drivebase.settings()
#  - Speed and acceleration, both linear and angular
#- Gyroscope or lack thereof
#- No attachment
#- Battery voltage
#Some things it might also be nice to control for, but it's not as critical:
#- Wheels being clean
#- Table:
#  - Flat (as in angle - measure with a level)
#  - Not bumpy (check for sand, crumbs, small pieces, etc. under the mat)
#  - Proper material (preferably FLL mat - smooth and with a little friction)
#  - Clean
#- Which hub you're using (the IMUs can slightly differ sometimes)
#- Which motors you're using (older motors sometimes aren't as precise)
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

#Reverse which code is commented and uncommented if you don't want to test arcs.
#drivebase.straight(100)
#drivebase.turn(90)
#drivebase.straight(100)
#drivebase.turn(90)
drivebase.straight(100, then=Stop.NONE)
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
drivebase.straight(-300)
