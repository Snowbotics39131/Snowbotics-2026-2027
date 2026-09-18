#2 from red line
# at black line
# facing right
from PortMap2026 import *
drivebase.settings(straight_speed=300)
#drivebase.straight(605)
drivebase.arc(-1650, distance=650)
drivebase.turn(25)
drivebase.straight(-650)
