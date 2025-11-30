import os
import random

# Placeholder for a real deep learning model (InceptionV3, etc.).
# You can replace this stub with actual Keras/TensorFlow code.

EMOTIONS = ["happy", "sad", "angry", "surprised", "neutral"]


class EmotionModel:
    def __init__(self, model_path: str | None = None):
        self.model_path = model_path or "models/emotion_model.h5"
        self.model = None
        self._load_model_if_available()

    def _load_model_if_available(self):
        if os.path.exists(self.model_path):
            # TODO: Load your actual Keras model here, for example:
            # from tensorflow.keras.models import load_model
            # self.model = load_model(self.model_path)
            print(f"[INFO] Found model file at {self.model_path}. Load your Keras model here.")
        else:
            print("[WARN] No model file found. Using random-emotion stub.")

    def predict_emotion_from_frame(self, frame):
        """Takes an image (numpy array) and returns an emotion label.

        This stub just returns a random emotion. Replace with real inference code.
        """
        # Example if you had a real model:
        # preprocessed = self._preprocess_frame(frame)
        # preds = self.model.predict(preprocessed)
        # label = self._decode_predictions(preds)
        # return label

        return random.choice(EMOTIONS)
