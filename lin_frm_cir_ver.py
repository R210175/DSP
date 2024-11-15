import numpy as np 
from matplotlib import pyplot as plt
signal=[1,2]
kernel=[5,7,6]
convolved_length=len(signal)+len(kernel)-1
convolved_signal=np.zeros(convolved_length)
for i in range(convolved_length):
	for j in range(len(kernel)):
		if i-j>=0 and i-j<len(signal):
			convolved_signal[i]+=signal[i-j]*kernel[j]
print(convolved_signal)

