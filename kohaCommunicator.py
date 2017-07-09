#!/usr/bin/env python3
#Program to communicate with a koha server using SIP2 protocol

import socket
from encryptor import Encryptor

class communicator:

    def __init__(self):
        
        self.carriageReturn = chr(13)
        self._data = Encryptor.getData(Encryptor())

    def sipConnect(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.sock.connect((self._data['kohaServerIP'],self._data['kohaServerPort']))
            return True
        except TimeoutError:
            print("Connection timed out\n")
            return False
        except OSError:
            pass

    def sipDisconnect(self):
        try:
            del self.sock
        except AttributeError:
            pass

    def sipLogin(self):
        loginCommand = '9300CN'+self._data['kohaUserName']+"|CO"+self._data['kohaPassword']+"|"+self._data['kohaLocation']+self.carriageReturn
        try:
            self.sock.send(loginCommand.encode())
            data = self.sock.recv(4096)
            if data.decode('utf-8').strip() == '941':
                pass
            else:
                print('SIPLogin failed')
        except socket.error as e:
            print(str(e))


    def sipGetBookStatus(self,bookID):

        bsearchCommand = '1720060110     215612AOMPTCL|AB'+str(bookID)+"|"+self.carriageReturn
        try:
            self.sock.send(bsearchCommand.encode())
            bookData = self.sock.recv(4096).decode('utf-8')
            bookDataArray = bookData.split('|')
            if(len(bookDataArray)>3):
                if(bookDataArray[0][2:4]=='03'):
                    issued = False
                    bookName = bookDataArray[1][2:]
                elif(bookDataArray[0][2:4] == '04'):
                    issued = True
                    bookName = bookDataArray[1][2:]
                else:
                    issued = 'Invalid Book'
                    bookName = 'Invalid'
            else:
                issued = 'Invalid Book'
                bookName = 'Invalid'
        except socket.error as e:
            print(str(e))
            return {'IssueStatus':'Invalid Book','BookName':'Invalid'}

        return {'IssueStatus':issued,
                'BookName':bookName
                }





    def sipGetMember(self,memberID):
        self.sipConnect()
        self.sipLogin()
        msearchCommand = '630020060329    201700          AOBR1|AA'+str(memberID)+'|AD'+self._data['kohaPassword']+'|'+self.carriageReturn
        try:
            self.sock.send(msearchCommand.encode())
            memberData = self.sock.recv(4096).decode('utf-8')
            memberDataArray = memberData.split('|')
            if(len(memberDataArray)>3):
                if(memberDataArray[3][2:3]=='N'):
                    member = 'Invalid'
                else:
                    member = memberDataArray[2][2:]
            else:
                return False
        except socket.error as e:
            print(str(e))
        return member
