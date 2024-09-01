from yeelight import Bulb
import apprise

#Yeelight
bulb = Bulb("192.168.68.9")
properties = bulb.get_properties()
power = properties["power"] == "on"
colorMode = properties["color_mode"] == "1"
bright = properties["bright"] != "100"

#Notification
apobj = apprise.Apprise()
apobj.add('windows://')
#apobj.add('gotify://192.168.68.30:1004/Ae-eNhbp4zp6bmG/?priority=high')

def brightness():
    """Function brightness 100% and color white"""
    bulb.set_brightness(100)
    bulb.set_color_temp(6500)

def toggle():
    """Function toggling lamp and do brightness"""
    bulb.toggle()
    brightness()

def NotifyOn():
    apobj.notify(
    body="Uhh so bright! Your lamp just turn on.",
    title='Lamp On',
)
def NotifyOff():
    apobj.notify(
    body="Enjoy your darkness.",
    title='Lamp Off',
)
def NotifyBright():
    apobj.notify(
    body="Hey you need more light power!",
    title="White lamp",
)
def NotifyRGB():
    apobj.notify(
    body="RGB can't speed your productivity!",
    title="White lamp",
)

if not power:
    toggle()
    NotifyOn()
elif colorMode:
    brightness()
    NotifyRGB()
elif bright:
    brightness()
    NotifyBright()
else:
    toggle()
    NotifyOff()