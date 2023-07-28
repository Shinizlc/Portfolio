import smtplib
def send_mail():
    SERVER = "localhost"
    FROM = "aleksei.semerikov@ringcentral.com"
    TO = ["aleksei.semerikov@ringcentral.com", "dmitry.savchenko@ringcentral.com"]
    SUBJECT = "Job JOB$_MESSAGES_DELETE status"
    text = "This message was sent with Python's smtplib."

    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, text)

    server = smtplib.SMTP(SERVER)
    # server.set_debuglevel(3)
    server.sendmail(FROM, TO, message)
    server.quit()
