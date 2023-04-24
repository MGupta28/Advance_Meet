# Advance_Meet

The required shot and make notes by themselves

Our Idea is to develop a model to create a one-stop solution to encounter all these problems and make teacher's life a bit easier by doing all the redundant tasks for them to let them focus on the important teaching stuff... Our Project constitutes of 3 different modules -

1. Create a camera holder which automatically rotates by detecting the teacher's face in order to keep the teacher in the frame to avoid multiple camera adjustment
2. Develop a screenshot algorithm that detects the hand gestures made by the teacher in order to take screenshots of the desired area of the important stuff written on the whiteboard.
3. Create a python module that takes in the audio input while recording the video and converting it into speech-to-text output. Once the text is created, a speech-to-text algorithm is implemented on it and images taken by the teacher are placed in the appropriate position using Bart-Large-CNN API

```
pip install pyfirmata
sudo apt install python3-pyaudio
pip install nlpcloud
pip install pyttsx3
pip install SpeechRecognition
pip install playsound
pip install libespeak.so.1
sudo apt install espeak
```
