#!/usr/bin/python3

# LED on GPIO 14 toggles with switch on GPIO 15, using interrupt-driven callback

import wiringpi
import time

WP_INPUT  = 0
WP_OUTPUT = 1
WP_ALT    = 2

PIN_LED    = 14
PIN_SWITCH = 15

DEBOUNCE_DURATION = 10 # milliseconds

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode (PIN_LED,    wiringpi.GPIO.OUTPUT)
wiringpi.pinMode (PIN_SWITCH, wiringpi.GPIO.INPUT)

lastTime = wiringpi.millis()
lightValue = 0

def switchToggle():
    global lastTime
    global lightValue

    t = wiringpi.millis()

    if DEBOUNCE_DURATION < (t - lastTime):
        print ('Toggle! {}'.format(t))
        lightValue = not lightValue
        wiringpi.digitalWrite(PIN_LED, lightValue)
    else:
        print ('Bounce! {}'.format(t))

    lastTime = t

wiringpi.wiringPiISR (PIN_SWITCH, wiringpi.GPIO.INT_EDGE_RISING, switchToggle)

while True:
    wiringpi.delay (2000)
