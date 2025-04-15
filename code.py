"""
March 25, 2025
by: Liya G

This program uses a sonar.
"""

import time
import board
import adafruit_hcsr04
import digitalio

# variables
delay_time = 0.5
distance = 0

# setup
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP15, echo_pin = board.GP14)

# loop
while True:
    # Sonar gets the distance form object
    #time.sleep(1)
    distance = sonar.distance
    #time.sleep(1)

    print(f"Distance: {distance} cm")

    # The commented out code is not part of the actual code but is needed to get it working by uncommenting it and then recommenting it
    time.sleep(delay_time)