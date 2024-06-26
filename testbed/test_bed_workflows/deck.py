# add username here
username = ""
import sys
from ika.thermoshaker import Thermoshaker
from ika.magnetic_stirrer import MockMagneticStirrer
sys.path.append(
    '/home/{}/interbotix_ws/src/interbotix_ros_toolboxes/interbotix_ws_toolbox/interbotix_ws_modules/src/interbotix_xs_modules'.format(username))
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from dummy import SimulatedSmartDevice, Vial
from pyniryo import tcp_client
from workflow_utils import setup_thermoshaker, viperx_pick_up_object, viperx_place_object, start_shaking_soln, stop_shaking_soln, disconnect_devices, locations, get_viperx_gripper_state


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

# ViperX
global viperx
viperx = InterbotixManipulatorXS("vx300s", "arm", "gripper")
viperx.arm.go_to_sleep_pose()

# Ned2
ned2_ip = "169.254.200.200"
global ned2
ned2 = tcp_client.NiryoRobot(ned2_ip)
ned2.calibrate_auto()
ned2.update_tool()
ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])