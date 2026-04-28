import csv
from datetime import datetime
import os

def log(payload, result):
    file_path = "results.csv"

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        # write header once
        if not file_exists:
            writer.writerow(["Timestamp", "Payload", "Result", "Severity"])

        writer.writerow([
            datetime.now(),
            payload,
            result,
            "HIGH" if "Flaw" in result or "Crash" in result or "Detected" in result else "LOW"
        ])