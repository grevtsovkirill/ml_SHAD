import numpy as np

Z = np.array([[4, 5, 0], 
             [1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]])
print (Z)
Sumline= np.sum(Z,axis=1)
print (Sumline)

print (np.nonzero(Sumline>10) )
print (np.nonzero(Sumline<10) )
