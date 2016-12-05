import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys
import os.path


#Signal
path = os.path.dirname(__file__)
wavFile = wave.open('../samples/scout_1000.wav', 'r')
signal = wavFile.readframes(-1)
signal = np.fromstring(signal, 'Int16')

#Fourier
fs, data = wavfile.read('scout_1000.wav') # load the data

channel_1 = data.T[0] # this is a two channel soundtrack

b=[]
for ele in range(channel_1):
    b.append((ele/2**8.)*2-1) # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = len(c)/2  # you only need half of the fft list (real signal symmetry)

#Signal
plt.subplot(4, 1, 1)
plt.title('Music Analysis', fontsize=40)
plt.plot(signal)

#Channel 1
plt.subplot(4, 1, 2)
plt.plot(channel_1)

#Channel 2
plt.subplot(4, 1, 3)
plt.plot()

#Fourier
plt.subplot(4, 1, 4)
plt.plot(abs(c[:(d-1)]),'r')

plt.show()