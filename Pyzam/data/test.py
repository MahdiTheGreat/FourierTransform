import scipy.io.wavfile as wavRead
import numpy as np
import matplotlib.pyplot as plt
import copy

signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)

fourier = np.fft.fft(signal)

n = signal.size

timestep = 0.1

freq = np.fft.fftfreq(n)

print(fourier)

print(freq)