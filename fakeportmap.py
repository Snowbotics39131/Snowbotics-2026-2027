from turtle import *
showturtle()
penup()
#shape('square')
teleport(0, -300)
speed(2)
left(90)
pendown()
class Stop:
    NONE = None
class DriveBase:
    def straight(self, mm, then=None):
        forward(mm)
    def turn(self, mm):
        right(mm)
    def arc(self, radius, angle=None, then=None):
        circle(-radius, angle)
    def settings(self, straight_speed=None, straight_acceleration=None, turn_rate=None, turn_acceleration=None):
        if straight_speed is not None:
            speed(straight_speed / 100)
drivebase = DriveBase()
