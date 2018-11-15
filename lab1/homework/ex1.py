from gmail import GMail, Message
import datetime
gmail = GMail("spy12a6@gmail.com","cuong11a6")
message = Message("Don xin nghi", to="cuongnh1305.namtien@gmail.com", text="em bi dau bung")
now = datetime.datetime.now().strftime("%H:%M %p")

while True:
    now = datetime.datetime.now().strftime("%I:%M %p")
    if now == "07:00 AM":
        gmail.send(message)