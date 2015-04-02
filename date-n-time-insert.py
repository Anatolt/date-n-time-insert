# http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
# http://schurpf.com/python/python-hotkey-module/
# pip install clipboard
import clipboard
import time
import pyhk


def fun():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    clipboard.copy(now)
    clipboard.paste()

# create pyhk class instance
hot = pyhk.pyhk()

# add hotkey
hot.addHotkey(['Ctrl', 'V'], fun)

# start looking for hotkey.
hot.start()
