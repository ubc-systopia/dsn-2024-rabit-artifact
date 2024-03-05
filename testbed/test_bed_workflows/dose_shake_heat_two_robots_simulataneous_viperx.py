from dummy import SimulatedSmartDevice, Vial
from workflow_utils import setup_thermoshaker, viperx_pick_up_object, viperx_place_object, ned2_pick_up_object, ned2_place_object, start_stirring_soln, start_tempering_soln, stop_stirring_soln, stop_tempering_soln, disconnect_devices, locations
from deck import thermoshaker, dosing_device, vial, viperx, ned2, hotplate

# Set vial locations
viperx_grid = locations["grid"]["NW"]["viperx"]
viperx_dosing_device = locations["dosing_device"]["viperx"]
viperx_thermoshaker = locations["thermoshaker"]["viperx"]


def run_viperx(viperx):
    viperx.arm.go_to_sleep_pose()

    # First Time
    viperx.arm.go_to_home_pose()
    viperx_pick_up_object(viperx, viperx_grid, vial)
    viperx_place_object(viperx, viperx_thermoshaker, vial)
    viperx.arm.go_to_home_pose()

    start_tempering_soln(thermoshaker, vial, 50, 2)
    stop_tempering_soln(thermoshaker)

    viperx_pick_up_object(viperx, viperx_thermoshaker, vial)
    viperx_place_object(viperx, viperx_grid, vial)
    viperx.arm.go_to_home_pose()

    # Second Time
    viperx.arm.go_to_home_pose()
    viperx_pick_up_object(viperx, viperx_grid, vial)
    viperx_place_object(viperx, viperx_thermoshaker, vial)
    viperx.arm.go_to_home_pose()

    start_tempering_soln(thermoshaker, vial, 50, 2)
    stop_tempering_soln(thermoshaker)

    viperx_pick_up_object(viperx, viperx_thermoshaker, vial)
    viperx_place_object(viperx, viperx_grid, vial)
    viperx.arm.go_to_home_pose()

    # Third Time
    viperx.arm.go_to_home_pose()
    viperx_pick_up_object(viperx, viperx_grid, vial)
    viperx_place_object(viperx, viperx_thermoshaker, vial)
    viperx.arm.go_to_home_pose()

    start_tempering_soln(thermoshaker, vial, 50, 2)
    stop_tempering_soln(thermoshaker)

    viperx_pick_up_object(viperx, viperx_thermoshaker, vial)
    viperx_place_object(viperx, viperx_grid, vial)
    viperx.arm.go_to_home_pose()


if __name__ == '__main__':
    run_viperx(viperx)

    disconnect_devices(hp=False, viperx=viperx, ned2=False)