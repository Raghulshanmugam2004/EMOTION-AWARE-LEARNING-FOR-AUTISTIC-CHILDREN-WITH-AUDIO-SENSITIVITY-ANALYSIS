# Emotion-Aware Learning for Autistic Children with Audio Sensitivity Analysis

This repository contains a reference implementation of the **Emotion-Aware Learning for Autistic Children with Audio Sensitivity Analysis** project. It is a web-based system that:

- Detects **parent emotions** from a live camera feed using a deep learning model (InceptionV3-based stub).
- Shows the detected emotion as an **emoji** to the child.
- Tracks the child's responses over **three attempts** and stores them in a database (simple JSON/CSV storage in this reference implementation).
- Generates a **report** of the child's performance and can email it to the parent (SMTP configuration required).
- Lets parents **upload audio files** and monitors the child's facial expression to detect irritation or discomfort.

> NOTE: The ML model included here is a **placeholder stub**. You must integrate your trained InceptionV3 model for real accuracy.

## Tech Stack

- Backend: Python 3, Flask
- Frontend: HTML, CSS, basic JavaScript
- Deep Learning: Keras / TensorFlow (InceptionV3 placeholder)
- Camera Access: OpenCV
- Email: Python's `smtplib` (needs configuration)


2. Export it as an `.h5` file.
3. Place it in the `models/` folder (e.g. `models/emotion_model.h5`).
4. Update `models/emotion_model.py` to load your actual weights and preprocessing pipeline.

## Disclaimer

This is a **reference academic implementation** created for project/demo and GitHub submission purposes.  
It is **not** medically certified and must not be used as a diagnostic tool.
