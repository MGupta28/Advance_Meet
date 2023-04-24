import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
   
fromaddr = "divyanshsharma1802@gmail.com"
toaddr = "hriday311203@gmail.com"

print("sending mail to: " + toaddr)

text = str(sys.argv[1])

# instance of MIMEMultipart
msg = MIMEMultipart()
  
# storing the senders email address  
msg['From'] = fromaddr
  
# storing the receivers email address 
msg['To'] = toaddr
  
# storing the subject 
msg['Subject'] = "Report"
  
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