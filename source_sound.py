import sksound as sk
import numpy as np
import os


class Signals:

    # Wave sound properties
    def __init__(self):
        self.rate = 22050
        self.dt = 1. / self.rate
        self.freq = 440
        self.dot_t = np.arange(0, 0.05, self.dt)  # Range of time for "dot" sound
        self.dash_t = np.arange(0, 0.15, self.dt)  # Range of time for "dash" sound
        self.x = np.sin(2 * np.pi * self.freq * self.dot_t)
        self.amp = 2 ** 13
        self.sound_data = np.int16(self.x * self.amp)
        self.make_signal()

    # Function that check if sound files exist, if not, make then
    def make_signal(self):
        if os.path.isfile("sounds/dot.wav") and os.path.isfile("sounds/dash.wav"):
            pass
        else:
            os.makedirs("sounds")
            self.make_dot()
            self.make_dash()

    # Function that create the 'dot' sound
    def make_dot(self):
        my_sound = sk.sounds.Sound(inData=self.sound_data, inRate=self.rate)
        my_sound.write_wav("sounds/dot.wav")

    # Function that create the 'dash' sound
    def make_dash(self):
        x = np.sin(2 * np.pi * self.freq * self.dash_t)  # Generación del sonido "dash" con diferente rango de tiempo
        sound_data = np.int16(x * self.amp)
        my_sound = sk.sounds.Sound(inData=sound_data, inRate=self.rate)
        my_sound.write_wav("sounds/dash.wav")

