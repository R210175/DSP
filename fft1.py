import cmath
import numpy as np
from matplotlib import pyplot as plt

x=[1,-1,2,4]
n=len(x)

def fft(x):
       n=len(x)
       if n==1:
           return x
       else:
            a=x[0::2]
            b=x[1::2]
            Even=fft(a)
            Odd=fft(b)
            Wn=np.exp(-1j*2*np.pi*np.arange(0,int(n/2))/n)
            X=np.concatenate([Even+Wn*Odd,Even-Wn*Odd])
            return X

output=fft(x)
print("fft result")
for value in output:
	print(value)
