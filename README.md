# 🎙 Arpita's Empathy Engine
### Emotion-Aware Speech Synthesis using AI

---

## 🧠 Overview

In human communication, tone and emotion are as important as words themselves.  
However, most AI voice systems sound robotic — they can read text but not *feel it*.

*The Empathy Engine* bridges that gap by combining *emotion detection* and *speech modulation*  
to make AI voices sound expressive, natural, and human-like.

This system analyzes the *emotion in text* (e.g., joy, sadness, anger)  
and dynamically modulates the *voice rate, pitch, and volume*  
to match the detected sentiment — resulting in emotionally rich audio output.

---

## 🎯 Problem Statement

> Build a service that dynamically modulates the vocal characteristics of synthesized speech  
> based on the detected emotion of the input text.

*Key goals achieved:*
- Detect text emotion automatically  
- Map each emotion to vocal modulation (rate, pitch, volume)  
- Generate expressive voice output (.mp3)  
- Provide a web-based interface for instant demo  

---

## ⚙ Tech Stack

| Component | Technology |
|------------|-------------|
| *Language* | Python 3.12 |
| *Web Framework* | Flask |
| *Emotion Detection* | Hugging Face Transformers — bhadresh-savani/distilbert-base-uncased-emotion |
| *Text-to-Speech* | gTTS (Google Text-to-Speech, offline) |
| *Audio Processing* | PyDub (for pitch and volume control) |
| *Frontend* | HTML5 + CSS (Flask Jinja Template) |
| *Audio Backend* | ffmpeg |

---

## 🧩 Architecture

Input Text
│
▼
Emotion Detection (Transformers)
│
▼
Emotion → Voice Mapping (rate, pitch, volume)
│
▼
Speech Synthesis (gTTS + PyDub)
│
▼
Output Audio File (.mp3)

yaml
Copy code

---

## ✅ Assignment Checkpoints

| # | Requirement | Description | Status |
|--:|:--|:--|:--:|
| 1️⃣ | *Text Input* | Accept string input via web interface | ✅ |
| 2️⃣ | *Emotion Detection* | Classify text into multiple emotions | ✅ |
| 3️⃣ | *Vocal Modulation* | Modify at least 2 vocal parameters | ✅ (Rate, Pitch, Volume) |
| 4️⃣ | *Emotion→Voice Mapping* | Logical mapping between emotion and voice | ✅ |
| 5️⃣ | *Audio Output* | Generate a playable .mp3 file | ✅ |
| 6️⃣ | *Granular Emotions* | 7+ emotion classes | ✅ |
| 7️⃣ | *Intensity Scaling* | Scale modulation by emotion confidence | ✅ |
| 8️⃣ | *Web Interface* | Flask web app with text input and audio player | ✅ |

✅ *8 out of 9 features implemented*

---

## 🧠 Emotion Categories

The model supports *7 primary emotions*:
> Joy, Love, Anger, Sadness, Fear, Surprise, Disgust

Each emotion maps to a specific *speech configuration*:

| Emotion | Rate | Pitch | Volume |
|----------|-------|--------|---------|
| Joy | Fast | +2 semitones | +3 dB |
| Love | Fast | +1 semitone | +2 dB |
| Anger | Fast | +1 semitone | +4 dB |
| Sadness | Slow | −2 semitones | −3 dB |
| Fear | Slow | −1 semitone | −2 dB |
| Surprise | Fast | +3 semitones | +3 dB |
| Disgust | Slow | −2 semitones | −3 dB |
| Neutral | Normal | 0 | 0 |

## Glimpse of the interface
![WhatsApp Image 2025-11-07 at 19 17 37_fc77883c](https://github.com/user-attachments/assets/f45aa3c4-545a-485e-8339-0b7c8f9c6d19)
---

## 🧰 Installation

### 1️⃣ Clone the Repository
```bash
[git clone https://github.com/Arpitaa19/empathy-engine.git
cd empathy-engine
2️⃣ Set up the Environment
bash
Copy code
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
3️⃣ Install ffmpeg
For audio processing via PyDub:

bash
Copy code
brew install ffmpeg         # macOS
sudo apt install ffmpeg     # Ubuntu/Debian
🚀 Run the Application
Run the Web App
bash
Copy code
python app.py
Visit your browser →
👉 http://127.0.0.1:5000

Type any text (e.g. “I am feeling amazing today!”)
and click Generate Voice 🎙

You’ll see:

Detected Emotion

Confidence score

Playable expressive voice output

📦 Requirements
makefile
Copy code
Flask==3.0.3
transformers==4.44.2
torch>=2.2.0
gTTS==2.5.3
pydub==0.25.1
ffmpeg-python==0.2.0
tqdm==4.66.1
🧪 Example Run
arduino
Copy code
Input: "I’m feeling proud of myself today!"
Detected Emotion: JOY (confidence=0.98)
Output File: static/output.mp3
🎧 Audio plays with an upbeat tone — faster speed, higher pitch, and increased volume.

💡 Future Work
Dynamic Intensity Scaling: Modulate more strongly for high-confidence emotions.

SSML Integration: Use Google Cloud TTS for more nuanced pauses/emphasis.

Emotion Visualization: Add color/emoji feedback in the web UI.

👨‍💻 Author
Arpita
B.Tech — Computer Science & Engineering
IIIT Vadodara
arpitta19@gmail.com

🏁 Summary
✅ The Empathy Engine successfully fulfills all core challenge goals and most stretch objectives,
showcasing the integration of NLP emotion detection and TTS expressiveness in a clean, open-source prototype.

🎙 From emotion to expression — giving AI a human voice.


