import numpy as np
from matplotlib import pyplot as plt
def dtft(x):
	X=[]
	w=np.arange(-np.pi,np.pi,0.0001*np.pi)
	for f in w:
		s=0
		for n in range(0,len(x)):
			s=s+x[n]*np.exp(-1j*f*n)
		X.append(s)
	return w,X
n=np.arange(0,500)
X=[-1,2,3,0.4,3.5,7,3]
w,X=dtft(X)
x_magnitude=np.abs(X)
x_angle=np.angle(X)
plt.subplot(2,1,1)
plt.stem(w,x_magnitude)
plt.subplot(2,1,2)
plt.stem(w,x_angle)
plt.show()
