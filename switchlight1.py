#!/usr/bin/python3

# Light LED based on switch value, using busy polling loop

import wiringpi
import time

WP_INPUT  = 0
WP_OUTPUT = 1
WP_ALT    = 2

PIN_LED    = 14
PIN_SWITCH = 15

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_LED,    wiringpi.OUTPUT)
wiringpi.pinMode(PIN_SWITCH, wiringpi.INPUT)

light = 0
oldValue = wiringpi.digitalRead(PIN_SWITCH)

while True:
    newValue = wiringpi.digitalRead(PIN_SWITCH)
    if newValue and not oldValue:
        light = not light

    oldValue = newValue

    wiringpi.digitalWrite(PIN_LED, light)
    print (','.join([str(newValue),str(light)]))
    time.sleep(.01)
