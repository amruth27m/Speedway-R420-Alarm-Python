#!/usr/bin/env python3
#program to write data to credentials file
from Crypto.Cipher import ARC4
from json import dumps

dataDictonary = { '<Your data here as key value pair>'}
dataDictonaryJSON = dumps(ls)
dataDictonaryEncrypted = ARC4.new('<your key here>').encrypt(dataDictonaryJSON)
with open('credentials.dat','wb') as f:
	f.write(dataDictonaryEncrypted)

