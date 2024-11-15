import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

def plot_dft(signal, fs):
    N = len(signal)
    X = np.fft.fft(signal)
    X_magnitude = np.abs(X)
    X_phase = np.angle(X)
    freqs = np.fft.fftfreq(N, d=1/fs)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(freqs[:N // 2], X_magnitude[:N // 2])  
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.subplot(2, 1, 2)
    plt.plot(freqs[:N // 2], X_phase[:N // 2]) 
    plt.title('Phase Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (radians)')
    
    plt.tight_layout()
    plt.show()
filename = '/home/rguktvalley/Documents/DSP Lab/week 5/example_small.wav'
fs, x = wavfile.read(filename)

if len(x.shape) > 1:
    x = x[:, 0]
if len(x) == 0:
    raise ValueError("The audio file is empty or could not be read properly.")
if np.issubdtype(x.dtype, np.integer):
    x = x.astype(float)

plot_dft(x, fs)

