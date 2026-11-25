#(17, 1.25) facing right
from QuadBotPortMap import *
drivebase.straight(570)
drivebase.arc(-55, 60)
drivebase.settings(turn_rate=600, turn_acceleration=1500)
drivebase.turn(-20)
drivebase.turn(30)
drivebase.turn(-30)
drivebase.settings(straight_speed=500, straight_acceleration=1000, turn_rate=360, turn_acceleration=1000)
drivebase.arc(-25, -80)
drivebase.straight(-800)