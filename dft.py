import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			l=k/N
			s=s+x[n]*np.exp(-1j*2*np.pi*n*l)
		X.append(s)
	return X
a=[1,2,3,4,5]
N=len(a)
X=dft(a,N)
k=[0,1,2,3,4]
X_magnitude=np.abs(X)
X_phase=np.angle(X)
plt.subplot(2,1,1)
plt.stem(k,X_magnitude)
plt.subplot(2,1,2)
plt.stem(k,X_phase)
plt.show()
