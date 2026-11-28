from QuadBotPortMap import*

#1,5 from the left side, bottom left corner
drivebase.straight(-200)
drivebase.settings(straight_speed=190)
drivebase.straight(-200)
#pushes the rock
drivebase.settings(straight_speed=300)
'''drivebase.straight(50)
drivebase.straight(-100)'''
drivebase.straight(250)
drivebase.turn(180)
drive_until_stalled(-300)
#goes home
drivebase.straight(200)
drivebase.turn(50)
motorAttachment.run_until_stalled(200, duty_limit=100)
drivebase.straight(610)
drivebase.turn(-50)
#
drivebase.settings(60)
drivebase.straight(-25)
drivebase.turn(3.5)
#motorAttachment.run_angle(100,-160)
drivebase.straight(90)
wait(1000)
motorAttachment.run_until_stalled(-300, duty_limit=100)
drivebase.straight(-90)
drivebase.turn(20)
motorAttachment.run_until_stalled(-150, duty_limit=100)
drivebase.straight(-20)
drivebase.turn(-20.5)
drivebase.settings(300)
#
drive_until_stalled(275.1)
#does the tree
drivebase.settings(100)
drivebase.straight(-100)
drivebase.straight(30)
drivebase.straight(-50)
drivebase.turn(-90)
drivebase.straight(145)

drivebase.turn(75)
motorAttachment.run_until_stalled(150, duty_limit=100)
drivebase.turn(10)
drivebase.straight(-50)