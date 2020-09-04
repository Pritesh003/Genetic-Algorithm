def decode(population, x_1, x_2, l1, l2):
    x1_bin = population[:,:5]
    x2_bin = population[:,5:]
    x1_binary = [''.join(row) for row in x1_bin.astype(str).tolist()]
    x2_binary = [''.join(row) for row in x2_bin.astype(str).tolist()]
    d1 = [float(int(row,2)) for row in x1_binary]
    d2 = [float(int(row,2)) for row in x2_binary]
    
    x1=[]
    x2=[]
    [x1.append(min(x_1) + (max(x_1)-min(x_1))*d/pow(2,(l1-1))) for d in d1]
    [x2.append(min(x_2) + (max(x_2)-min(x_2))*d/pow(2,(l2-1))) for d in d2]
    
    return [x1, x2]
