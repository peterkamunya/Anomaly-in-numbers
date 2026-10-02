import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_anomaly_detection(csv_path, window_size=1000, q_percentile=98.5):
    # 1. Load Data
    df = pd.read_csv(csv_path)
    
    
    nitrate_col = [c for c in df.columns if 'Nitrate' in c or 'NO3' in c][0]
    ground_truth_col = 'Student_Flag'

    
    data = df[nitrate_col].values
    actual_anomalies = df[ground_truth_col].values  
    
    n_samples = len(data)
    predictions = np.zeros(n_samples, dtype=int)
    
    W = window_size
    q = q_percentile
    
   
    window_1 = data[0:W]
    T1 = np.percentile(window_1, q, method="linear")
    
    
    for idx in range(W):
        if data[idx] >= T1:
            predictions[idx] = 1
            
   
    for i in range(2, n_samples - W + 2):
        window_start = i - 1
        window_end = i + W - 2
        
        current_window = data[window_start:window_end]
        Ti = np.percentile(current_window, q, method="linear")
        
        new_point_idx = window_end - 1
        if new_point_idx < n_samples:
            if data[new_point_idx] >= Ti:
                predictions[new_point_idx] = 1

    # 4. Calculate Confusion Matrix Metrics
    TP = np.sum((predictions == 1) & (actual_anomalies == 1))
    FP = np.sum((predictions == 1) & (actual_anomalies == 0))
    FN = np.sum((predictions == 0) & (actual_anomalies == 1))
    TN = np.sum((predictions == 0) & (actual_anomalies == 0))
    
    P = TP + FN  # Total Actual Anomalies (Target: 141)
    N = TN + FP  # Total Actual Normals
    
    normal_acc = (TN / N) * 100
    anomaly_acc = (TP / P) * 100
    
    # Printing the results 9
    print(f"--- Results (W={W}, q={q}) ---")
    print(f"TP: {TP} | FP: {FP} | FN: {FN} | TN: {TN}")
    print(f"Total Anomalies (P): {P} (Expected: 141)")
    print(f"Normal Event Detection Accuracy: {normal_acc:.2f}% (Target: >= 80%)")
    print(f"Anomaly Event Detection Accuracy: {anomaly_acc:.2f}% (Target: >= 75%)")
    
   
    plt.figure(figsize=(14, 6))
    plt.plot(data, label='Nitrate Level', color='lightblue', alpha=0.7)
    
   
    anomaly_indices = np.where(predictions == 1)[0]
    plt.scatter(anomaly_indices, data[anomaly_indices], color='red', label='Detected Anomaly', s=15, zorder=5)
    
    plt.title(f"Sliding Window Anomaly Detection (W={W}, q={q})")
    plt.xlabel("Index / Time Step")
    plt.ylabel("Nitrate Value")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("anomaly_plot.png")
    plt.show()

if __name__ == "__main__":
    run_anomaly_detection("AG_NO3_fill_cells_remove_NAN.csv", window_size=1000, q_percentile=98.5)