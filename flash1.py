#!/usr/bin/python3

# Flash LED with cycles of 100ms on + 1000ms off

import wiringpi
import time

PIN_LED  = 14
TIME_ON  = 0.100
TIME_OFF = 0.400

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN_LED, wiringpi.OUTPUT)

while True:
    wiringpi.digitalWrite (PIN_LED, 1)
    print ('On')
    time.sleep (TIME_ON)
    wiringpi.digitalWrite (PIN_LED, 0)
    print ('Off')
    time.sleep (TIME_OFF)
