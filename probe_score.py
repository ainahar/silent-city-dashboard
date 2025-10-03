import sys
import pandas as pd

def compute_score(csv_path):
    df = pd.read_csv(csv_path)
    anomalies = len(df)
    services = df['service'].nunique()

    score = anomalies * services
    if score < 5:
        level = "Low"
    elif score < 10:
        level = "Medium"
    else:
        level = "High"
    print(f"Probe suspicion level: {level} (score={score})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python probe_score.py data/mock_incidents.csv")
        sys.exit(1)

    compute_score(sys.argv[1])
