#!/usr/bin/env python3
#Program to communicate with Speedway Impinj R420 gate reader using LLRP protocol
#Written by Amruthlal M 
#amruth27m@gmail.com

import socket
from time import sleep
import time

class Communicator:

    def __init__(self):
        self._alaramDuration = 5
        
        self._AntennaPower = 87
        self._gateIP = 'your-ip-here'
        self._gateLLRPPort = 5084

    def _connect(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self._gateIP,self._gateLLRPPort))
            #print('Connection success')
       
    def _disconnect(self):
        closeLLRPCommand = chr(4)+chr(14)+chr(0)+chr(0)+chr(0)+chr(10)+chr(0)+chr(0)+chr(0)+chr(21)
        self.sock.send(closeLLRPCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)
        del self.sock

    def startAlaram(self,duration=1):
        #self._connect()
        self.sock.recv(4096000)
        startCommand = chr(4)+chr(3)+chr(0)+chr(0)+chr(0)+chr(18)+chr(0)+chr(0)+chr(0)+chr(125)+chr(0)+chr(0)+chr(219)+chr(0)+chr(7)+chr(0)+chr(1)+chr(128)
        self.sock.send(startCommand.encode('+latin-1'))
        sleep(duration)
        self.stopAlaram()

    def stopAlaram(self):
        stopCommand = chr(4)+chr(3)+chr(0)+chr(0)+chr(0)+chr(18)+chr(0)+chr(0)+chr(0)+chr(204)+chr(0)+chr(0)+chr(219)+chr(0)+chr(7)+chr(0)+chr(1)+chr(0)
        self.sock.send(stopCommand.encode('latin-1'))
        self.sock.recv(4096000)

    def startReading(self):
    #    self._connect()
        enableExtensionCommand = chr(7)+chr(255)+chr(0)+chr(0)+chr(0)+chr(19)+chr(0)+chr(0)+chr(0)+chr(71)+chr(0)+chr(0)+chr(101)+chr(26)+chr(21)+chr(0)+chr(0)+chr(0)+chr(0)

        setReaderConfigCommand = chr(4)+chr(3)+chr(0)+chr(0)+chr(0)+chr(11)+chr(0)+chr(0)+chr(0)+chr(76)+chr(128)

        deleteROSpecCommand = chr(4)+chr(21)+chr(0)+chr(0)+chr(0)+chr(14)+chr(0)+chr(0)+chr(0)+chr(78)+chr(0)+chr(0)+chr(0)+chr(0)

        deleteAccessSpecCommand = chr(4)+chr(41)+chr(0)+chr(0)+chr(0)+chr(14)+chr(0)+chr(0)+chr(0)+chr(80)+chr(0)+chr(0)+chr(0)+chr(0)

        enableExtensionCommand2 = chr(7)+chr(255)+chr(0)+chr(0)+chr(0)+chr(19)+chr(0)+chr(0)+chr(0)+chr(82)+chr(0)+chr(0)+chr(101)+chr(26)+chr(21)+chr(0)+chr(0)+chr(0)+chr(0)

        setConfigCommand = chr(4)+chr(3)+chr(0)+chr(0)+chr(0)+chr(93)+chr(0)+chr(0)+chr(0)+chr(85)+chr(0)+chr(0)+chr(244)+chr(0)+chr(32)+chr(0)+chr(245)+chr(0)+chr(7)+chr(0)+chr(1)+chr(128)+chr(0)+chr(245)+chr(0)+chr(7)+chr(0)+chr(8)+chr(128)+chr(0)+chr(245)+chr(0)+chr(7)+chr(0)+chr(3)+chr(128)+chr(0)+chr(245)+chr(0)+chr(7)+chr(0)+chr(2)+chr(128)+chr(0)+chr(237)+chr(0)+chr(13)+chr(2)+chr(0)+chr(1)+chr(0)+chr(238)+chr(0)+chr(6)+chr(0)+chr(0)+chr(0)+chr(225)+chr(0)+chr(8)+chr(0)+chr(1)+chr(128)+chr(0)+chr(0)+chr(225)+chr(0)+chr(8)+chr(0)+chr(2)+chr(128)+chr(0)+chr(0)+chr(225)+chr(0)+chr(8)+chr(0)+chr(3)+chr(128)+chr(0)+chr(0)+chr(225)+chr(0)+chr(8)+chr(0)+chr(4)+chr(128)+chr(0)+chr(0)+chr(226)+chr(0)+chr(5)+chr(128)

        addROSpecCommand = chr(4)+chr(20)+chr(0)+chr(0)+chr(1)+chr(65)+chr(0)+chr(0)+chr(0)+chr(87)+chr(0)+chr(177)+chr(1)+chr(55)+chr(0)+chr(0)+chr(55)+chr(70)+chr(0)+chr(0)+chr(0)+chr(178)+chr(0)+chr(18)+chr(0)+chr(179)+chr(0)+chr(5)+chr(1)+chr(0)+chr(182)+chr(0)+chr(9)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(183)+chr(1)+chr(14)+chr(0)+chr(4)+chr(0)+chr(1)+chr(0)+chr(2)+chr(0)+chr(3)+chr(0)+chr(4)+chr(0)+chr(184)+chr(0)+chr(9)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(186)+chr(0)+chr(247)+chr(0)+chr(123)+chr(1)+chr(0)+chr(222)+chr(0)+chr(60)+chr(0)+chr(1)+chr(0)+chr(223)+chr(0)+chr(6)+chr(0)+chr(1)+chr(0)+chr(224)+chr(0)+chr(10)+chr(0)+chr(1)+chr(0)+chr(1)+chr(0)+chr(self._AntennaPower)+chr(1)+chr(74)+chr(0)+chr(38)+chr(0)+chr(1)+chr(79)+chr(0)+chr(8)+chr(3)+chr(232)+chr(0)+chr(0)+chr(1)+chr(80)+chr(0)+chr(11)+chr(128)+chr(0)+chr(32)+chr(0)+chr(0)+chr(0)+chr(0)+chr(3)+chr(255)+chr(0)+chr(14)+chr(0)+chr(0)+chr(101)+chr(26)+chr(0)+chr(0)+chr(0)+chr(23)+chr(0)+chr(2)+chr(0)+chr(222)+chr(0)+chr(60)+chr(0)+chr(2)+chr(0)+chr(223)+chr(0)+chr(6)+chr(0)+chr(1)+chr(0)+chr(224)+chr(0)+chr(10)+chr(0)+chr(1)+chr(0)+chr(1)+chr(0)+chr(self._AntennaPower)+chr(1)+chr(74)+chr(0)+chr(38)+chr(0)+chr(1)+chr(79)+chr(0)+chr(8)+chr(3)+chr(232)+chr(0)+chr(0)+chr(1)+chr(80)+chr(0)+chr(11)+chr(128)+chr(0)+chr(32)+chr(0)+chr(0)+chr(0)+chr(0)+chr(3)+chr(255)+chr(0)+chr(14)+chr(0)+chr(0)+chr(101)+chr(26)+chr(0)+chr(0)+chr(0)+chr(23)+chr(0)+chr(2)+chr(0)+chr(222)+chr(0)+chr(60)+chr(0)+chr(3)+chr(0)+chr(223)+chr(0)+chr(6)+chr(0)+chr(1)+chr(0)+chr(224)+chr(0)+chr(10)+chr(0)+chr(1)+chr(0)+chr(1)+chr(0)+chr(self._AntennaPower)+chr(1)+chr(74)+chr(0)+chr(38)+chr(0)+chr(1)+chr(79)+chr(0)+chr(8)+chr(3)+chr(232)+chr(0)+chr(0)+chr(1)+chr(80)+chr(0)+chr(11)+chr(128)+chr(0)+chr(32)+chr(0)+chr(0)+chr(0)+chr(0)+chr(3)+chr(255)+chr(0)+chr(14)+chr(0)+chr(0)+chr(101)+chr(26)+chr(0)+chr(0)+chr(0)+chr(23)+chr(0)+chr(2)+chr(0)+chr(222)+chr(0)+chr(60)+chr(0)+chr(4)+chr(0)+chr(223)+chr(0)+chr(6)+chr(0)+chr(1)+chr(0)+chr(224)+chr(0)+chr(10)+chr(0)+chr(1)+chr(0)+chr(1)+chr(0)+chr(self._AntennaPower)+chr(1)+chr(74)+chr(0)+chr(38)+chr(0)+chr(1)+chr(79)+chr(0)+chr(8)+chr(3)+chr(232)+chr(0)+chr(0)+chr(1)+chr(80)+chr(0)+chr(11)+chr(128)+chr(0)+chr(32)+chr(0)+chr(0)+chr(0)+chr(0)+chr(3)+chr(255)+chr(0)+chr(14)+chr(0)+chr(0)+chr(101)+chr(26)+chr(0)+chr(0)+chr(0)+chr(23)+chr(0)+chr(2)+chr(0)+chr(237)+chr(0)+chr(13)+chr(0)+chr(0)+chr(0)+chr(0)+chr(238)+chr(0)+chr(6)+chr(18)+chr(64)

        enableROSpecCommand = chr(4)+chr(24)+chr(0)+chr(0)+chr(0)+chr(14)+chr(0)+chr(0)+chr(0)+chr(89)+chr(0)+chr(0)+chr(55)+chr(70)

        closeLLRPCommand = chr(4)+chr(14)+chr(0)+chr(0)+chr(0)+chr(10)+chr(0)+chr(0)+chr(0)+chr(21)

        self.sock.send(enableExtensionCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(setReaderConfigCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(deleteROSpecCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(deleteAccessSpecCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(enableExtensionCommand2.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(setConfigCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(addROSpecCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        self.sock.send(enableROSpecCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)

        #self.sock.send(closeLLRPCommand)
        #flush = self.sock.recv(4096000)

    def getGateStatus(self):
        self._connect()
        getStatusCommand = chr(4)+chr(26)+chr(0)+chr(0)+chr(0)+chr(10)+chr(0)+chr(0)+chr(0)+chr(197)
        try:
            self.sock.send(getStatusCommand.encode('latin-1'))
            self.status = self.sock.recv(4096000)
        except socket.error as e:
            if e.errno == 32:
                pass
            else:
                pass

    def readRFID(self):
    #    self._connect()
        enableReadReportsCommand = chr(4)+chr(64)+chr(0)+chr(0)+chr(0)+chr(10)+chr(0)+chr(0)+chr(0)+chr(18)
        readRequestCommand = chr(4)+chr(60)+chr(0)+chr(0)+chr(0)+chr(10)+chr(0)+chr(0)+chr(0)+chr(19)

        self.sock.send(enableReadReportsCommand.encode('latin-1'))
        flush = self.sock.recv(4096000)
        self.sock.send(readRequestCommand.encode('latin-1'))
        data = []
        data = self.sock.recv(4096000).decode('latin-1')
        booklist = []
        x = 13
        if(len(data)>13):
            while x<len(data):
                if ord(data[x]) == 34:
                    book = ''
                    y = x + 2
                    while y<=x+13:
                        try:
                            if ord(data[x+y])!=0 and (ord(data[x+y])>32 or ord(data[x+y])==1):
                                book = chr(ord(data[x+y]))+book
                            else:
                                pass
                        except IndexError:
                            pass
                        finally:
                            y = y + 1
                    booklist.append(book)
                    x += 34
                else:
                    x = x + 1
        return booklist
