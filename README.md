# virtual-assistant-desktop 🧠🎙️
A voice-controlled virtual assistant built in Python that can perform various desktop-related tasks such as searching Wikipedia, opening websites, telling the current time, and more. The assistant uses speech recognition and text-to-speech to interact with users in real time.

## 🔧 Features

- Greets the user based on the time of day
- Converts text to speech using `pyttsx3`
- Recognizes speech input with `speech_recognition`
- Searches and speaks results from Wikipedia
- Opens popular websites like:
  - YouTube
  - Google
  - Python.org
  - GitHub
- Tells the current time
- Opens Notepad
- Listens continuously until user says "exit" or "bye"

- ## 🛠️ Technologies Used

- Python 3
- [pyttsx3](https://pypi.org/project/pyttsx3/) – for text-to-speech
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – for capturing and recognizing speech
- [wikipedia](https://pypi.org/project/wikipedia/) – to fetch data from Wikipedia
- Built-in modules: `webbrowser`, `datetime`, `os`

- ## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/sanikabhale88/virtual-assistant-desktop.git
   
2. Navigate to the project directory:
   cd virtual-assistant-desktop
   
4. Install the dependencies:
   pip install pyttsx3 SpeechRecognition wikipedia
   
6. Run the program:
  python assistant.py

📝 Notes
Make sure your microphone is working properly.

Ensure you have an active internet connection (for Google Speech Recognition and Wikipedia).

This script uses the female voice by default (voices[1]), but you can change it in the code.

👩‍💻 Author
Sanika Bhale
