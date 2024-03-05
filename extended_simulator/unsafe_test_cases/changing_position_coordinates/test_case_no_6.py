from deck import dosing_device, vial, thermoshaker, arm, hotplate
from workflow_utils_sim import setup_thermoshaker, locations, arm_home_position, arm_sleep_position, arm_pick_up_object, arm_place_object, start_stirring_soln, stop_stirring_soln, start_tempering_soln, stop_tempering_soln
from hein_robots.universal_robots.ur3 import UR3Arm
from hein_robots.robotics import Location, Orientation


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
    arm_place_object(arm, dosing_device_location, vial)
    arm_home_position(arm)

    ## Scenario: robot arm height reduced beyond platform value.
    random_location = [271.6, -127.9, 12.0, 178.6, 1.437, -88.08]
    arm.move_to_location(Location(x=random_location[0], y=random_location[1], z=random_location[2], rx=random_location[3], ry=random_location[4], rz=random_location[5]))
    
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


