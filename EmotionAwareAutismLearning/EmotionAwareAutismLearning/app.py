from flask import Flask, render_template, Response, request, redirect, url_for, flash
import os
from config import (
    DATA_DIR,
    CHILD_RESPONSE_LOG,
    IRRITATION_LOG,
)
from models.emotion_model import EmotionModel
from services.camera_service import gen_camera_stream
from services.learning_service import LearningService
from services.report_service import generate_child_report
from services.email_service import send_report_email
from services.audio_service import save_audio_file, log_irritation_result

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Initialize services
emotion_model = EmotionModel()
learning_service = LearningService(CHILD_RESPONSE_LOG)

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)


@app.route("/")
def index():
    """Landing page: Parent dashboard."""
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    """Video streaming route for webcam."""
    return Response(
        gen_camera_stream(emotion_model),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


@app.route("/child-learning", methods=["GET", "POST"])
def child_learning():
    """Child learning page – shows emoji and records child answer."""
    if request.method == "POST":
        detected_emotion = request.form.get("detected_emotion")
        child_answer = request.form.get("child_answer")
        child_name = request.form.get("child_name", "Unknown Child")

        learning_service.log_attempt(child_name, detected_emotion, child_answer)
        flash("Response recorded!", "success")
        return redirect(url_for("child_learning"))

    # For demo: we just pick a dummy emotion label here.
    # In a real system, this can be passed from the parent detection screen.
    sample_emotion = "happy"
    return render_template("child_learning.html", emotion=sample_emotion)


@app.route("/upload-audio", methods=["GET", "POST"])
def upload_audio():
    if request.method == "POST":
        file = request.files.get("audio_file")
        child_name = request.form.get("child_name", "Unknown Child")
        observed_emotion = request.form.get("observed_emotion", "neutral")

        if not file or file.filename == "":
            flash("Please select an audio file.", "danger")
            return redirect(url_for("upload_audio"))

        saved_path = save_audio_file(file)
        log_irritation_result(child_name, saved_path, observed_emotion)
        flash("Audio uploaded and irritation response recorded.", "success")
        return redirect(url_for("upload_audio"))

    return render_template("upload_audio.html")


@app.route("/report")
def report():
    child_name = request.args.get("child_name", "Unknown Child")
    report_stats = generate_child_report(CHILD_RESPONSE_LOG, child_name)
    return render_template("report.html", child_name=child_name, report=report_stats)


@app.route("/send-report", methods=["POST"])
def send_report():
    child_name = request.form.get("child_name", "Unknown Child")
    parent_email = request.form.get("parent_email")

    report_stats = generate_child_report(CHILD_RESPONSE_LOG, child_name)
    if not parent_email:
        flash("Parent email is required", "danger")
        return redirect(url_for("report", child_name=child_name))

    ok = send_report_email(parent_email, child_name, report_stats)
    if ok:
        flash("Report emailed successfully!", "success")
    else:
        flash("Failed to send email. Check email configuration.", "danger")

    return redirect(url_for("report", child_name=child_name))


if __name__ == "__main__":
    app.run(debug=True)
