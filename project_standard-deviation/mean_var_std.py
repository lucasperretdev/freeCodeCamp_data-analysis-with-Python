import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

#use of reshape to define a new shape for my array
    array_unshaped =np.array(list)
    clean =np.reshape(array_unshaped, [3,3])

#use of np.tolist() in order to convert numpy array into list    
    calculations = dict()
    calculations['mean'] = [np.mean(clean,axis=0).tolist(), np.mean(clean, axis=1).tolist(),np.mean(clean)]
    calculations['variance'] = [np.var(clean,axis=0).tolist(), np.var(clean, axis=1).tolist(),np.var(clean)]
    calculations['standard deviation'] = [np.std(clean,axis=0).tolist(), np.std(clean, axis=1).tolist(),np.std(clean)]
    calculations['max'] = [np.max(clean,axis=0).tolist(), np.max(clean, axis=1).tolist(),np.max(clean)]
    calculations['min'] = [np.min(clean,axis=0).tolist(), np.min(clean, axis=1).tolist(),np.min(clean)]
    calculations['sum'] = [np.sum(clean,axis=0).tolist(), np.sum(clean, axis=1).tolist(),np.sum(clean)]

    return calculations

