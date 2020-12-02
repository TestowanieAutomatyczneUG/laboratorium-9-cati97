from Laptop import *

class Checker:
    def __init__(self):
        self.laptop = Laptop()

    def remainder(self, file):
        hour = self.laptop.getTime()
        if int(hour) > 17:
            self.laptop.playWavFile(file)


    def reset(self, file):
        result = self.laptop.wavWasPlayed(file)
        self.laptop.resetWav(file)
        return result

