# Anomaly-in-numbers
An automated Python tool for sliding-window anomaly detection in nitrate time-series data with dynamic baseline thresholding and ground-truth evaluation.
             Featurres
Dynamic Column Selection: Automatically detects nitrate/NO3 measurement columns and anomaly ground-truth columns.

Sliding Window Percentile Threshold: Computes localized percentile thresholds over a rolling window to account for shifting baselines in time-series data.

Performance Evaluation: Calculates True Positives (TP), False Positives (FP), False Negatives (FN), True Negatives (TN), and detection accuracy for both normal and anomaly events.

Visualization: Generates and exports a plot (anomaly_plot.png) displaying the nitrate time series with highlighted anomaly points.
       🛠️  Prerequisites
 Bash
python -m pip install numpy pandas matplotlib
      📁 File Structure
      C:\Anomaly\
├── AG_NO3_fill_cells_remove_NAN.csv   # Input dataset
├── anomaly_detection.py               # Main Python script
├── anomaly_plot.png                   # Output plot (generated on run)
└── README.md                          # Project documentation
     🚀 How to Run
Open your terminal or PowerShell and navigate to your project directory:

PowerShell
cd C:\Anomaly
Run the script:

PowerShell
python anomaly_detection.py
     ⚙️ Configuration & Parameters
Pythonrun_anomaly_detection(
    csv_path="AG_NO3_fill_cells_remove_NAN.csv", 
    window_size=1000,    # Size of the sliding window (W)
    q_percentile=98.5    # Percentile threshold cutoff (q)
)
ParameterTypeDefaultDescriptioncsv_pathstr"AG_NO3_fill_cells_remove_NAN.csv"Path to the target CSV filewindow_sizeint1000Number of samples included in each sliding windowq_percentilefloat98.5
      📊 Sample Output
Upon execution, the script prints confusion matrix metrics directly to the console:

Plaintext
--- Results (W=1000, q=98.5) ---
TP: 120 | FP: 15 | FN: 21 | TN: 4800
Total Anomalies (P): 141 (Expected: 141)
Normal Event Detection Accuracy: 99.69% (Target: >= 80%)
Anomaly Event Detection Accuracy: 85.11% (Target: >= 75%)
