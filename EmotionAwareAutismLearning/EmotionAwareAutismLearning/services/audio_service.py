import os
import csv
from datetime import datetime

from config import DATA_DIR, IRRITATION_LOG

AUDIO_UPLOAD_DIR = os.path.join(DATA_DIR, "audio_uploads")
os.makedirs(AUDIO_UPLOAD_DIR, exist_ok=True)


def save_audio_file(file_storage):
    """Save uploaded audio file to the audio_uploads directory."""
    filename = file_storage.filename
    safe_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
    path = os.path.join(AUDIO_UPLOAD_DIR, safe_name)
    file_storage.save(path)
    return path


def log_irritation_result(child_name: str, audio_path: str, observed_emotion: str):
    """Log irritation / emotion response to CSV."""
    if not os.path.exists(IRRITATION_LOG):
        with open(IRRITATION_LOG, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "child_name", "audio_path", "observed_emotion"])

    ts = datetime.now().isoformat()
    with open(IRRITATION_LOG, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([ts, child_name, audio_path, observed_emotion])
