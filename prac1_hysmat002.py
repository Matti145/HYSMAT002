#!/usr/bin/python3

"""
Matthew Hayes
HYSMAT002
Prac no. 1
/07/2019
"""


import RPi.GPIO as GPIO


led = 0
count = 0

def buttonPressed(val):
    global led
    global count
   # print ("Button Pressed!")
    if led:
	led =  0
    else:
	led =  1


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT) # set BCM 17 as output
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set BCM as input with a pull down resistor
    GPIO.add_event_detect(18, GPIO.RISING, callback=buttonPressed, bouncetime=300)

def main():
    GPIO.output(17, led)
    #End of main

if __name__ == "__main__":
    try:
	init()
	while True:
	    main()
    except KeyboardInterrupt:
	print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
	print ("Some other error occurred")
	GPIO.cleanup()
    # End if __name__ == "__main__"

# End
