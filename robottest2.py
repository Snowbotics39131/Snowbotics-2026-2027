from PortMapUltimate import *
#tests robot turns
def test(speed):
    drivebase.settings(straight_speed=speed)
    drivebase.straight(100)
    drivebase.turn(90)
    drivebase.straight(50)
    drivebase.straight(-50)
    drivebase.turn(-90)
    drivebase.straight(-100)
    drivebase.turn(360)
    drivebase.turn(-360)
    for _ in range(3):
        drivebase.straight(50)
        drivebase.turn(270)
        drivebase.turn(-270)
        drivebase.straight(-50)
test(195)
wait(5000)
test(100)
wait(5000)
test(400)