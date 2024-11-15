import numpy as np
import matplotlib.pyplot as plt
def circ_reverse(x):
	x_r=[]
	N=len(x)
	for i in range(N):
		if (i==0):
			x_r.append(x[i])
		else:
			x_r.append(x[N-i])
	return x_r

def circ_shift(x,m):
	x_rd=[]
	N=len(x)
	for n in range(0,N):
		if n-m>=0:
			idx=(n-m)%N
		else :
			idx=N+n-m
		x_rd.append(x[idx])
	return x_rd

def circ_conv(x1,x2):
	y=[]
	N=len(x1)
	x2r=circ_reverse(x2)
	for m in range(N):
			sum=0
			x=circ_shift(x2r,m)
			for k in range(N):
				y2=x1[k]*x[k]
				sum+=y2
			y.append(y2)
	return np.array(y)
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
	return np.array(x)		
	
x1=[1,2,3,4]
x2=[4,0,3,2]
y=circ_conv(x1,x2)

N=len(x1)
x=np.array([0,1,2,3])
X=np.array(dft(x1,N))
Y=np.array(dft(x2,N))
z=X*Y
k=idft(z,N)

plt.subplot(2,1,1)
plt.plot(x,y)
plt.title("TIME DOMAIN")
plt.subplot(2,1,2)
plt.plot(x,np.abs(k))
plt.title("FREQ DOMAIN")
plt.show()

#print("CIRCULAR CONVOLUTION IN TIME DOMAIN " ,y)
			
