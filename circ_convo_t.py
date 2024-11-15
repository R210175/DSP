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
x1=[1,2,3,4]
x2=[4,0,3,2]
y=circ_conv(x1,x2)
x=np.array([1,2,3,4])
plt.subplot(2,1,1)
plt.plot(x,y)
plt.title("TIME DOMAIN")
plt.show()

#print("CIRCULAR CONVOLUTION IN TIME DOMAIN " ,y)
