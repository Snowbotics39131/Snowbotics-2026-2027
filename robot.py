#ALL THE RUN NUMBERS BELOW ARE INCORRECT:
#For up to 200 points, run 1, then 2, then 3:
#1. Drone: pointed right in left home, front right corner of robot at (17, 0)
#2. Garden skylight: with the bar on the front, pointed forward in left home, back left corner at (8, 1)
#   This run starts in the left red home and end in the right blue home.
#3. Right map run: with the many-purposed attachment, pointed forward in right home, back right corner at (-8, 4) from the corner of the launch area
#5. In red facing right (0, 15)
#6. located on the left base on the thick line one square away from the red arc
#7. 3rd black line from red and on the thick horizontal black line
#4 is an alternative to 2 that just goes from the left home to the right without doing any missions.
#You may consider using it if you're low on time or you don't have a bar for the front of the robot.
from pybricks.hubs import InventorHub
from pybricks.tools import *
from gobetweenhomes import *
hub = InventorHub()
selection = hub_menu(1, 2, 3, 4, 5, 'R', 'L')
if selection == 1:
    import rightmaprun
elif selection == 2:
    import Map_CollinAttachent
elif selection == 3:
    import drone
elif selection == 4:
    import seedexplosion
elif selection == 5:
    import vine_and_reaching_roots
elif selection == 'R':
    #This starts in the right home and goes to the left.
    homebase(-90)
elif selection == 'L':
    #This starts in the right home and goes to the left.
    homebase(90)
else:
    print('The sky is falling.')
    hub.speaker.beep()
