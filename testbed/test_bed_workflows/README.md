# Running Testbed Workflows

## Information Regarding Testbed Workflows and Device Commands
* [Testbed Workflow Steps and List of Device Commands](././docs/testbed_information.pdf)

## Helper python files
1) `dummy.py`: Defines the classes for the low-fidelity objects of the testbed.
2) `workflow_utils.py`: Defines helper functions for writing workflows.
3) `deck.py`: Initializes all devices in one file.

## Running Workflows

### Configuration
1) Download (`interbotix`)[https://github.com/Interbotix] and pass the file path of viperx repository in the `deck.py` file.
2) Install `pyniryo` python library using the following command line `pip install pyniryo`

### Dose, Shake, and Heat using One Robot
1) Run the command `python dose_shake_heat_one_robot.py`

### Dose, Shake, and Heat using Two Robots Sequentially
1)  Run the command `python dose_shake_heat_two_robots_sequential.py`

### Dose, Shake, and Heat using Two Simultaneously Moving Robots
1) Open two command terminals
2) Execute `python dose_shake_heat_two_robots_simulataneous_viperx.py` in one terminal and `python dose_shake_heat_two_robots_simulataneous_ned2.py` in the other terminal together.