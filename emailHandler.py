#!/usr/bin/env python3
#Program to alert the Library about gate events using smtp mail 
import smtplib
from encryptor import Encryptor

class Mailer:
    def __init__(self):
        self._data = Encryptor.getData(Encryptor())
	self._mailServer = 'smtp.gmail.com'
	self._mailServerPort = 587

    def connect(self):
        try:
            self.server = smtplib.SMTP(self._mailServer,self._mailServerPort)
            self.server.starttls()
        except Exception as e:
            print("Failed to connect to email-server")
            print(e)

    def login(self):
        try:
            self.server.login(self._data['emailUsername'],self._data['emailPassword'])
        except Exception as e:
            print('Failed to login to email-account')
            print(e)

    def sendmessage(self,fromaddress,toaddresses,message):
        for to in toaddresses:
            try:
                self.server.sendmail(fromaddress,to,message)
            except:
                print("Sending E-mail alert to "+str(to)+" failed")
