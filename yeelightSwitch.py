import customtkinter
from yeelight import Bulb

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('Yeelight Switcher')
w = 260
h = 100
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/3.8) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

bulb = Bulb("192.168.1.9")

buttonOn = customtkinter.CTkButton(
    root,
    text="Light ON",
    command=bulb.turn_on,
    width=260
)
buttonOn.pack(padx=20, pady=10)

buttonOff = customtkinter.CTkButton(
    root,
    text="Light OFF",
    command=bulb.turn_off,
    width=260
)
buttonOff.pack(padx=20, pady=10)

root.mainloop()
