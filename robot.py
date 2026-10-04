#For up to 200 points, run 1, then 2, then 3:
#1. Drone: pointed right in left home, front right corner of robot at (17, 0)
#2. Garden skylight: with the bar on the front, pointed forward in left home, back left corner at (8, 1)
#   This run starts in the left red home and end in the right blue home.
#3. Right map run: with the many-purposed attachment, pointed forward in right home, back right corner at (-8, 5) from the corner of the launch area
#
#4 is an alternative to 2 that just goes from the left home to the right without doing any missions.
#You may consider using it if you're low on time or you don't have a bar for the front of the robot.
from pybricks.hubs import InventorHub
from pybricks.tools import *
hub = InventorHub()
selection = hub_menu(1, 2, 3, 4)
if selection == 1:
    import drone
elif selection == 2:
    import gardenskylight
elif selection == 3:
    import rightmaprun
elif selection == 4:
    import practicesnowbotics39131run
else:
    print('The sky is falling.')
    hub.speaker.beep()