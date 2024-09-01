#Yeelight
from yeelight import Bulb
bulb = Bulb("192.168.68.9")

properties = bulb.get_properties()
power = properties["power"] != "on"

def rgb():
    """Function to do the Brightness to 100% and random color using randint"""
    bulb.set_brightness(100)
    bulb.set_rgb(r, g, b)

#Randomize Color
from random import randint
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

import webcolors
#https://stackoverflow.com/a/9694246
#Update https://stackoverflow.com/a/78869532
def closest_colour(requested_colour):
    min_colours = {}
    for name in webcolors.names("css3"):
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = (r, g, b)
actual_name, closest_name = get_colour_name(requested_colour)

#Notification
import apprise
apobj = apprise.Apprise()
apobj.add('windows://')
#apobj.add('gotify://192.168.68.30:1004/Ae-eNhbp4zp6bmG/?priority=high')

def NotifyColor():
    apobj.notify(
        body="Your lamp color changed to "+closest_name,
        title='Lamp Color',
)

if power:
    bulb.turn_on()
    rgb()
    NotifyColor()
else:
    rgb()
    NotifyColor()
