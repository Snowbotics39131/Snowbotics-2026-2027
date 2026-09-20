try:
    from PortMap2026 import *
    print("2026 robot detected")
except OSError:
    from QuadBotPortMap import *
    print("quad bot detected")
