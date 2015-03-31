# http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
# http://schurpf.com/python/python-hotkey-module/
import time
import pyhk
from Tkinter import Tk


def fun():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(now)
    r.destroy()
    print now

# create pyhk class instance
hot = pyhk.pyhk()

# add hotkey
# if you want just copy uncoment this 
# hot.addHotkey(['Ctrl', 'Alt' ,'D'], fun)
hot.addHotkey(['Ctrl', 'V'], fun)

# start looking for hotkey.
hot.start()
