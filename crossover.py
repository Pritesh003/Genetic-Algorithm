import numpy as np
def crossover(Parents,n):
    
    for p in range(0,n-1,2):
        site1=np.random.randint(0,10)
        site2=np.random.randint(0,10)
        for i in range(site1,site2):
            temp=Parents[p][i]
            Parents[p][i]=Parents[p+1][i]
            Parents[p+1][i]=temp    
    
    return Parents
