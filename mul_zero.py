import numpy as np
from matplotlib import pyplot as plt
def conv_z_to_w(z,k):
	h_w=[]
	for w in k:
		p=1
		for i in z:
			p*=(1-(i*np.exp(-1j*w)))
		h_w.append(p)
	return h_w
p=int(input("Enter number of zeroes "))
z=[]
for i in range(p):
	r=int(input("enter the magnitude of z"))
	w=int(input("enter the angle from zeroaxis"))
	z.append(r*np.exp(1j*w))
k=np.arange(-np.pi,np.pi,0.0001*np.pi)
h_w=conv_z_to_w(z,k)
mag_plt=np.abs(h_w)
phs_plt=np.angle(h_w)
plt.subplot(2,1,1)
plt.plot(k,mag_plt)
plt.subplot(2,1,2)
plt.plot(k,phs_plt)
plt.xlabel("w-axis")
plt.ylabel("magnitude")
plt.show()

