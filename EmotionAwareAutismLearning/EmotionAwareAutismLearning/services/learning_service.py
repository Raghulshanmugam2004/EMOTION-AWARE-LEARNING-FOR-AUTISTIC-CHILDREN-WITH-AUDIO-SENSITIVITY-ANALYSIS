import csv
import os
from datetime import datetime


class LearningService:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["timestamp", "child_name", "detected_emotion", "child_answer"]
                )

    def log_attempt(self, child_name: str, detected_emotion: str, child_answer: str):
        ts = datetime.now().isoformat()
        with open(self.csv_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([ts, child_name, detected_emotion, child_answer])
