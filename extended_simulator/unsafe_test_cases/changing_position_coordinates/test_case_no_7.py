from deck import dosing_device, vial, thermoshaker, arm, hotplate
from workflow_utils_sim import setup_thermoshaker, locations, arm_home_position, arm_sleep_position, arm_pick_up_object, arm_place_object, start_stirring_soln, stop_stirring_soln, start_tempering_soln, stop_tempering_soln
from hein_robots.universal_robots.ur3 import UR3Arm


if __name__ == '__main__':
 
    # Initilializing Locations
    grid_location = locations['grid']['NW']['arm']
    hotplate_location = locations['grid']['SE']['arm']
    thermoshaker_location = locations['thermoshaker']['arm']
    dosing_device_location = locations['dosing_device']['arm']


    # Start Workflow
    arm_sleep_position(arm)

    arm_home_position(arm)

    dosing_device.set_door("state", "open")
    vial.decap_vial()

    arm_pick_up_object(arm, grid_location,vial)

    ## Scenario: robot arm when holding the vial was placed inside the dosing device, the height of the robot
    ## arm’s location is reduced to be above the platform but with the vial extending beyond it
    ## (refer to locations["dosing_device"]["arm"]["pickup"] in workflow_utils_test_case_no_13.py)
    arm_place_object(arm, dosing_device_location, vial)
    arm_home_position(arm)
    
    dosing_device.set_door("state", "closed")
    dosing_device.run_action(delay=3, quantity=5)
    dosing_device.stop_action(delay=0)
    dosing_device.set_door("state", "open")

    arm_pick_up_object(arm, dosing_device_location, vial)
    arm_place_object(arm, thermoshaker_location, vial)
    dosing_device.set_door("state", "closed")
    arm_home_position(arm)

    start_tempering_soln(thermoshaker, vial, 50, 2)
    stop_tempering_soln(thermoshaker)
    arm_pick_up_object(arm, thermoshaker_location, vial)
    arm_place_object(arm, grid_location, vial)
    arm_home_position(arm)


    arm_pick_up_object(arm, grid_location,vial)
    arm_place_object(arm, hotplate_location, vial)
    arm_home_position(arm)
    start_stirring_soln(hotplate, 200, 1)
    stop_stirring_soln(hotplate, 100, 1)
    arm_pick_up_object(arm, hotplate_location,vial)
    arm_place_object(arm, grid_location, vial)
    

    # Disconnect devices
    arm_home_position(arm)
    arm_sleep_position(arm)
    arm.close()


