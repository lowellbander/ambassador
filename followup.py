import smtplib
import settings

def main():
    print "hello world"
    sender = "lowellbander@gmail.com"
    recipient = "lowellbander@gmail.com"
    body =  "howdy"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
    server.sendmail(sender, recipient, body)


if __name__ == "__main__":
    main()
