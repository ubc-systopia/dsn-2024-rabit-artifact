from dummy import SimulatedSmartDevice, Vial
from workflow_utils import setup_thermoshaker, viperx_pick_up_object, viperx_place_object, ned2_pick_up_object, ned2_place_object, start_stirring_soln, start_tempering_soln, stop_stirring_soln, stop_tempering_soln, disconnect_devices, locations
from deck import thermoshaker, dosing_device, vial, viperx, ned2, hotplate

if __name__ == '__main__':

    # Set vial locations
    ned2_grid = locations["grid"]["NW"]["ned2"]
    ned2_hotplate = locations["grid"]["SE"]["ned2"]
    viperx_grid = locations["grid"]["NW"]["viperx"]
    viperx_dosing_device = locations["dosing_device"]["viperx"]
    viperx_thermoshaker = locations["thermoshaker"]["viperx"]

    # Start workflow
    dosing_device.set_door("state", "open")
    vial.decap_vial()

    viperx.arm.go_to_home_pose()

    ## Scenario: viperx’s location changed to the location of the ned2’s sleep pose.
    random_location = [0.5, 0.4, 0.2]
    viperx.arm.set_ee_pose_components(x=random_location[0], y=random_location[1], z=random_location[2])

    viperx_pick_up_object(viperx, viperx_grid, vial)
    viperx_place_object(viperx, viperx_dosing_device, vial)
   
    viperx.arm.go_to_home_pose()
    
    dosing_device.set_door("state", "closed")
    dosing_device.run_action(delay=3, quantity=5)
    dosing_device.stop_action(delay=0)
    dosing_device.set_door("state", "open")

    viperx_pick_up_object(viperx, viperx_dosing_device, vial)
    viperx_place_object(viperx, viperx_thermoshaker, vial)
    dosing_device.set_door("state", "closed")
    viperx.arm.go_to_home_pose()

    start_tempering_soln(thermoshaker, vial, 50, 2)
    stop_tempering_soln(thermoshaker)

    viperx_pick_up_object(viperx, viperx_thermoshaker, vial)
    viperx_place_object(viperx, viperx_grid, vial)
    viperx.arm.go_to_home_pose()
    viperx.arm.go_to_sleep_pose()

    ned2_pick_up_object(ned2, ned2_grid, vial)
    ned2_place_object(ned2, ned2_hotplate, vial)
    ned2.move_pose([0.1342,0.0000, 0.1650,-0.003, 1.001, 0.000])
    start_stirring_soln(hotplate, 200, 1)
    stop_stirring_soln(hotplate, 100, 1)
    ned2_pick_up_object(ned2, ned2_hotplate, vial)
    ned2_place_object(ned2, ned2_grid, vial)
    vial.cap_vial()
    
    disconnect_devices(hp=False, viperx=viperx, ned2=ned2)
  