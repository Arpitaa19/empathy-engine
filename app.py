from flask import Flask, render_template, request, send_from_directory
from main import load_emotion_model, get_emotion, synthesize_speech
import os
import time

app = Flask(__name__)
clf = load_emotion_model()  # Load model once on startup

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    detected_emotion = None
    confidence = None

    if request.method == "POST":
        text_input = request.form["text"]
        if text_input.strip():
            start = time.time()

            # Detect emotion
            emotion, score = get_emotion(text_input, clf)
            detected_emotion = emotion.upper()
            confidence = f"{score:.2f}"

            # Generate expressive speech
            output_path = os.path.join("static", "output.mp3")
            synthesize_speech(text_input, emotion, output_path)

            print(f"✅ Generated in {time.time() - start:.2f}s: {output_path}")
            audio_file = "output.mp3"

    return render_template(
        "index.html",
        audio_file=audio_file,
        detected_emotion=detected_emotion,
        confidence=confidence
    )

@app.route("/static/<path:filename>")
def serve_audio(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
