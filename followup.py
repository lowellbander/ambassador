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
    subject = "UCLA Engineering Tour Follow-Up"
    body = "Dear %s,\n\n" % family['name']
    body += "We hope you enjoyed your tour of the UCLA Henry Samueli School of Engineering and Applied Science.\n\n"
    body += "If you'd like, you can use the follow link to gives us feedback:\n\n"
    body += settings.FOLLOWUP_URL + family['id'] + '\n\n'
    body += "Sincerely,\nThe UCLA Engineering Ambassador Program"
    message = 'Subject: %s\n\n%s' % (subject, body)

    print "Sending ... ",
    server.sendmail(sender, recipient, message)
    print "Sent!"

def main():
    tours = [family for family in get_all() if "2014-08-01" in str(family['date'])]
    for family in tours:
        send(family)
        return

if __name__ == "__main__":
    main()
