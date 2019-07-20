#!/usr/bin/python3

"""
Matthew Hayes
HYSMAT002
Prac no. 1
/07/2019
"""


import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

    GPIO.output(17,1)
    #End of main

if __name__ == "__main__":
    try:
	while True:
	    main()
    except KeyboardInterrupt:
	print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    #except:
#	print ("Some other error occurred")
    # End if __name__ == "__main__"

# End
