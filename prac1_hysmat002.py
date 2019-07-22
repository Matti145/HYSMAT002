#!/usr/bin/python3

"""
Binary Counter
Matthew Hayes
HYSMAT002
Prac no. 1
22/07/2019
"""

import RPi.GPIO as GPIO
import time

led = 0
count = 0

bit = [17, 27, 22]
states = [[0,0,0], [1,0,0], [0,1,0], [1,1,0], [0,0,1], [1,0,1], [0,1,1], [1,1,1] ]
debounceTime = 300

def buttonPressed(val):
    global led
    global count
    if val == 18:
	if count < 7:
	    count += 1
        else:
	    count = 0
    else:
	if count > 0:
            count -= 1
	else:
            count = 7

    GPIO.output(bit, states[count])
    # end of buttonPressed

def init():
    GPIO.setmode(GPIO.BCM)

    # Outputs
    GPIO.setup(bit, GPIO.OUT)
    # Inputs
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set BCM as input with a pull down resistor
    GPIO.add_event_detect(18, GPIO.RISING, callback=buttonPressed, bouncetime=debounceTime) # set up interupt and debounce
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set BCM as input with a pull down resistor
    GPIO.add_event_detect(23, GPIO.RISING, callback=buttonPressed, bouncetime=debounceTime) # set up interupt and debounce
    # End of init

def main():
    # Allow for something else to be done
    time.sleep(60)
    #End of main

if __name__ == "__main__":
    try:
	init()
	while (True):
	    main()
    except KeyboardInterrupt:
	print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
	GPIO.cleanup()

	print("Error: ")
	print (e.message)
    # End if __name__ == "__main__"

# End
