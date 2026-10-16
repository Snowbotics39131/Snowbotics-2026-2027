from QuadBotPortMap import *
'''def forward_and_right(angle):
    drivebase.straight(100)
    drivebase.turn(angle)
    drivebase.straight(100)
forward_and_right(90)
forward_and_right(-90)'''

def homebase(angle):
    drivebase.settings(straight_acceleration=1700, straight_speed=900)
    drivebase.straight(300)
    drivebase.turn(angle)
    drivebase.straight(1900)
