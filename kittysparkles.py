#8, 0
from QuadBotPortMap import *
drivebase.straight(750)
drivebase.settings(straight_speed=100, turn_rate=45)
drivebase.turn(-68)
drivebase.straight(80)
drivebase.turn(-22)
drivebase.straight(200)
drivebase.arc(-90, 90)
motorLeft.dc(100)
motorRight.dc(100)
wait(3000)
#drivebase.settings(straight_speed=700, straight_acceleration=300)
#drivebase.straight(300)