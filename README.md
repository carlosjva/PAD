# PAD
# Projective Anomaly Detection

A toolset of Python programs for anomaly detection on time series signals

## References

Vides, F., Segura, E., Vargas-Aguero, C. (2022) A Subspace Method for Time Series Anomaly Detection in Cyber-Physical Systems. URL:https://arxiv.org/abs/2205.09959


## Usage

We can detect the anomaly using SVD decomposition, Hermitian Eigenvalue Solver, or the Inverse Power Method. This function can be called importing the functions from the codes: `AnomalyDetectorSVD.py`, `AnomalyDetectorEigH.py`,  and 
`InversePowerMethod.py`.

This returns the position where the identified anomalies are. We can plot it with the script `plotAnomalyDetector.py`

Three examples are given on the usage of the PAD with the scripts `example_real_signal_1.py`, `example_real_signal_2.py`, `example_synthetic_signal.py `. 


## Calibration of parameters

We need to set the `L` and `N` to form the Hankel matrix and find a appropiate tolerance to identify the anomaly. A Jupyter notebook is provided with a widget with examples to see how we can tune the parameters on the notebook `anomaly_detector_calibration_widget.ipynb`


## Results

The figure below shows a signal with an anomaly. The figure is produced with the script `example_real_signal_1.py`

![image](https://github.com/carlosjva/PAD/blob/main/Figures/real_signal_1_anomalies_IPM_L%3D75_N%3D1300_tolerance%3D1.1_AndOR%3DOR.png)




The figure below shows another signal with an anomaly. The figure is produced with the script `example_real_signal_2.py`

![image](https://github.com/carlosjva/PAD/blob/main/Figures/real_signal_1_anomalies_IPM_L%3D75_N%3D1300_tolerance%3D1.1_AndOR%3DOR.png)





The figure below shows the effect of choosing different threshold for signal with an anomaly.
The algorithm may not detect anomalies as pass them as normal, or detect normal behavior as anomalies.
The figure is produced with the script `example_different_tolerance.py`

![image](https://github.com/carlosjva/PAD/blob/main/Figures/real_signal_1_different_tolerances_L%3D75_N%3D1300_AndOR%3DOR.png)


