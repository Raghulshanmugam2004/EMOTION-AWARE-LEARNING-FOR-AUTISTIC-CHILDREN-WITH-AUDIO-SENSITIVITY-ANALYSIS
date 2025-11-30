import cv2

def gen_camera_stream(emotion_model):
    """Generator function that yields video frames for MJPEG streaming.

    For simplicity, we do *not* draw the emotion label on the frame here.
    You can extend this to overlay text or emojis.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Here you could call:
        # emotion = emotion_model.predict_emotion_from_frame(frame)
        # and draw the label on the frame using cv2.putText.

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
        )
