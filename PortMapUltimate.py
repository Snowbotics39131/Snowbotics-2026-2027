try:
    from PortMap2026 import *
    print("2026 robot detected")
except OSError:
    from QuadBotPortMap import *
    print("quad bot detected")
except ModuleNotFoundError:
    # The pybricks module doesn't exist in CPython.
    from fakeportmap import *
    print("simulated turtle robot detected")
