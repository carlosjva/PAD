"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides, E. Segura, C. Vargas
For Paper, "A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

from AnomalyDetectorSVD import AnomalyDetectorSVD
from AnomalyDetectorEigH import AnomalyDetectorEigH
from AnomalyDetectorIPM import AnomalyDetectorIPM
from plotAnomalyDetector import plotAnomalyDetector
from pandas import read_csv



#For the figures
scaling = 0.65
figsize = (10*scaling, 8*scaling)

# Read the signal
signal = read_csv('../Data/synthetic_signal.csv', header = None)
signal = signal.values.reshape(-1)



# Using SVD



# Using AND

L = 150
N_hankel = 1200
tolerance = 0.30
and_or = "AND"

save_signal_figure = "../Figures/synthetic_anomalies_SVD_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)

rest = AnomalyDetectorSVD(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                         tolerance = tolerance,
                         and_or = and_or)


plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)


# Using OR

L = 150
N_hankel = 1200
tolerance = 1.2
and_or = "OR"

save_signal_figure = "../Figures/synthetic_anomalies_SVD_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)

rest = AnomalyDetectorSVD(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                         tolerance = tolerance,
                         and_or = and_or)


plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)




# Using with Eig H



# Using AND

L = 150
N_hankel = 1200
tolerance = 0.30
and_or = "AND"

save_signal_figure = "../Figures/synthetic_anomalies_EigH_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)

rest = AnomalyDetectorEigH(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                         tolerance = tolerance,
                         and_or = and_or)


plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)


# Using OR

L = 150
N_hankel = 1200
tolerance = 1.2
and_or = "OR"

save_signal_figure = "../Figures/synthetic_anomalies_EigH_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)

rest = AnomalyDetectorEigH(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                         tolerance = tolerance,
                         and_or = and_or)


plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)




# Using Inverse Power Method IPM


# Using AND

L = 150
N_hankel = 1200
tolerance = 0.27
and_or = "AND"

save_signal_figure = "../Figures/synthetic_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)

tolIPM = 1e-8
kIterMax = 200
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 0.01975 + 1e-5


rest = AnomalyDetectorIPM(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                          tolerance = tolerance,
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax, 
                          q0 = q0)

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)



# Using OR

L = 150
N_hankel = 1200
tolerance = 1.90
and_or = "OR"

save_signal_figure = "../Figures/synthetic_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)

tolIPM = 1e-8
kIterMax = 200
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 0.01975 + 1e-5


rest = AnomalyDetectorIPM(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                          tolerance = tolerance,
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax, 
                          q0 = q0)

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)











