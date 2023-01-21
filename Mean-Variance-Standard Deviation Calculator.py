import numpy as np

l=list(map(int,input('Enter list elements:').split()))
print('List=',l)  
print('Mean=',np.mean(l))
print('Variance=',np.var(l))
print('Standard deviation={0:.4f}'.format(np.std(l)))
print('Maximum=',max(l))
print('Minimum=',min(l))
print('Sum=',sum(l))
    
