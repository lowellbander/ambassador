import smtplib
import settings
from api import get_all
from pprint import pprint

print "Connecting ... ",
server = smtplib.SMTP('smtp.gmail.com', 587)
print "done."
print "Starting TLS ...",
server.starttls()
print "done."
print "Authenticating ...",
server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
print "done."

def send(family):
    sender = "lowellbander@gmail.com"
    recipient = "lowellbander@gmail.com"
    subject = "Engineering Tour Follow-Up"
    body =  "Dear %s,\n\nHow was the tour?\n\nSincerely,\nThe UCLA Engineering Ambassador Program" % family['name']
    message = 'Subject: %s\n\n%s' % (subject, body)

    print "Sending ... ",
    server.sendmail(sender, recipient, message)
    print "Sent!"

def main():
    tours = [family for family in get_all() if "2014-08-01" in str(family['date'])]
    for family in tours:
        send(family)

if __name__ == "__main__":
    main()
