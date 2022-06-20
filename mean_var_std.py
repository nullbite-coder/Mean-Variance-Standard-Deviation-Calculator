import numpy as np

def calculate(num_list):
    if(len(num_list)!=9):
        raise ValueError("List must contain nine numbers")
    num = np.array(num_list)
    num = num.reshape((3,3))
    dic = {
        'mean': [[],[],0],
        'variance': [[],[],0],
        'standard deviation': [[],[],0],
        'max': [[],[],0],
        'min': [[],[],0],
        'sum': [[],[],0],
    }
    for i in range(3):
        dic['mean'][1].append(num[i:i+1,:].mean())
        dic['mean'][0].append(num[:,i:i+1].mean())
        dic['mean'][2] = num.mean()

        dic['variance'][1].append(num[i:i+1,:].var())
        dic['variance'][0].append(num[:,i:i+1].var())
        dic['variance'][2] = num.var()

        dic['standard deviation'][1].append(num[i:i+1,:].std())
        dic['standard deviation'][0].append(num[:,i:i+1].std())
        dic['standard deviation'][2] = num.std()

        dic['max'][1].append(num[i:i+1,:].max())
        dic['max'][0].append(num[:,i:i+1].max())
        dic['max'][2] = num.max()    

        dic['min'][1].append(num[i:i+1,:].min())
        dic['min'][0].append(num[:,i:i+1].min())
        dic['min'][2] = num.min()

        dic['sum'][1].append(num[i:i+1,:].sum())
        dic['sum'][0].append(num[:,i:i+1].sum())
        dic['sum'][2] = num.sum()

    return dic

