from dummy import SimulatedSmartDevice, Vial
from workflow_utils import setup_thermoshaker, viperx_pick_up_object, viperx_place_object, ned2_pick_up_object, ned2_place_object, start_stirring_soln, start_tempering_soln, stop_stirring_soln, stop_tempering_soln, disconnect_devices, locations
from deck import thermoshaker, dosing_device, vial, viperx, ned2, hotplate


# Set vial locations
ned2_grid = locations["grid"]["NW"]["ned2"]
ned2_hotplate = locations["grid"]["SE"]["ned2"]
ned2_dosing_device = locations["dosing_device"]["ned2"]

def run_ned2(ned2):
    ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])
    
    # First Time
    dosing_device.set_door("state", "open")
    ned2_pick_up_object(ned2, ned2_hotplate, vial)
    ned2_place_object(ned2, ned2_dosing_device, vial)
    ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])

    dosing_device.set_door("state", "closed")
    dosing_device.run_action(delay=3, quantity=5)
    dosing_device.stop_action(delay=0)
    dosing_device.set_door("state", "open")
    
    
    ned2_pick_up_object(ned2, ned2_dosing_device, vial)
    ned2_place_object(ned2, ned2_hotplate, vial)
    ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])
    start_stirring_soln(hotplate, 200, 1)
    stop_stirring_soln(hotplate, 100, 1)

    # Second Time
    dosing_device.set_door("state", "open")

    ned2_pick_up_object(ned2, ned2_hotplate, vial) 
    ned2_place_object(ned2, ned2_dosing_device, vial)
    ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])

    dosing_device.set_door("state", "closed")
    dosing_device.run_action(delay=3, quantity=5)
    dosing_device.stop_action(delay=0)
    dosing_device.set_door("state", "open")
    
    
    ned2_pick_up_object(ned2, ned2_dosing_device, vial)
    ned2_place_object(ned2, ned2_hotplate, vial)
    ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])
    start_stirring_soln(hotplate, 200, 1)
    stop_stirring_soln(hotplate, 100, 1)


if __name__ == '__main__':
    run_ned2(ned2)

    disconnect_devices(hp=False, viperx=False, ned2=ned2)