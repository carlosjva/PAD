"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides
For Paper, "On Operator Theory-Based Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""



def AnomalyDetectorEigH(signal, L, N_hankel, tolerance, and_or):
    from numpy.linalg import eigh
    from numpy import zeros, where, nan, ones, logical_or, logical_and
    from statistics import mean,stdev
    from scipy.linalg import hankel
    
    x1 = signal.copy()
    xm = mean(x1)
    x0 = x1 - xm


    H = hankel(x0[:L],x0[(L-1):N_hankel])
    H1 = H@H.T
    eigvec = eigh(H1)[1]
    p = eigvec[:,0]

    lp = len(p)
    lx = len(x0)
    N = lx-lp

    d0 = zeros(lx)
    d1 = zeros(lx)

    for k in range(N):
        d0[k+lp-1] = abs(p.T@x0[(k):(k+lp)])
        d1[N-k-1] = abs(p.T@x0[(lx-k-lp):(lx-k)])

    threshold0 = tolerance*stdev(d0)
    threshold1 = tolerance*stdev(d1)
   
    
    d0 = (d0 >= threshold0)
    d1 = (d1 >= threshold1)

    if and_or == "AND":
        d = logical_and(d0,d1)
    if and_or == "OR":
        d = logical_or(d0,d1)

    di = where(d==1)[0]
    y = nan*ones(lx)
    y[di] = x0[di]
    
    return(d,di,y,x0,x1,xm)