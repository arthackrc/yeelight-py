from yeelight import *
bulb = Bulb("192.168.1.9", auto_on=True)

properties = bulb.get_properties()
bright = int(properties["bright"])

if bright == 100:
    bulb.set_brightness(0)
elif bright == 1:
    bulb.set_brightness(50)
else:
    bulb.set_brightness(100)