from random import randint
from yeelight import Bulb
bulb = Bulb("192.168.1.9")

properties = bulb.get_properties()
power = properties["power"] != "on"

r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

def rgb():
    bulb.set_brightness(100)
    bulb.set_rgb(r, g, b)

if power:
    bulb.turn_on()
    rgb()
else:
    rgb()