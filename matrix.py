import numpy as np

X = np.random.normal(loc=1, scale=10, size=(1000, 50))
XcolMean=np.mean(X,axis=0)
XcolStd=np.std(X,axis=0)
print ('mean: ')
print (XcolMean)
print ('; std: ')
print (XcolStd)

X_norm = ((X-XcolMean)/XcolStd)
print ("matrix")
print (X)
print ("matrix - mean")
print (X-XcolMean)
print ("(matrix - mean)/std")
print (X_norm)
