# add to esp32 boot.py using thonny
import machine
# This disables the brownout reset
import micropython
from machine import mem32
# Specific command for ESP32 to ignore brownout
mem32[0x3ff480d4] = 0x0
