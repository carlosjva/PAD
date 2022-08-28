"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides, E. Segura, C. Vargas
For Paper, "A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

from AnomalyDetectorIPM import AnomalyDetectorIPM
#from plotAnomalyDetector import plotAnomalyDetector
from matplotlib.pyplot import plot,subplot,grid,tight_layout
from matplotlib.pyplot import figure, savefig
from pandas import read_csv


signal = read_csv('../Data/real_signal_1.csv', header = None)
signal = signal.values.reshape(-1)




L = 75
N_hankel = 1300
#tolerance = 1.10
and_or = "OR"

tolIPM = 1e-8
kIterMax = 100
#This q0 is an approximation to the lowest singular value
#This can be estimated by other methods, but here we use it as known
q0 = 2313.020907 + 1e-1



#Set the different tolerances



tolerance_1 = 4.2
tolerance_2 = 1.10
tolerance_3 = 0.30


scaling = 0.65
figsize = (10*scaling, 8*scaling)



rest_1 = AnomalyDetectorIPM(signal = signal, 
                          L = L, 
                          N_hankel = N_hankel,
                          tolerance = tolerance_1, 
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax, 
                          q0 = q0)


rest_2 = AnomalyDetectorIPM(signal = signal, 
                          L = L, 
                          N_hankel = N_hankel,
                          tolerance = tolerance_2, 
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax, 
                          q0 = q0)


rest_3 = AnomalyDetectorIPM(signal = signal, 
                          L = L, 
                          N_hankel = N_hankel,
                          tolerance = tolerance_3, 
                          and_or = and_or,
                          tolIPM = tolIPM, 
                          kIterMax = kIterMax, 
                          q0 = q0)



(d1,di,y,x0,x1,xm_1) = rest_1
(d2,di,y,x0,x1,xm_2) = rest_2
(d3,di,y,x0,x1,xm_3) = rest_3


## Save to PDF


figure(figsize =figsize)

ax1 = subplot(3,1,1)
plot(signal,'blue')
plot(d1*x0+xm_1,'darkorange')
grid(color='k', linestyle='--', linewidth=0.5)
ax1.set_title('Identified anomalies with tolerance = {:2.2f}'.format(tolerance_1),
              fontsize=12)
tight_layout()



ax2 = subplot(3,1,2)
plot(signal,'blue')
plot(d2*x0+xm_2,'darkorange')
grid(color='k', linestyle='--', linewidth=0.5)
ax2.set_title('Identified anomalies with tolerance = {:2.2f}'.format(tolerance_2), 
              fontsize=12)
tight_layout()


ax3 = subplot(3,1,3)
plot(signal,'blue')
plot(d3*x0+xm_3,'darkorange')
grid(color='k', linestyle='--', linewidth=0.5)
ax3.set_title('Identified anomalies with tolerance = {:2.2f}'.format(tolerance_3), fontsize=12)
tight_layout()

savefig("../Figures/real_signal_1_different_tolerances_L=75_N=1300_AndOR=OR.pdf")
savefig("../Figures/real_signal_1_different_tolerances_L=75_N=1300_AndOR=OR.png")














