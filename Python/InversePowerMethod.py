"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides
For Paper, "On Operator Theory-Based Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

def InversePowerMethod(A,tol, kIterMax,q0):
    
    import numpy as np
    
    n = A.shape[0]

    x = np.random.rand(n).reshape(-1,1)

    B = A.copy()

    error = 1
    
    #First Run
    for od in range(n):
            B[od,od] = A[od,od] - q0
        
    x = np.linalg.solve(B,x)
    x = x/np.linalg.norm(x)
    lamOld = x.T@A@x
    
    kIter = 1
    
    while kIter < kIterMax:
        
        #od = on diagonal
        for od in range(n):
            B[od,od] = A[od,od] - q0
        
        x = np.linalg.solve(B,x)
        x = x/np.linalg.norm(x)
        lamNew = x.T@A@x
        kIter = kIter + 1
        
        error = np.abs(lamNew - lamOld)
        if error < tol:
            return (x, lamNew, kIter)
        else:
            lamOld = lamNew
        
        
        
    return (x, lamNew, kIter)