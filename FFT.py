from pylsl import StreamInlet, resolve_stream
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

canal1 = list()
timestamp_list = list()
len_sample = 2000

plt.ion()

while True:

    sample, timestamp = inlet.pull_sample()

    if len(canal1) > len_sample:
        del canal1[0]
        del timestamp_list[0]

    canal1.append(sample[0])
    timestamp_list.append(timestamp)

    if len(canal1) > len_sample:
        f = interp1d(timestamp_list, canal1)
        FFT = np.fft.fft(f(timestamp_list))
        plt.plot(FFT)
        plt.xlim(0, len_sample/2)
        plt.ylim(-0.3e7,0.3e7)
        plt.draw()
        plt.pause(0.01)
        plt.clf()


# EEG-Maynooth
