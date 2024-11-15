import numpy as np
import matplotlib.pyplot as plt
import cmath
w=np.arange(-np.pi,np.pi,0.0001*np.pi)
def DTFT(x,w):
  X=[]
  for i in w:
    add=0
    for k in range(len(x)):
      r=x[k]*cmath.exp(-1j*i*k)
      add+=r
    X.append(add)
  return X
x=[0,1,2,3,4,5]
y=DTFT(x,w)
plt.subplot(1,3,1)
plt.plot(w,np.abs(y))
plt.xlabel("W")
plt.ylabel("|X(W)|")
plt.title("MAGNITUDE SPECTRUM")
plt.subplot(1,3,3)
plt.plot(w,np.angle(y))
plt.xlabel("W")
plt.ylabel("<X(W)")
plt.title("PHASE SPECTRUM")

plt.show()
