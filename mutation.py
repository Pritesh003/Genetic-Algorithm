import numpy as np

def mutation(Children,Pm,L):
    for c in range(len(Children)):
        for i in range(L):
            p = np.random.uniform()
            if p<Pm:
                if Children[c][i]==0:
                    Children[c][i]=1
                else:
                    Children[c][i]=0
    return Children
