

import sys 
import numpy as np

# -------------------------------------------------------------------------
def get_preds(file_name):
    
    preds=[]
    with open(file_name) as file:
        for line in file:
            v = line.rstrip().split()
            
            preds.append([v[0], float(v[1]), int(v[2])])
    return preds


# -------------------------------------------------------------------------
def get_confusion_matrix(preds, threshold=0.001):
    
    cm = np.zeros((2,2))
    n = len(preds)
    
    for k in range(n):
        j = 0
        i = preds[k][2] 

        
        if preds[k][1] <= threshold:
            j += 1
            
        cm[i,j] += 1

    return cm

# -------------------------------------------------------------------------
def get_accuracy(cm):
    
    return (cm[0,0] + cm[1,1]) / np.sum(cm)

def get_mcc(cm):
    
    TP = cm[1,1]
    TN = cm[0,0]
    FP = cm[0,1]
    FN = cm[1,0]
    
    d = (TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)
    
    
    if d == 0:
        return 0.0
        
    return (TP*TN - FP*FN) / np.sqrt(d)

# -------------------------------------------------------------------------
if __name__=='__main__':
    file_name = sys.argv[1]
    th = float(sys.argv[2])
    
    preds = get_preds(file_name)
    cm = get_confusion_matrix(preds, th)
    acc = get_accuracy(cm)
    mcc = get_mcc(cm)
    
    
    print(f'TH: {th}\tACC: {acc:.4f}\tMCC: {mcc:.4f}')