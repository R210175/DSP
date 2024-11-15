import numpy as np
from matplotlib import pyplot as plt

def dtft(x):
    w = np.arange(-np.pi, np.pi, 0.0001 * np.pi)
    X = np.zeros(len(w), dtype=complex)
    for i, f in enumerate(w):
        X[i] = np.sum(x * np.exp(-1j * f * np.arange(len(x))))
    
    return w, X
def auto(x):
    N = len(x)
    r = np.zeros(N)
    for m in range(N):
        r[m] = np.sum(x[:N - m] * x[m:])
    
    return r
x = np.array([1, 2, 3, 4])
r = auto(x)
w_rxx, Rxx = dtft(r)
w_x, X_w = dtft(x)
X_mag = np.abs(X_w)
ESD = X_mag**2
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(w_rxx, np.abs(Rxx))
plt.title('Autocorrelation Sequence Magnitude')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.plot(w_x, ESD)
plt.title('Power Spectral Density (ESD)')
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Magnitude Squared')

plt.tight_layout()
plt.show()
