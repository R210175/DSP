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
x1=[1,2,3,4]
x2=[-1,0,5,3]
print(circular_conv(x1,x2))
