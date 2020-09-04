import numpy as np
def Roulette(population,P,N,n):
    cumulative_prob_sum = np.cumsum(P)
    cum_prob = np.cumsum(P).tolist()
    Par_ind = []
    
    for i in range(n):
        x=np.random.uniform()
        for index in range(N):
            if x<cum_prob[index]:
                Par_ind.append(index)
                break
    Parents=population[[Par_ind],:][0]
    return Parents
