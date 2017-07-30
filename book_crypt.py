# Its a soft that can encrypt text files with transition cipher
#

import time, sys, os
import transposition_cipher as cipher

"""MAIN function that will encrypt and decrypt file, that must be in that folder like a script"""
def main():
	mode = input("Enter (E) to encrypt or (D) to decrypt: ")
	if mode.upper() == 'E':
		encrypt()
	elif mode.upper() == 'D':
		decrypt()	
	


""" Those functions encrypt our file and write it to another file with transposition cipher. Functions that do a crypt and decrypt logic in transposition_cipher.py
Algorithms taked from book 'Hacking cipher with python'"""
# Choose the file to encrypt
def file_to_encrypt():
	active = True
	while active:
		try:
			file_name = input("Enter the file_name, that you want to encrypt or decrypt: ")
			with open(file_name, 'r') as book_text:
				text = book_text.read()
				print("The file was opened")
				active = False
		except FileNotFoundError:
			print("File doesn`t exist, try again")
			time.sleep(1)
	key =int(input("Enter the key: "))
	return text, key

# Encrypt the file
def encrypt():
	message, key = file_to_encrypt()
	print("####Starting to encrypt")
	startTime = time.time()
	encrypted_message = cipher.encryptMessage(key, message)
	print("The time of encryptyng is: {:.3f}".format(time.time() - startTime))
	save_encrypted_File(encrypted_message)

# Saving our encrypted file
def save_encrypted_File(encrypted_file):
	choice = input("Do you want to write it in file? (Y/N)")
	if choice.upper() == 'Y':
		check_active = True
		while check_active:
			outfile_name = input("Enter the name of file: ")
			if os.path.exists(outfile_name):
				checking = input("File with this name is already exist. Do you want to overwrite? Y/N")
				if checking.upper() == 'Y':
					check_active = False
				elif checking.upper() == 'N':
					print('Enter the name again...')
					time.sleep(1)
			else:
				check_active = False
				outfile = open(outfile_name, 'w')
				outfile.write(encrypted_file)
				outfile.close()
				print("#### Everything is done")
	elif choice.upper() == 'N':
		print('Quiting...GoodBye!')
		sys.exit()
#
# THE END OF ENCRYPTYNG IS HERE !!!!!
#


""" Next functions are for decrypting our file. 
And also you can complain original file with this, if you want (those lines are commented)
"""
# Choose file to decrypt
def file_to_decrypt():
	active_D = True
	while active_D:
		try:
			file_to_decrypt = input("Enter the file that you want to decrypt: ")
			with open(file_to_decrypt, 'r') as crypt_text:
				decrypt = crypt_text.read()
				print("The file was opened")
				active_D = False
		except FileNotFoundError:
			print("File doesn`t exist, try again")
			time.sleep(1)
	key = int(input("Enter the key to decrypt: "))
	return decrypt, key

# Decrypting
def decrypt():
	text, key = file_to_decrypt()
	print("#### Starting to decrypt")
	startTime = time.time()
	decrypted_message = cipher.decryptMessage(key, text)
	print("The time of decrypting is: {:.3f}".format(time.time() - startTime))
	save_decrypted_File(decrypted_message)
		
# Save decrypted file
def save_decrypted_File(decrypted):
	file_to_write = input("Enter the name of the file in what you want to save this decrypted text: ")
	decrypt_file = open(file_to_write,'w')
	decrypt_file.write(decrypted)
	print("Everything is done....GoodBye!")

#
#THE END OF DECRYPTING IS HERE!!!
#




if __name__ == '__main__':
	main()
