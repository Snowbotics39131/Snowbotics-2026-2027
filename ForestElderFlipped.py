from QuadBotPortMap import *

motorShift.run_until_stalled(400,duty_limit=30)
motorShift.run_angle(300,-1320)
drivebase.settings(straight_acceleration=300)
drivebase.straight(-62)#+
drivebase.turn(6)
motorShift.run_angle(300,300)
motorShift.run_angle(800,-60)
#motorAttachment.run_angle(300,300)
drivebase.straight(100)
motorShift.run_angle(800,-240)
drivebase.turn(-6)
motorShift.run_angle(800,-120)
drivebase.straight(100)
motorShift.run_angle(800,-20)
motorShift.run_angle(800,1000)