"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides, E. Segura, C. Vargas
For Paper, "A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

from AnomalyDetectorEigH import AnomalyDetectorEigH
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




# Set the parameters with OR
L = 90
N_hankel = 900
tolerance = 1.06
and_or = "OR"


tolIPM = 1e-8
kIterMax = 100
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 2.5697 + 1e-3





rest = AnomalyDetectorIPM(signal = signal,
                          L = L,
                          N_hankel = N_hankel,
                          tolerance = tolerance,
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax,
                          q0 = q0)


#Saving a PNG for the Github repo

save_signal_figure = "../Figures/real_signal_2_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.png".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)


plotAnomalyDetector(signal, rest, figsize = figsize, 
                    save_signal_figure = save_signal_figure)


