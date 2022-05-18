"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides
For Paper, "On Operator Theory-Based Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

from AnomalyDetector import AnomalyDetector
from plotAnomalyDetector import plotAnomalyDetector
from numpy.random import randn
from pandas import read_csv

signal_s = read_csv('../Data/all_synthetic/synthetic_signal_all.csv', header = None)
signal_s = signal_s.values
signal_s = signal_s[1,:]


# Adding the anomaly
P = [1800,3800,5100,10000,12000]
scale = 5e-1
signal_s[P[0]:(P[0]+300)] = signal_s[P[0]:(P[0]+300)] + scale*randn(300)
signal_s[P[1]:(P[1]+300)] = signal_s[P[1]:(P[1]+300)] + scale*randn(300)
signal_s[P[2]:(P[2]+300)] = signal_s[P[2]:(P[2]+300)] + scale*randn(300)
signal_s[P[3]:(P[3]+300)] = signal_s[P[3]:(P[3]+300)] + scale*randn(300)
signal_s[P[4]:(P[4]+300)] = signal_s[P[4]:(P[4]+300)] + scale*randn(300)


L = 300
S = 1200
sensitivity = 1.2


rest_s = AnomalyDetector(signal = signal_s, L = L, S = S, sensitivity= sensitivity )

plotAnomalyDetector(signal_s, rest_s, figsize = (15,8))