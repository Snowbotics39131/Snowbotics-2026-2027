from QuadBotPortMap import *
# this does simple code to show the judges for robot design

for i in range(4):
    drivebase.straight(100)
    drivebase.turn(90)
    print(i)
drivebase.arc(150, 360)
motorAttachment.run_angle(90, 75)
hub.speaker.beep()