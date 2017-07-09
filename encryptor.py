#!/usr/bin/env python3
#Program to decrypt and modify the data variables stored
#Written by Amruthlal M
#amruth27m AT gmail DOT com

from Crypto.Cipher import ARC4
from json import  dumps,loads

class Encryptor:
	def __init__(self):
		self._key = '<your-key-here>'

	def decryptCredentials(self):
		try:
			with open('credentials.dat','rb') as file:
				EncryptedData = file.read()
		except FileNotFoundError:
			print('Fatal error! Credentials file not found. Contact admin')
			return
		DecryptedData = ARC4.new(self._key).decrypt(EncryptedData).decode('latin-1')
		return loads(DecryptedData)

	def encryptCredentials(self,data):
		jsonData = dumps(data)
		EncryptedData = ARC4.new(self._key).encrypt(jsonData)
		try:
			with open('credentials.dat','wb') as file:
				file.write(EncryptedData)
				return True
		except:
			pass
			
	def getData(self):
		return self.decryptCredentials()
