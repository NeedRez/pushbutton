#	filename: pushbutton.py
#	author: kjp@kellyfx.com
#	desc: PushButton class
#       functionally an integrator driven by up/down switch inputs, large hysteresis triggered at zero crossing

# filt value is how many cycles needed to flip state
# pbswup or pbswdn are called to change filt value, return 0 = still being filtered, 1 = stable condition, -1 = state change
# pbstate is called to find current switch state, -1 is returned if in the pbswdn position
# filt initialized to 0 will always generate event flag and hit limit on first cycle
# filt can be set to future limit or beyond but next cycle will cause it to limit
class PushButton:
    'Pushbutton filter with hysteresis'
    def __init__(self, filt):
        self.filt = filt
        self.toggle_position = False

    def clickin(self, limit):
        if self.filt < 0:
            self.filt = -limit
            return 1
        elif self.filt == 0:
            self.filt = -limit
            return -1
        else:
            self.filt -= 1
            return 0

    def clickin_toggle(self, limit):
        if self.filt < 0:
            self.filt = -limit
            return 1
        elif self.filt == 0:
            self.filt = -limit
            self.toggle_position = not self.toggle_position
            return -1
        else:
            self.filt -= 1
            return 0

    def clickout(self, limit):
        if self.filt > 0:
            self.filt = limit
            return 1
        elif self.filt == 0:
            self.filt = limit
            return -1
        else:
            self.filt += 1
            return 0

    def clickout_toggle(self, limit):
        if self.filt > 0:
            self.filt = limit
            return 1
        elif self.filt == 0:
            self.filt = limit
            self.toggle_position = not self.toggle_position
            return -1
        else:
            self.filt += 1
            return 0

    def click_position(self):
        if self.filt < 0:
            return -1
        else:
            return 0
