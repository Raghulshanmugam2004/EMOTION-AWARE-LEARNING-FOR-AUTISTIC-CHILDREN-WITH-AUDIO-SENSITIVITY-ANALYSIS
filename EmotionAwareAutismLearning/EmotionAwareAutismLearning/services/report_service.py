import csv
import os
from collections import Counter


def generate_child_report(csv_path: str, child_name: str):
    """Generate simple statistics for the given child from the CSV log.

    Returns a dict with:
    - total_attempts
    - correct_attempts
    - accuracy
    - emotion_confusion (how often each detected emotion is misclassified)
    """
    if not os.path.exists(csv_path):
        return {
            "total_attempts": 0,
            "correct_attempts": 0,
            "accuracy": 0.0,
            "emotion_confusion": {},
        }

    total = 0
    correct = 0
    confusion = Counter()

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["child_name"] != child_name:
                continue
            total += 1
            detected = row["detected_emotion"]
            answer = row["child_answer"]
            if detected.strip().lower() == answer.strip().lower():
                correct += 1
            else:
                confusion[(detected, answer)] += 1

    accuracy = (correct / total) * 100 if total > 0 else 0.0
    confusion_dict = {
        f"{d} → {a}": c for (d, a), c in confusion.items()
    }

    return {
        "total_attempts": total,
        "correct_attempts": correct,
        "accuracy": round(accuracy, 2),
        "emotion_confusion": confusion_dict,
    }
