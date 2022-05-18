"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides
For Paper, "On Operator Theory-Based Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

from AnomalyDetectorSVD import AnomalyDetectorSVD
from AnomalyDetectorIPM import AnomalyDetectorIPM
from plotAnomalyDetector import plotAnomalyDetector
from pandas import read_csv



#For the figures
scaling = 0.65
figsize = (10*scaling, 8*scaling)



#Read the signal

signal = read_csv('../Data/real_signal_2.csv', header = None)
signal = signal.values.reshape(-1)

#First with SVD

# Set the parameters with AND
L = 90
N_hankel = 900
tolerance = 0.68
and_or = "AND"


save_signal_figure = "../Figures/real_signal_2_anomalies_SVD_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
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




# Set the parameters with OR
L = 90
N_hankel = 900
tolerance = 1.16
and_or = "OR"


save_signal_figure = "../Figures/real_signal_2_anomalies_SVD_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
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




# Now with Inverse Power Method IPM

# Set the parameters with AND
L = 90
N_hankel = 900
tolerance = 0.50
and_or = "AND"


tolIPM = 1e-8
kIterMax = 100
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 1.6030 + 1e-3 



save_signal_figure = "../Figures/real_signal_2_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)



rest = AnomalyDetectorIPM(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                          tolerance = tolerance,
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax,
                          q0 = q0)

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)




# Set the parameters with OR
L = 90
N_hankel = 900
tolerance = 1.01
and_or = "OR"


tolIPM = 1e-8
kIterMax = 100
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 1.6030 + 1e-3 



save_signal_figure = "../Figures/real_signal_2_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)


rest = AnomalyDetectorIPM(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                          tolerance = tolerance,
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax,
                          q0 = q0)

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)
