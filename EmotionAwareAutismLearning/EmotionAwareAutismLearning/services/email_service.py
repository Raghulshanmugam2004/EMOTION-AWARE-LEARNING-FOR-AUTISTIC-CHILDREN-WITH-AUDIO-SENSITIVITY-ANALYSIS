import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD


def send_report_email(to_email: str, child_name: str, report: dict) -> bool:
    """Send a simple text report email. Returns True on success, False on failure."""
    subject = f"Emotion Learning Report for {child_name}"

    body_lines = [
        f"Emotion Learning Report for {child_name}",
        "",
        f"Total attempts: {report.get('total_attempts', 0)}",
        f"Correct attempts: {report.get('correct_attempts', 0)}",
        f"Accuracy: {report.get('accuracy', 0.0)}%",
        "",
        "Emotion Confusion (detected → answered : count):",
    ]
    confusion = report.get("emotion_confusion", {})
    if confusion:
        for key, count in confusion.items():
            body_lines.append(f"  {key}: {count}")
    else:
        body_lines.append("  No confusion data available yet.")

    body = "\n".join(body_lines)

    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        print("[INFO] Report email sent successfully.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send report email: {e}")
        return False
