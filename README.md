# pushbutton.py
Usage:
from pushbutton import PushButton
while True:
    sw_whtgrn = PushButton(10)

    if GPIO.input(12):  sw_whtgrn.clickout(10)
    else:               sw_whtgrn.clickin_toggle(10)

    if sw_whtgrn.toggle_position:   GPIO.output(26, GPIO.HIGH)
    else:                           GPIO.output(26, GPIO.LOW)

    time.sleep(0.005)
