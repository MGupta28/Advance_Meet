import speech_recognition as sr
import pyttsx3
import nlpcloud
from time import sleep
import re
from playsound import playsound


class Audio_Handler:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.speech_text = ''
        self.speech_to_text()

    def SpeakText(self, command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    def StartTeachIT(self):
        print("\n \n \n ")
        print("Hi, Welcome to Teach it. Your Personal Teaching assistant \n ")
        print("- Starting Recording \n ")
        print("- Please Say Finish Lecture to stop recording \n ")
        self.SpeakText("Hi, Welcome to Teach it. Your Personal Teaching assistant")
        sleep(0.7)
        self.SpeakText("Starting recording")
        sleep(0.7)
        self.SpeakText("Please Say Finish Lecture to stop recording")
        #print("\n \n Please wait, Recording from File...\n ")
        #self.SpeakText("Playing test audio file")
        #sleep(0.7)
        #self.SpeakText("Recording from file")


    def speech_to_text(self):

        i = 0

        #self.StartTeachIT()

        self.text_file = open("sample.html", "w")
        #playsound('test2.wav')

        #sleep(0.7)
        #self.SpeakText("Recording finished, initiating speech to text")
        #print("Recording finished, Please wait initiating speech to text...")

        while (1):
            try:
                with sr.Microphone() as source2:
                #with sr.AudioFile('test2.wav') as source2:
                
                    self.recognizer.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = self.recognizer.listen(source2)

                    if i == 0:
                        self.StartTeachIT()
                    i = i+1
                        
                    MyText = self.recognizer.recognize_google(audio2)

                    MyText = str(MyText.lower()) + '.'
                    print(MyText)
                    self.speech_text = self.speech_text + ' ' + MyText

                    if 'lecture finished.' in self.speech_text:
                        self.SpeakText(" Lecture Finished ")
                        print("\n************************************\n")
                        print("Lecture Finished !!!\n")
                        print("************************************\n")

                        self.text_file.write(self.speech_text)
                        self.text_file.close()

                        self.SpeakText(" Summarizing Text ")
                        print("...Summarizing Text...\n")

                        self.Summarize_text(self.speech_text)
                        break

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("...")

    def Summarize_text(self, text):
        client = nlpcloud.Client("bart-large-cnn", "5a765a6d4986fabc780213295cfdaad94d9f313e")
        summarrized_text = client.summarization(f"""{text}""")
        self.SpeakText(" Here's the Summarized Text ")
        print("<-------Summarized Text-------->\n")
        pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')
        final_text = re.sub(pat,'.\n\n--> ',str(summarrized_text))
        final_text = final_text.replace("{'summary_text': '", "")
        final_text = final_text.replace("'}", "")
        print("--> " + final_text)
        self.summarized_text_file = open("summarized_text.txt", "w")
        self.summarized_text_file.write(str(final_text))


Handler = Audio_Handler()
