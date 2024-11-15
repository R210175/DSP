import numpy as np
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			s=s+x[n]*np.exp(-1j*2*np.pi*n*k/N)
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
x1=[1,2,3,4]
x2=[-1,0,5,3]
N=len(x1)
X=np.array(dft(x1,N))
Y=np.array(dft(x2,N))
z=X*Y
k=idft(z,N)
print(np.real(k))
