from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *

hub = InventorHub()

motorRight = Motor(Port.A, Direction.CLOCKWISE)
motorLeft = Motor(Port.B, Direction.COUNTERCLOCKWISE)
moterback = Motor(Port.D, Direction.CLOCKWISE)
moterfront = Motor(Port.F, Direction.CLOCKWISE)
colorSensorLeft = ColorSensor(Port.C)
colorSensorRight = ColorSensor(Port.E)
drivebase = DriveBase(motorLeft,motorRight,56,96.5)

drivebase.use_gyro(True)

print(hub.battery.voltage())
#print(motorAttachment.control.pid())
#print(motorAttachment.control.target_tolerances())