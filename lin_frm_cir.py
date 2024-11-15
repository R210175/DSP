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
def idft(X,N):
	x=[]
	for n in np.arange(0,N):
		s=0
		for k in np.arange(0,N):
			s=s+X[k]*np.exp(1j*2*np.pi*n*k/N)
		d=s/N
		x.append(d)
	return x
a=[1,2]#l1=2
b=[5,7,6]#l2=3
a_zp=[1,2,0,0]#z.p=l2-1=2
b_zp=[5,7,6,0]#z.p=l1-1=1
x1=np.array(dft(a_zp,4))
x2=np.array(dft(b_zp,4))
x3=x1*x2
y=idft(x3,4)
print(np.real(y))
