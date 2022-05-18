#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:25:19 2022

@author: kaliche
"""

from AnomalyDetectorSVD import AnomalyDetectorSVD
from AnomalyDetectorIPM import AnomalyDetectorIPM
from plotAnomalyDetector import plotAnomalyDetector
from pandas import read_csv


signal = read_csv('../Data/real_signal_2.csv', header = None)
signal = signal.values.reshape(-1)


L = 90
N_hankel = 900
tolerance = 0.74

from numpy.linalg import svd
from numpy import zeros, where, nan, ones
from statistics import mean,stdev
from scipy.linalg import hankel

x1 = signal.copy()
xm = mean(signal)
x0 = signal - xm


H = hankel(x0[:L],x0[(L-1):N_hankel])
u,s,v = svd(H,full_matrices=0)
sigma_min = s[-1]
