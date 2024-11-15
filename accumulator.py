import numpy as np
from matplotlib import pyplot as plt
input_signal=[1,2,3,4]
output_signal=[]
accumulator=0
N=len(input_signal)
for k in range(N):
	accumulator+=input_signal[k]
	output_signal.append(accumulator)
print(output_signal)
plt.subplot(2,1,1)
plt.stem(input_signal)
plt.subplot(2,1,2)
plt.stem(output_signal)
plt.show()


