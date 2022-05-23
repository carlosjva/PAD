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


signal = read_csv('../Data/real_signal_1.csv', header = None)
signal = signal.values.reshape(-1)

#For the figures
scaling = 0.65
figsize = (10*scaling, 8*scaling)



# With SVD

# With AND and this parameters

L = 75
N_hankel = 1300
tolerance = 0.43
and_or = "AND"

save_signal_figure = "../Figures/real_signal_1_anomalies_SVD_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)


rest = AnomalyDetectorSVD(signal = signal, 
                          L = L,
                          N_hankel = N_hankel,
                          and_or = and_or,
                          tolerance = tolerance )

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)



# with OR and this parameters

L = 75
N_hankel = 1300
tolerance = 1.06
and_or = "OR"

save_signal_figure = "../Figures/real_signal_1_anomalies_SVD_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)


rest = AnomalyDetectorSVD(signal = signal, 
                          L = L,
                          N_hankel = N_hankel,
                          and_or = and_or,
                          tolerance = tolerance )

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)





# With Eig Hermitian

# With AND and this parameters

L = 75
N_hankel = 1300
tolerance = 0.43
and_or = "AND"

save_signal_figure = "../Figures/real_signal_1_anomalies_EigH_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)


rest = AnomalyDetectorEigH(signal = signal, 
                          L = L,
                          N_hankel = N_hankel,
                          and_or = and_or,
                          tolerance = tolerance)

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)



# with OR and this parameters

L = 75
N_hankel = 1300
tolerance = 1.06
and_or = "OR"

save_signal_figure = "../Figures/real_signal_1_anomalies_EigH_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)


rest = AnomalyDetectorSVD(signal = signal, 
                          L = L,
                          N_hankel = N_hankel,
                          and_or = and_or,
                          tolerance = tolerance)

plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)




# With Inverse Power Method IPM


# Set the parameters and with AND

L = 75
N_hankel = 1300
tolerance = 0.43
and_or = "AND"


tolIPM = 1e-8
kIterMax = 100
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 2313.020907 + 1e-1


save_signal_figure = "../Figures/real_signal_1_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)



rest = AnomalyDetectorIPM(signal = signal, 
                          L = L, 
                          N_hankel = N_hankel,
                          and_or = and_or,
                          tolerance = tolerance, tolIPM = tolIPM, 
                          kIterMax = kIterMax,
                          q0 = q0)


plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)



# With Inverse Power Method IPM

# Set the parameters and with OR

L = 75
N_hankel = 1300
tolerance = 1.10
and_or = "OR"

tolIPM = 1e-8
kIterMax = 100
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 2313.020907 + 1e-1


save_signal_figure = "../Figures/real_signal_1_anomalies_IPM_L={L}_N={N_hankel}_tolerance={tolerance}_AndOR={and_or}.pdf".format(
    L = L,
    N_hankel = N_hankel,
    tolerance = tolerance,
    and_or = and_or)



rest = AnomalyDetectorIPM(signal = signal, 
                          L = L, 
                          N_hankel = N_hankel,
                          and_or = and_or,
                          tolerance = tolerance, tolIPM = tolIPM, 
                          kIterMax = kIterMax, q0 = q0)


plotAnomalyDetector(signal, save_signal_figure, rest, figsize = figsize)


