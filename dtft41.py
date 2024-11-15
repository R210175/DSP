import numpy as np
import matplotlib.pyplot as plt
import cmath

def DTFT(x,w):
  X=[]
  for i in w:
    add=0
    for k in range(len(x)):                    #linearity property
      r=x[k]*cmath.exp(-1j*i*k)
      add+=r
    X.append(add)
  return  np.array(X)

w=np.arange(-np.pi,np.pi,0.0001*np.pi)		
x1=np.array([4,5,7,2,3])
x2=np.array([2,7,9,8,5])
if len(x1)==len(x2):
	x3=x1+x2
	X1=DTFT(x1,w)
	X2=DTFT(x2,w)
	X3=DTFT(x3,w)
	y=X1+X2
plt.figure()
plt.plot(w,np.abs(y))
plt.xlabel("W")
plt.ylabel("|X(W)|")
plt.title("MAGNITUDE1 SPECTRUM")
plt.figure()
plt.plot(w,np.abs(X3))
plt.xlabel("W")
plt.ylabel("|X(W)|")
plt.title("MAGNITUDE SPECTRUM")

plt.show()
