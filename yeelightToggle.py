from yeelight import Bulb
bulb = Bulb("192.168.1.9")

properties = bulb.get_properties()
power = properties["power"] == "on"
colorMode = properties["color_mode"] == "1"
bright = properties["bright"] != "100"

def brightness():
    """Function brightness 100% and color white"""
    bulb.set_brightness(100)
    bulb.set_color_temp(6500)

def toggle():
    """Function toggling lamp and do brightness"""
    bulb.toggle()
    brightness()

if not power:
    toggle()
elif colorMode or bright:
    brightness()
else:
    toggle()