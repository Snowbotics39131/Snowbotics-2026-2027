from PortMapUltimate import *

for _ in range(4):
    drivebase.straight(200)
    drivebase.arc(100, -90)

drivebase.settings(straight_speed=600)
drivebase.arc(100, -360)

drivebase.straight(100)
drivebase.turn(100)
drivebase.straight(190)
drivebase.straight(-190)
drivebase.turn(-100)
drivebase.straight(-100)
drivebase.arc(100, 360)
drivebase.arc(100, -360)
