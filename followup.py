import smtplib
import settings

def main():
    sender = "lowellbander@gmail.com"
    recipient = "lowellbander@gmail.com"
    subject = "Engineering Tour Follow-Up 123"
    body =  """Dear ____,\n\nHow was the tour?\n\nSincerely,\nThe UCLA Engineering Ambassador Program"""
    message = 'Subject: %s\n\n%s' % (subject, body)

    print "Connecting to server ... ",
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print "done."
    print "Starting TLS ...",
    server.starttls()
    print "done."
    print "Authenticating ...",
    server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
    print "done."
    print "Sending ... ",
    server.sendmail(sender, recipient, message)
    print "Sent!"


if __name__ == "__main__":
    main()
