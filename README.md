# 🗣️ Text-to-Speech Converter Using Python

## 📌 Project Overview

The **Text-to-Speech Converter** is a simple Python application that converts written text into spoken audio.

The project uses the **Google Text-to-Speech (gTTS)** library to convert text into an MP3 audio file. After generating the audio, the program automatically opens the file using the default media player on Windows.

This project demonstrates the basic concept of **Speech Technology and Text-to-Speech (TTS)** using Python.

---

## 🎯 Objectives

* Convert written text into spoken audio.
* Generate an MP3 audio file from text.
* Automatically play the generated audio.
* Demonstrate the use of the `gTTS` Python library.
* Understand the basic working of Text-to-Speech systems.

---

## 🧠 AI Concept

The project demonstrates **Text-to-Speech (TTS)** technology.

The basic process is:

```text
Text Input
    ↓
Text-to-Speech Processing
    ↓
Speech Generation
    ↓
MP3 Audio File
    ↓
Voice Output
```

Text-to-Speech technology is used in applications such as:

* Voice assistants
* Accessibility tools
* Educational applications
* Navigation systems
* Automated announcements
* Reading applications

---

## 🛠️ Technologies Used

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Programming language        |
| gTTS       | Text-to-Speech conversion   |
| OS module  | Opening the generated audio |
| MP3        | Audio output format         |

---

## 📦 Required Library

Install the `gTTS` library using:

```bash
pip install gTTS
```

The `os` module is built into Python, so it does not require separate installation.

---

## 💻 Source Code

```python
import os
from gtts import gTTS

text = ("Hi this is Chandrakala, how are you?")

tts = gTTS(text=text, lang='en')

tts.save("test.mp3")

print("Audio saved")

os.system("start test.mp3")
```

---

## ⚙️ How the Program Works

### 1. Import Libraries

```python
import os
from gtts import gTTS
```

The `gTTS` library is used to convert text into speech.

The `os` module is used to open the generated audio file.

### 2. Provide Text

```python
text = ("Hi this is Chandrakala, how are you?")
```

The text that needs to be converted into speech is stored in the `text` variable.

### 3. Convert Text to Speech

```python
tts = gTTS(text=text, lang='en')
```

The `gTTS` function converts the text into spoken audio.

`lang='en'` specifies English as the language.

### 4. Save Audio

```python
tts.save("test.mp3")
```

The generated speech is saved as an MP3 file named:

```text
test.mp3
```

### 5. Play Audio

```python
os.system("start test.mp3")
```

This command opens the generated MP3 file using the default media player on Windows.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install gTTS

Open the VS Code terminal or Command Prompt and run:

```bash
pip install gTTS
```

### Step 3: Create Python File

Create a file named:

```text
text_to_speech.py
```

### Step 4: Add the Code

Copy the source
