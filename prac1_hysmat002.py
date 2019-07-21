#!/usr/bin/python3

"""
Binary Counter
Matthew Hayes
HYSMAT002
Prac no. 1
/07/2019
"""


import RPi.GPIO as GPIO


led = 0
count = 000

bit1 = 17
bit2 = 27
bit3 = 22

debounceTime = 300

def buttonPressed(val):
    global led
    global count
    if val == 18:
	count += 1
    else:
	if count > 0:
            count -= 1
	else:
            count = 3
    # end of buttonPressed

def init():
    GPIO.setmode(GPIO.BCM)

    # Outputs
    GPIO.setup(bit1, GPIO.OUT) # set BCM 17 as output
    GPIO.setup(bit2, GPIO.OUT)
    GPIO.setup(bit3, GPIO.OUT)


    # Inputs
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set BCM as input with a pull down resistor
    GPIO.add_event_detect(18, GPIO.RISING, callback=buttonPressed, bouncetime=debounceTime) # set up interupt and debounce
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set BCM as input with a pull down resistor
    GPIO.add_event_detect(23, GPIO.RISING, callback=buttonPressed, bouncetime=debounceTime) # set up interupt and debounce
    # End of init

def main():
    binary = bin( count + int('1000000',2))
    GPIO.output(bit1, int(binary[-1]))
    GPIO.output(bit2, int(binary[-2]))
    GPIO.output(bit3, int(binary[-3]))
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
    except e:
	GPIO.cleanup()

	print("Error: ")
	print (e.message)
    # End if __name__ == "__main__"

# End
