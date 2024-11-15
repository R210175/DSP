import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			s=s+x[n]*np.exp(-1j*2*np.pi*n*k/N)
		X.append(s)
	return X
n=np.arange(1000)
x=np.sin(2*np.pi*200*n/1800)
N=len(x)
X=dft(x,N)
X_magnitude=np.abs(X)
X_phase=np.angle(X)
plt.subplot(2,1,1)
plt.stem(X_magnitude)
plt.subplot(2,1,2)
plt.stem(X_phase)
plt.show()
