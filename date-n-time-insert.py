# http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
# http://schurpf.com/python/python-hotkey-module/
import time
import pyhk


def fun():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print now

# create pyhk class instance
hot = pyhk.pyhk()

# add hotkey
hot.addHotkey(['Ctrl', 'Alt', 'D'], fun)

# start looking for hotkey.
hot.start()
