"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides, E. Segura, C. Vargas
For Paper, "A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""



def AnomalyDetectorEigH(signal, L, N_hankel, tolerance, and_or):
    """
    The algorithm used to detect the anomaly using the Hermitian Eigenvalue 
    method. It used that left singular vector with the smallest singular
    value to detect the anomaly
    
    This function contains the training and the detection on the signal
    

    Parameters
    ----------
    signal : numpy array: float
        Contains the signal
    L : Integer
        Contains the size of the number of rows in the construction
        of the Hankel Matrix
        DESCRIPTION.
    N_hankel : Integer
        Contains the number of points in the signal used to construct
        the Hankel Matrix
    tolerance : float
        Contains a number related to the threshold. The threshold is linear
        with respecto to this parameter
    and_or : Boolean
        Contains a boolean used to determing the anomaly.
        Two different passing try to capture the anomaly on the signal.
        Using AND return the point as an anomaly if both passing
        clasify it as anomaly. Using OR return the point as an anomaly 
        if only one passing clasify it as an anomaly

    Returns
    -------
    rest: A tuple containing the information:
        d: numpy array: boolean
            Contains the points that are measured as anomalies
        di: numpy array: integer
            Constains the index of the detected anomalies in the signal
        y: numpy array: float
            Contains values of the anomalies the signal 
            shifted with mean = 0 and containas NaN where it is not
            identified as an anomaly
        x0: numpy array: float
            Contains the signal with shifted with mean = 0 
        xm: float
            The mean of the signal
    """
    
    
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
    
    return(d,di,y,x0,xm)