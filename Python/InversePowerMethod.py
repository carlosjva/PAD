"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides, E. Segura, C. Vargas
For Paper, "A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

def InversePowerMethod(A,tol, kIterMax,q0):
    
    from numpy.linalg import solve, norm
    from numpy import abs as npabs
    from numpy.random import rand

    
    n = A.shape[0]

    x = rand(n).reshape(-1,1)

    B = A.copy()

    error = 1
    
    #First Run
    for od in range(n):
            B[od,od] = A[od,od] - q0
        
    x = solve(B,x)
    x = x/norm(x)
    lamOld = x.T@A@x
    
    kIter = 1
    
    while kIter < kIterMax:
        
        #od = on diagonal
        for od in range(n):
            B[od,od] = A[od,od] - lamOld
        
        x = solve(B,x)
        x = x/norm(x)
        lamNew = x.T@A@x
        kIter = kIter + 1
        
        error = npabs(lamNew - lamOld)
        if error < tol:
            return (x, lamNew, kIter)
        else:
            lamOld = lamNew
        
        
        
    return (x, lamNew, kIter)