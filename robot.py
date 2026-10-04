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