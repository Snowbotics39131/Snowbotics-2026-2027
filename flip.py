#3 from red line; on black line
from QuadBotPortMap import *
drivebase.straight(500)
drivebase.turn(90)
drivebase.straight(-80)
motorLeft.dc(-100)
motorRight.dc(100)
wait(8000)