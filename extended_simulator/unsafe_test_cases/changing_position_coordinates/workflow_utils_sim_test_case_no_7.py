import json
import time
import sys
import numpy as np
from ika.thermoshaker import Thermoshaker
from ika.magnetic_stirrer import MockMagneticStirrer
from dummy import SimulatedSmartDevice, Vial

from hein_robots.robotics import Location, Orientation
from hein_robots.universal_robots.ur3 import UR3Arm



locations = {
    "grid": {
        "NW": {
            "meta": "original vial location",
            "arm": {
                "pickup_safe_height": [513, 8.322, 244, 178.6, 1.437, -88.08],
                "pickup": [513, 8.322, 130.0, 178.6, 1.437, -88.08]
            },
        },
        "SE": {
            "meta": "imaginary hotplate for now",
            "arm": {
                "pickup_safe_height": [513, 65.0, 244.1, 178.6, 1.437, -88.08],
                "pickup": [513, 65.0, 130.3, 178.6, 1.437, -88.08]
            }
        }
    },
    "dosing_device": {
        "arm": {                    
            "pickup_safe_height": [140.8, 458.5, 240, 178.6, 1.437, -88.08],
            ## Scenario: robot arm when holding the vial was placed inside the dosing device, the height of the robot
            ## arm’s location is reduced to be above the platform but with the vial extending beyond it
            # "pickup": [140.8, 458.5, 100, 178.6, 1.437, -88.08]
            "pickup" : [140.8, 458.5, 60, 178.6, 1.437, -88.08]
        }
    },
    "thermoshaker": {
        "arm": {
            "pickup_safe_height": [427.2, -234.2, 244.1, 178.6, 1.437, -88.08],
            "pickup": [427.2, -234.2, 130.0, 178.6, 1.437, -88.08]
        }
    }
}


### SETUP + TEARDOWN
def setup_thermoshaker(thermoshaker, safety_temp, wd_1, wd_2):
    thermoshaker.watchdog_safety_temperature = safety_temp
    thermoshaker.start_watchdog_mode_1(wd_1)
    thermoshaker.start_watchdog_mode_2(wd_2)
    thermoshaker.switch_to_normal_operation_mode()
    print("Completed setting up thermoshaker.")


### HOTPLATE
def start_stirring_soln(hotplate, start_stir_rate, delay):
    print("[HOTPLATE]: Starting to stir solution...")
    hotplate.start_stirring()
    hotplate.target_stir_rate = start_stir_rate
    time.sleep(delay)

def start_heating_soln(hotplate, vial, start_temp, delay):
    print("[HOTPLATE]: Starting to heat solution...")
    hotplate.target_temperature = start_temp
    hotplate.start_heating()
    time.sleep(delay)
    # vial.change_temp(start_temp)

def stop_stirring_soln(hotplate, end_stir_rate, delay):
    hotplate.target_stir_rate = end_stir_rate
    time.sleep(delay)
    hotplate.stop_stirring()
    print("[HOTPLATE]: Stopped stirring solution.")

def stop_heating_soln(hotplate, vial, end_temp, delay):
    hotplate.target_temperature = end_temp
    time.sleep(delay)
    hotplate.stop_heating()
    print("[HOTPLATE]: Stopped heating solution.")
    # vial.change_temp(end_temp)


### THERMOSHAKER
def start_shaking_soln(thermoshaker, speed, delay):
    thermoshaker.set_speed = speed
    print("[THERMOSHAKER]: Starting to shake solution...")
    thermoshaker.start_shaking()
    time.sleep(delay)

# TODO: debug change_temp
def start_tempering_soln(thermoshaker, vial, goal_temp, delay):
    thermoshaker.set_temperature = goal_temp
    print("[THERMOSHAKER]: Starting to temper solution...")
    thermoshaker.start_tempering()
    time.sleep(delay)

def stop_shaking_soln(thermoshaker):
    thermoshaker.stop_shaking()
    print("[THERMOSHAKER]: Stopped shaking solution.")

def stop_tempering_soln(thermoshaker):
    thermoshaker.stop_tempering()
    print("[THERMOSHAKER]: Stopped tempering solution.")


### UR3Arm
def convert_m_to_mm(pose):
    for i in range(0,3):
        pose[i] = pose[i] * 1000
    return pose

def arm_move(arm, pose, delay):
    arm.move_to_location(Location(x=pose[0], y=pose[1], z=pose[2], rx=pose[3], ry=pose[4], rz=pose[5]))
    time.sleep(delay)

def arm_sleep_position(arm):
    arm.move_to_location(Location(x=-136.9, y=-267.2, z=147.0, rx=178.6, ry=1.437, rz=-180.0))

def arm_home_position(arm):
    arm.move_to_location(Location(x=271.6, y=-127.9, z=147.0, rx=178.6, ry=1.437, rz=-88.08))

def arm_pick_up_object(arm, pose, obj):
    name = obj.__class__.__name__
    print(f"\n[UR3Arm]: Picking up {name}.")
    # arm.open_gripper(1)
    arm_move(arm, pose["pickup_safe_height"], 1)
    arm_move(arm, pose["pickup"], 1)
    # arm.close_gripper(1)
    arm_move(arm, pose["pickup_safe_height"], 0)

def arm_place_object(arm, pose, obj):
    name = obj.__class__.__name__
    print(f"[UR3Arm]: Placing {name}.\n")
    arm_move(arm, pose["pickup_safe_height"], 1)
    arm_move(arm, pose["pickup"], 1)
    # arm.open_gripper(1)
    arm_move(arm, pose["pickup_safe_height"], 0)