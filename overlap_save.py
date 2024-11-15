import numpy as np
def circular_shift(x,m):
	N=len(x)
	y=[]
	for n in range(0,N):
		if(n-m)>=0:
			idx=(n-m)%N
		else:
			idx=N+(n-m)
		y.append(x[idx])
	return y
def circular_conv(x1,x2):
	z=[]
	a=x2[1:]
	x2r=[x2[0]]+a[::-1]
	for n in range(len(x1)):
		y=circular_shift(x2r,n)
		z.append(np.dot(x1,y))
	return z
def overlap(x,h,N):
	m=len(h)
	l=N-m+1
	x_pad=np.concatenate((np.zeros(m-1),x))
	y=np.zeros(len(x)+m-1)
	for i in range(0,len(x),l):
		x_block=x_pad[i:i+N]
		y_block=circular_conv(x_block,h)
		y[i:i+l]=y_block[m-1:]
	return y
x1=[7,6,4,5,2,4,5,2,3]
h1=[1,2,3]
N=3
y1=overlap(x1,h1,N)
print(y1)

