#voice recorder in python

import sounddevice as sd

from scipy.io.wavfile import write

import wavio as wv

freq = 44100
duration = 6.5

recording = sd.rec(int(duration*freq), samplerate=freq, channels=2 )

sd.wait()
write("recording0.wav", freq, recording)

wv.write("recording1.wav", recording, freq, sampwidth=2)
































"""
#time counter
import time

input_time = int(input("enter the time(seconds) : "))

for i in range(input_time,0, -1):
    seconds = int(i%60)
    minutes = int((i/60)%60)
    hours = int((i/3600))
    print(f"{hours:02}: {minutes:02} : {seconds:02} \r")
    time.sleep(1)
print("TIME'S UP")
"""












