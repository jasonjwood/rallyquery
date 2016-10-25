class SendMail:
    smtp_user = ''
    smtp_pwd = ''
    smtp_server = ''
    smtp_port = ''

    def __init__(self, smtp_user, smtp_pwd, smtp_server, smtp_port):
        self.smtp_user = smtp_user
        self.smtp_pwd = smtp_pwd
        self.smtp_port = smtp_port
        self.smtp_server = smtp_server

    def sendmail(self, _to, _from, subject, body):
        import smtplib
        from email.mime.text import MIMEText

        # The sendmail function does most of the work in this example

        # Set SMTP_SERVER and SMTP_PORT. There should be no reason to change
        # these variables unless you prefer to use the SMTPS service running
        # on port 465 of ssrs.reachmail.net. If you do use that service, make
        # sure to remove the session.starttls and second session.ehlo lines
        # below
        SMTP_SERVER = self.smtp_server
        SMTP_PORT = self.smtp_port

        # Attempt to connect and send the message. If using the SMTPS service
        # on port 465, omit the session.starttls() and second
        # session.ehlo()
        try:
            # Start the session
            session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            # Introduce ourselves and login
            session.ehlo()
            session.starttls() # Omit if SMTPS
            session.ehlo() # Omit if SMTPS
            session.login(self.smtp_user, self.smtp_pwd)

            # Create a text/plain message
            msg = MIMEText(body)

            msg['Subject'] = subject
            msg['From'] = 'jason.wood@d2l.com'
            msg['To'] = 'jason.wood@d2l.com'

            print msg.as_string()

            # Send the message and quit
            session.sendmail(_from, _to, msg.as_string())
            session.quit()

            print "Message sent!"
        except Exception, e:
            # Handle any errors
            print "SMTP ERROR: %s" % e

        return True
