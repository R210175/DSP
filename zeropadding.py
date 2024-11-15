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
a=[1,2,3,4,]
b=[1,2,3,4,0,0]
c=[1,2,3,4,0,0,0,0,0]
X1=dft(a,4)
X2=dft(b,6)
X3=dft(c,9)
X1_mag=np.abs(X1)
X2_mag=np.abs(X2)
X3_mag=np.abs(X3)
plt.subplot(3,1,1)
plt.plot(X1_mag)
plt.subplot(3,1,2)
plt.plot(X2_mag)
plt.subplot(3,1,3)
plt.plot(X3_mag)
plt.show()
