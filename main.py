import argparse
import time
from transformers import pipeline
from gtts import gTTS
from pydub import AudioSegment
import os

def load_emotion_model():
    """
    Load the Hugging Face emotion classification pipeline.
    Model: bhadresh-savani/distilbert-base-uncased-emotion
    (Downloads once, then cached locally for instant reuse)
    """
    model_name = "bhadresh-savani/distilbert-base-uncased-emotion"
    clf = pipeline("text-classification", model=model_name, top_k=1)
    return clf

def get_emotion(text, clf):
    """
    Detect emotion from text using pretrained model.
    Returns (emotion_label, confidence_score)
    """
    preds = clf(text)
    if isinstance(preds, list) and len(preds) > 0:
        res = preds[0]
        if isinstance(res, list):  # for pipelines returning nested lists
            res = res[0]
        return res['label'].lower(), res['score']
    return "neutral", 0.0

def emotion_to_voice_config(emotion):
    """
    Map model emotion labels to speech synthesis parameters.
    """
    configs = {
        "joy":       {"slow": False, "pitch_shift": 2,  "volume_db": 3},
        "love":      {"slow": False, "pitch_shift": 1,  "volume_db": 2},
        "anger":     {"slow": False, "pitch_shift": 1,  "volume_db": 4},
        "sadness":   {"slow": True,  "pitch_shift": -2, "volume_db": -3},
        "fear":      {"slow": True,  "pitch_shift": -1, "volume_db": -2},
        "surprise":  {"slow": False, "pitch_shift": 3,  "volume_db": 3},
        "disgust":   {"slow": True,  "pitch_shift": -2, "volume_db": -3},
        "neutral":   {"slow": False, "pitch_shift": 0,  "volume_db": 0},
    }
    return configs.get(emotion, configs["neutral"])

def synthesize_speech(text, emotion, out_path):
    """
    Generate expressive speech using gTTS for rate control,
    and PyDub for pitch + volume modulation.
    """
    cfg = emotion_to_voice_config(emotion)
    tmp_path = "temp_output.mp3"

    # Step 1: Generate speech with gTTS (rate control)
    tts = gTTS(text=text, lang="en", slow=cfg["slow"])
    tts.save(tmp_path)

    # Step 2: Load audio and apply pitch/volume modulation
    sound = AudioSegment.from_file(tmp_path)

    # Pitch shift (change playback rate)
    if cfg["pitch_shift"] != 0:
        new_frame_rate = int(sound.frame_rate * (2 ** (cfg["pitch_shift"] / 12)))
        sound = sound._spawn(sound.raw_data, overrides={"frame_rate": new_frame_rate})
        sound = sound.set_frame_rate(44100)  # restore to standard sample rate

    # Volume adjustment
    sound = sound + cfg["volume_db"]

    # Step 3: Export final audio
    sound.export(out_path, format="mp3")

    # Clean up temp file
    if os.path.exists(tmp_path):
        os.remove(tmp_path)

def main():
    parser = argparse.ArgumentParser(description="🎙️ The Empathy Engine — Emotion-Aware Text-to-Speech")
    parser.add_argument("--text", type=str, required=True, help="Input text to synthesize")
    parser.add_argument("--out", type=str, default="output.mp3", help="Output audio file name (mp3)")
    args = parser.parse_args()

    start_time = time.time()
    print("🔍 Loading emotion detection model...")
    clf = load_emotion_model()

    print("🧠 Analyzing emotion...")
    emotion, score = get_emotion(args.text, clf)
    print(f"Detected Emotion: {emotion.upper()} (confidence={score:.2f})")

    print("🎤 Generating expressive speech (rate, pitch, volume)...")
    synthesize_speech(args.text, emotion, args.out)

    elapsed = time.time() - start_time
    print(f"✅ Done! File saved as '{args.out}' in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
