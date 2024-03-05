from hein_robots.robotics import Location, Orientation
from hein_robots.universal_robots.ur3 import UR3Arm

from ika.thermoshaker import Thermoshaker
from ika.magnetic_stirrer import MockMagneticStirrer
from dummy import SimulatedSmartDevice, Vial
from workflow_utils_sim import setup_thermoshaker


## Initialize devices

# Thermoshaker
kwargs = {
            'port': 'COM8',
            'dummy': True,
        }
global thermoshaker
thermoshaker = Thermoshaker.create(**kwargs)
setup_thermoshaker(thermoshaker, 15.5, 30, 30)
    
# Dosing Device
dosing_device = SimulatedSmartDevice("Virtual Dosing Station", {"plane": "N","state": "closed","move_time": 1},"dosing a vial")
 
# Vial
vial = Vial(10, 20)

# Hotplate
global hotplate
port = 'COM5'
hotplate = MockMagneticStirrer(device_port=port)

# UR3Arm
global arm
## Change your IP address
ip = ""
arm = UR3Arm(ip,gripper_base_port=30002)