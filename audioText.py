import speech_recognition as sr
import pyttsx3
import nlpcloud
from time import sleep
import re
from playsound import playsound
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

SendEmail = ""
FileName = ""

class Audio_Handler:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.speech_text = ''
        self.speech_to_text()
        self.email = str(sys.argv[1])

    def SpeakText(self, command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    def StartTeachIT(self):
        print("\n \n \n ")
        print("Hi, Welcome to Teach it. Your Personal Teaching assistant \n ")
        #print("- Please Say Start Lecture to start recording \n ")
        #print("- Please Say Finish Lecture to stop recording \n ")
        self.SpeakText("Hi, Welcome to Teach it. Your Personal Teaching assistant")
        sleep(0.7)
        #self.SpeakText("Please Say Start Lecture to start recording")
        #sleep(0.7)
        #self.SpeakText("Please Say Finish Lecture to stop recording")
        print("\n \n Please wait, Recording from File...\n ")
        self.SpeakText("Playing test audio file")
        sleep(0.7)
        self.SpeakText("Recording from file")


    def speech_to_text(self):

        i = 0

        self.StartTeachIT()

        self.text_file = open("sample.html", "w")
        #playsound('test2.wav')

        sleep(0.7)
        self.SpeakText("Recording finished, initiating speech to text")
        print("Recording finished, Please wait, initiating speech to text")

        while (1):
            try:
                #with sr.Microphone() as source2:
                with sr.AudioFile(FileName) as source2:
                
                    #self.recognizer.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = self.recognizer.listen(source2)

                    # if i == 0:
                    #     self.StartTeachIT()
                    # i = i+1
                        
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
        client = nlpcloud.Client("bart-large-cnn", "31e639871be97aa659946c27e6e6228931477c54")
        summarrized_text = client.summarization(f"""{text}""")
        self.SpeakText(" Here's the Summarized Text ")
        pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')
        final_text = re.sub(pat,'.\n\n--> ',str(summarrized_text))
        final_text = final_text.replace("{'summary_text': '", "")
        final_text = final_text.replace("'}", "")
        final_text = "      <-------Summarized Text-------->\n\n" + "-->" + final_text + "\n\n"
        print(final_text)
        self.summarized_text_file = open("summarized_text.txt", "w")
        self.summarized_text_file.write(str(final_text))

        text_final = "      <-------Recorded Text-------->\n\n" + self.speech_text + "\n\n\n" + final_text + "\n\n"
        
        if SendEmail:
            self.Mailer(text_final)
        else:
            print("No Email Set")


    def Mailer(self, text):

        fromaddr = "krrishjindal2002@gmail.com"
        toaddr = SendEmail

        mail = "sending mail to: " + toaddr
        self.SpeakText(mail)
        print(mail)
        print("\nMail Sent")

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address  
        msg['From'] = fromaddr

        # storing the receivers email address 
        msg['To'] = toaddr

        # storing the subject 
        msg['Subject'] = "Text report"

        # string to store the body of the mail
        body = "hello this a report"

        # attach the body with the msg instance
        msg.attach(MIMEText(text, 'plain'))

        for i in range(1,4):
        # open the file to be sent 
          filename = "ROI" + str(i) + ".png"
          attachment = open("SnapshotImages/ROI" + str(i) + ".png", "rb")

          # instance of MIMEBase and named as p
          p = MIMEBase('application', 'octet-stream')

          # To change the payload into encoded form
          p.set_payload((attachment).read())

          # encode into base64
          encoders.encode_base64(p)

          p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

          msg.attach(p)
          # attach the instance 'p' to 

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "exxvpjtpcatnauit")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()

SendEmail = str(sys.argv[1])
FileName = str(sys.argv[2])
if SendEmail:
    print("email: " + SendEmail)
    Handler = Audio_Handler()
else:
    print("No email set")
