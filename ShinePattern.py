from machine import Pin
import time

class ShinePattern:
    
    _SWITCH_PIN = 23
    _HOMING_PIN = 19
    _SWITCH_TIME_CONSTANT_MS = 60
    _PATTERNS = [
        "OFF",
        "ALL_SOLID",
        "BREATHING_RAINBOW_1",
        "BREATHING_RAINBOW_2",
        "FAST_RAINBOW",
        "SOLID_RED",
        "SOLID_GREEN",
        "SOLID_BLUE",
        "BREATHING_RAINBOW_3"
    ] 

    def _switch_delay(self):
        time.sleep_ms(self._SWITCH_TIME_CONSTANT_MS)
    
    def next_pattern(self):
        self._switch.value(False)
        self._switch_delay()
        self._switch.value(True)

    def is_home(self):
        return self._home.value() is 0

    def find_home(self):
        while self.is_home() is False:
            self.next_pattern()
            self._switch_delay()

    def set_pattern(self, pattern):
        if pattern not in self._PATTERNS:
            return
        self.find_home()
        for p in self._PATTERNS[:self._PATTERNS.index(pattern)]:
            self.next_pattern()
            self._switch_delay() 

    def __init__(self):
        self._home = Pin(self._HOMING_PIN, mode=Pin.IN, pull=Pin.PULL_DOWN)
        self._switch = Pin(self._SWITCH_PIN, mode=Pin.OPEN_DRAIN)
        self.find_home()
