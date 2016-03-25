#!/usr/bin/env python

import led
from flask import Flask

matrix = led.RGBMatrix([
            led.RGBLed(27,18,17), # top left
            led.RGBLed(22,23,24), # top right
            led.RGBLed(13,6,12),  # bottom right
            led.RGBLed(25,4,5),   # bottom left
            ])

app = Flask(__name__)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

@app.route("/fill")
def fill():
    matrix.fill()
    return '{result: "ok"}'

@app.route("/drain")
def drain():
    matrix.drain()
    return '{result: "ok"}'

@app.route("/color/<hexcolor>")
def color(hexcolor):
    r, g, b = hex_to_rgb(hexcolor)
    matrix.set_color(led.Color(int(r), int(g), int(b)))
    return '{result: "ok"}'

@app.route("/colors/<hexcolor1>/<hexcolor2>/<hexcolor3>/<hexcolor4>")
def colors(hexcolor1, hexcolor2, hexcolor3, hexcolor4):
    r, g, b = hex_to_rgb(hexcolor1)
    matrix.leds[0].set_color(led.Color(int(r), int(g), int(b)))
    r, g, b = hex_to_rgb(hexcolor2)
    matrix.leds[1].set_color(led.Color(int(r), int(g), int(b)))
    r, g, b = hex_to_rgb(hexcolor3)
    matrix.leds[2].set_color(led.Color(int(r), int(g), int(b)))
    r, g, b = hex_to_rgb(hexcolor4)
    matrix.leds[3].set_color(led.Color(int(r), int(g), int(b)))
    return '{result: "ok"}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




# square.set_color(RgbColor(0,0,0))
# #square.rotate_on()
# #square.rotate_off()
#
#
# print "Press CTRL-C to finish"
#
# try:
#     while True:
#         for x in range(0,256,2):
#             square.set_color(RgbColor(x,0,0));
#             time.sleep(0.01);
#         for x in range(0,256,2):
#             square.set_color(RgbColor(255,x,0));
#             time.sleep(0.01);
#         for x in range(0,256,2):
#             square.set_color(RgbColor(255,255,x));
#             time.sleep(0.01);
#         square.rotate_off()
#
#
# except KeyboardInterrupt:
#     square.all_off()
#     RPIO.cleanup()
