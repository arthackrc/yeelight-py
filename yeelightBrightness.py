from yeelight import Bulb
import apprise

#Yeelight
bulb = Bulb("192.168.68.9", auto_on=True)
properties = bulb.get_properties()
bright = int(properties["bright"])

#Notification
apobj = apprise.Apprise()
apobj.add('windows://')
#apobj.add('gotify://192.168.68.30:1004/Ae-eNhbp4zp6bmG/?priority=high')

def Notify0():
    apobj.notify(
    body="We keep the light and the dark together.",
    title='Brightness as low as fuck',
)
def Notify50():
    apobj.notify(
    body="Just ordinary people",
    title='Brightness 50%',
)
def Notify100():
    apobj.notify(
    body="Oh, come on man, really?",
    title="Brightness Pro Max",
)

if bright == 100:
    bulb.set_brightness(0)
    Notify0()
elif bright == 1:
    bulb.set_brightness(50)
    Notify50()
else:
    bulb.set_brightness(100)
    Notify100()