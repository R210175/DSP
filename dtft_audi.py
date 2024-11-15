import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

def dtft(x):
    N = len(x)
    w = np.arange(-np.pi, np.pi, 0.0001 * np.pi)
    X = np.zeros(len(w), dtype=complex)
  
    for idx, f in enumerate(w):
        s = np.sum(x * np.exp(-1j * f * np.arange(N)))
        X[idx] = s
        
    return w, X
    
filename = '/home/rguktvalley/Documents/DSP Lab/week3/example_small.wav'
fs, data = wavfile.read(filename)
if len(data.shape) > 1:
    data = data.mean(axis=1)
x = data[:500]
w, X = dtft(x)
x_magnitude = np.abs(X)
x_angle = np.angle(X)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(w, x_magnitude)
plt.title('DTFT Magnitude Spectrum')
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Magnitude')
plt.xlim([-np.pi, np.pi]) 
plt.subplot(2, 1, 2)
plt.plot(w, x_angle)
plt.title('DTFT Phase Spectrum')
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Phase (radians)')
plt.xlim([-np.pi, np.pi]) 
plt.tight_layout()
plt.show()
