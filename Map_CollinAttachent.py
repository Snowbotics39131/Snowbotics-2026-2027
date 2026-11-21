from QuadBotPortMap import*

drivebase.straight(100)
drivebase.turn(-90)
drivebase.straight(45)
drivebase.turn(90)
drivebase.straight(760)
drivebase.turn(65)
drivebase.straight(-70)
drivebase.straight(55)
drivebase.turn(25)
hub.speaker.beep()
drivebase.straight(-70)
drivebase.settings(straight_speed=50,turn_acceleration=500)
drivebase.turn(73)
hub.speaker.beep()
drivebase.straight(-160)
drivebase.settings(straight_speed=200)
drivebase.straight(180)
drivebase.turn(80)
drivebase.straight(280)
drivebase.turn(-60)
drivebase.straight(-100)
drivebase.arc(140, 45) # :)
drivebase.arc(-140, -90)#:)
drivebase.straight(-500)
drivebase.turn(45)
drivebase.straight(-500)
hub.speaker.play_notes([
    "C4/4", "C4/4", "G4/4", "G4/4",
    "A4/4", "A4/4", "G4/2",
    "F4/4", "F4/4", "E4/4", "E4/4",
    "D4/4", "D4/4", "C4/2",
])