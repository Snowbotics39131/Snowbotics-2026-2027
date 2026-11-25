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
hub.speaker.beep()
drive_until_stalled(-300)
#goes home
drivebase.straight(200)
drivebase.turn(50)
drivebase.straight(575)
drivebase.turn(-50)
drive_until_stalled(375)
#does the tree
drivebase.settings(100)
drivebase.straight(-100)
drivebase.straight(30)
drivebase.straight(-50)
'''
drivebase.turn(90)
drivebase.straight(120)
drivebase.turn(-90)
drivebase.straight(-50)
drivebase.turn(45)
motorAttachment.run_angle(70,-140)
drivebase.turn(-45)
drivebase.straight(150)
drivebase.turn(25)
motorAttachment.run_angle(70,75)
drivebase.turn(10)
drivebase.straight(-25)
drivebase.straight(-50)
drivebase.straight(20)
drivebase.straight(-50)
drivebase.turn(90)
drivebase.straight(-300)
drivebase.turn(-90)
drivebase.straight(-20)
'''