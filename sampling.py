x=[1,2,3,4,5]
def sample(x,a):
	if a>1:
		y=[]
		for i in range(0,len(x)):
			if a*i<len(x):
				y.append(x[a*i])
		return y
k=sample(x,3)
print(k)	
