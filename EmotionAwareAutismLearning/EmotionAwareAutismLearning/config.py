import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data paths
DATA_DIR = os.path.join(BASE_DIR, "data")
CHILD_RESPONSE_LOG = os.path.join(DATA_DIR, "child_responses.csv")
IRRITATION_LOG = os.path.join(DATA_DIR, "irritation_log.csv")

# Model paths
MODELS_DIR = os.path.join(BASE_DIR, "models")
EMOTION_MODEL_PATH = os.path.join(MODELS_DIR, "emotion_model.h5")

# Email settings (fill with your values)
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER", "your_email@example.com")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "password")

DEFAULT_PARENT_EMAIL = os.environ.get("PARENT_EMAIL", "parent@example.com")
