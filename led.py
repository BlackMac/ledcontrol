#!/usr/bin/env python

import sys
import RPIO.PWM as PWM
import time

class RGBLed:
    def __init__(self, redPin, greenPin, bluePin):
        if not PWM.is_setup():
            PWM.setup(10,1)

        self.pins = [redPin, greenPin, bluePin]
        a=2
        while PWM.is_channel_initialized(a):
            a=a+1

        self.channels = [a, a+1, a+2]
        for channel_num in self.channels:
            PWM.init_channel(channel_num, subcycle_time_us=10000)

    def set_color(self, color, animated = False):
            PWM.add_channel_pulse(self.channels[0], self.pins[0], 0, int(color.r/255.0*999.0))
            PWM.add_channel_pulse(self.channels[1], self.pins[1], 0, int(color.g/255.0*999.0))
            PWM.add_channel_pulse(self.channels[2], self.pins[2], 0, int(color.b/255.0*999.0))

class RGBMatrix:
    def __init__(self, leds):
        if not PWM.is_setup():
            PWM.setup(10,1)
        self.leds = leds

    def fill(self):
        for led in self.leds:
            for x in range(0,256,15):
                led.set_color(Color(0,0,x))
                time.sleep(0.003);
            led.set_color(Color(0,0,255))
            for x in range(0,256,15):
                led.set_color(Color(0,x,255))
                time.sleep(0.003);
            led.set_color(Color(0,255,255))
            for x in range(0,256,15):
                led.set_color(Color(x,255,255))
                time.sleep(0.003);
            led.set_color(Color(255,255,255))

    def drain(self):
        for led in reversed(self.leds):
            for x in range(255,-1,-15):
                led.set_color(Color(x,255,255))
                time.sleep(0.003);
            led.set_color(Color(0,255,255))
            for x in range(255,-1,-15):
                led.set_color(Color(0,x,255))
                time.sleep(0.003);
            led.set_color(Color(0,0,255))
            for x in range(255,-1,-15):
                led.set_color(Color(0,0,x))
                time.sleep(0.003);
            led.set_color(Color(0,0,0))

    def set_color(self, color):
        for led in self.leds:
            led.set_color(color)

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
