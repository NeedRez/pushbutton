# pushbutton.py

A PushButton object is a polled switch. Example below shows how to toggle when clicked, and set a GPIO accordingly. Code is written with more deterministic timing and low CPU overhead.

Usage:
 from pushbutton import PushButton
 sw_whtgrn = PushButton(10)

 while True:
    if GPIO.input(12):  sw_whtgrn.clickout(10)
    else:               sw_whtgrn.clickin_toggle(10)

    if sw_whtgrn.toggle_position:   GPIO.output(26, GPIO.HIGH)
    else:                           GPIO.output(26, GPIO.LOW)

    time.sleep(0.005)
