#ALL THE RUN NUMBERS BELOW ARE INCORRECT:
#For up to 200 points, run 1, then 2, then 3:
#1. Right map run: with the many-purposRight map run: with the many-purposed attachment, pointed forward in right home, back right corner at (-8, 4) from the corner of the launch areaed attachment, pointed forward in right home, back right corner at (-8, 4) from the corner of the launch area
#2. Map_CollinAttachment: In the left base facing right fifteen sqaures up  and on the thick black line
#3. Drone: Pointed right in left home, front right corner of robot at (17, 0)
#4. vine_and_reaching_roots: In the left base facing backwards one sqaure to the right on the thick black line
from pybricks.hubs import InventorHub
from pybricks.tools import *
from gobetweenhomes import *
hub = InventorHub()
selection = hub_menu(1, 2, 3, 4, 'R', 'L', '*')
if selection == 1:
    import rightmaprun
elif selection == 2:
    import Map_CollinAttachent
elif selection == 3:
    import drone
elif selection == 4:
    import vine_and_reaching_roots
elif selection == 'R':
    #This starts in the right home and goes to the left.
    homebase(-90)
elif selection == 'L':
    #This starts in the right home and goes to the left.
    homebase(90)
elif selection == '*':
    import Presentation_2026
    #This is for the robot presentation
else:
    print('Pigs fly. (Unreachable code reached.)')
    for _ in range(3):
        hub.speaker.beep()
