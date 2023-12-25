# yeelight-py

It using Yeelight-Python library from **[python-yeelight](https://github.com/skorokithakis/python-yeelight)**.
Check out their page and install the library using pip

So I combine these python script with **[HID Macros](https://www.hidmacros.eu/)** and call each of them with this line

```shell
Set oShell = CreateObject ("WScript.Shell")
oShell.run "pythonw [YOUR SCRIPT LOCATION]\yeelightToggle.py"
```
Change Python script to another script too.
