#delay property

import numpy as np
import matplotlib.pyplot as plt
import cmath

def DTFT(x,w):
  X=[]
  for i in w:
    add=0
    for k in range(len(x)):
      r=x[k]*cmath.exp(-1j*i*k)
      add+=r
    X.append(add)
  return np.array(X)
  
w=np.arange(-np.pi,np.pi,0.0001*np.pi)

def delay_dtft(x,w,j):
  X=[]
  for i in w:
    add=0 
    for k in range(len(x)):
      r=x[k]*cmath.exp(-1j*i*k)*cmath.exp(-1j*i*j)
      add+=r
    X.append(add)
  return np.array(X)
  
x=np.array([3,6,7,8,3])
x_delay=np.append(np.zeros(4),x)
X=delay_dtft(x,w,3)
X_delay=DTFT(x_delay,w)
"""if(np.array_equal(X,X_delay)):
	print("yahoooo..")
else:
	print("try again")"""
plt.figure()
plt.subplot(1,2,1)
plt.plot(w,np.abs(X))
plt.title("delayed input")

plt.figure()
plt.subplot(1,2,2)
plt.plot(w,np.abs(X_delay))
plt.title("delayed output ")

plt.show()
