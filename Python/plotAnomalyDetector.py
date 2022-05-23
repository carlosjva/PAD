"""
Prototypical Projection Based Anomaly Detector
Code by F. Vides, E. Segura, C. Vargas
For Paper, "A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems"
by F. Vides, E. Segura, C. Vargas
@authors: F. Vides, E. Segura, C. Vargas
"""

def plotAnomalyDetector(signal, save_signal_figure, resto, figsize):
    
    from matplotlib.pyplot import plot,subplot,grid,tight_layout
    from matplotlib.pyplot import figure, savefig, axvspan, show
    
    (d,di,y,x0,x1,xm) = resto
    
    figure(figsize =figsize)
    
    ax1 = subplot(3,1,1)
    
    ax1.set_xlim(0,len(x0)+1)
    
    plot(signal,'blue')
    grid(color='k', linestyle='--', linewidth=0.5)
    ax1.set_title('Signal', fontsize=12)
    
    ax2 = subplot(3,1,2)
    
    #Put this or it doesn't plot the whole region
    ax2.set_xlim(0,len(x0)+1)
    ax2.set_ylim(0,1)
       
   
    for anom in di:
        ax2.axvspan(anom-0.5, anom+0.5, facecolor = "forestgreen", alpha = 1)
    
    #plot(d,'darkorange')
    grid(color='k', linestyle='--', linewidth=0.5)
    ax2.set_title('Identified scanning region', fontsize=12)
    tight_layout()
    
    ax3 = subplot(3,1,3)
    
    ax3.set_xlim(0,len(x0)+1)
    
    for anom in di:
        ax3.axvspan(anom-0.5, anom+0.5, facecolor = "forestgreen", alpha = 1)
    
    plot(signal,'blue')
    #plot(y+xm,'darkorange')
    #plot(d*signal,'darkorange')
    plot(d*x0+xm,'darkorange')
    grid(color='k', linestyle='--', linewidth=0.5)
    ax3.set_title('Identified anomalies', fontsize=12)
    tight_layout()
    savefig(save_signal_figure)
    #show()