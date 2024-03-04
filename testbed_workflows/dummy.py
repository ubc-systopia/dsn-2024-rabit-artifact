import time 

class DummyDevice:
    ### @param name - str
    ### @param door - dict with keys 'plane' (one of ['North', 'South', 'East', 'West', 'Top', 'Bottom']), 'state' ('open'|'closed') and 'move_time' (number)
    def __init__(self, name, door):
        self._name = name
        self._door = door
        print(f"Initialized {name}.")

    @property
    def name(self):
        return self._name

    @property
    def door(self):
        return self._door
    
    @property
    def door_state(self):
        print('DOOOOR: ', self._door['state'])
        return self._door['state']

    ### Setters
    @name.setter
    def set_name(self, new_name):
        self._name = new_name

    @door.setter
    def door(self, plane, state, delay):
        self._door = {
            'plane': plane, 
            'state': state,
            'move_time': delay,
        }
    
    ### @brief if door exists, set its state
    def set_door(self, attr, val):
        if type(self._door) is dict:
            self._door[attr] = val
            # if attr == "state":
            #     time.sleep(self.get_door()['delay'])
        else:
            print("Cannot change attribute: create a door first.")


class SimulatedSmartDevice(DummyDevice):
    ### @param action - str
    def __init__(self, name, door, action):
        super().__init__(name, door)
        self._action = action
        self._active = False
        print("Initialized SimulatedSmartDevice.")

    ### @brief returns whether action ran successfully after opening the door
    def run_action(self, delay, **kwargs) -> bool: 
        if self._active is False:
            print(f"Running action {self._action}...")
            self._active = True
            time.sleep(delay)
        else:
            print(f"Error: cannot run action {self._action}, action already running.")
            return False

    ### @brief returns whether action stopped successfully after closing the door
    def stop_action(self, delay):
        if self._active is True:
            print(f"Stopping action {self._action}.")
            self._active = False
            time.sleep(delay)
            return True
        else:
            print(f"Error: cannot stop action {self._action}, action is not running.")
            return False

    @property
    def action(self):
        return self._action
    
    @property
    def active(self):
        return self._active

    ### Setters
    @action.setter
    def set_action(self, new_action):
        self._action = new_action


class Vial():
    ### @param volume - number (mL)
    ### @param temp - number (Celsius)
    ### @attr cap - bool
    # TODO: should we add attributes safe_vol, curr_vol, curr_substance, clean, etc.?
    def __init__(self, max_vol, temp):
        self._max_vol = max_vol
        self._temp = temp
        self._cap = False
        print("Initialized Vial.")

    def cap_vial(self):
        self._cap = True

    def decap_vial(self):
        self._cap = False

    # TODO: should max_vol have a setter?
    @property
    def max_vol(self):
        return self._max_vol

    @property
    def temp(self):
        return self._temp
    
    @property
    def cap(self):
        return self._cap

    ### Setters
    @temp.setter
    def change_temp(self, temp):
        self._temp = temp

    @cap.setter
    def cap(self, cap):
        self._cap = cap