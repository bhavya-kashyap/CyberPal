import smtplib
import time
import imaplib
import email
import os
import sys
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

class Read():
    def __init__(self):
        self.username=(sys.argv)[1]
        self.yourPassword=(sys.argv)[2]
        ORG_EMAIL = "@gmail.com"
        FROM_EMAIL = ("{}"+ORG_EMAIL).format(username)
        print FROM_EMAIL
        FROM_PWD = ("{}").format(yourPassword)
        print FROM_PWD
        SMTP_SERVER = "imap.gmail.com"


    def read_email_from_gmail():
        try:
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL,FROM_PWD)
            mail.select('inbox')

            type, data = mail.search(None, 'ALL')
            mail_ids = data[0]

            id_list = mail_ids.split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])


                #for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(latest_email_id, '(RFC822)' )
                #print data

            for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        #print msg
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print('From : ' + email_from + '\n')
                        print('Subject : ' + email_subject + '\n')
                        if msg.is_multipart():
                            for payload in msg.get_payload():
                                # if payload.is_multipart(): ...
                                email_body = str(payload.get_payload())
                                return email_body
                                #print email_body
                        else:
                            print msg.get_payload()

        except Exception, e:
            print str(e)

new_acc = Read()
print new_acc.username
