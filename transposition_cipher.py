import math

def main ():
	message = input("Enter you message: ")
	key = int(input("Enter the key: "))
	mode = input("Enter (E) to encrypt or (D) to decrypt: ")
	if mode.lower() == "e":
		ciphertext = encryptMessage(key, message)
		print(ciphertext + ' end')
	elif mode.lower() == "d":
		decrypt_text = decryptMessage(key, message)
		print(decrypt_text + ' end')

def encryptMessage(myKey, myMessage):
	ciphertext = [''] * myKey
	for col in range(myKey):
		pointer = col
		
		while pointer < len(myMessage):
			ciphertext[col] += myMessage[pointer]
			pointer += myKey
	return ''.join(ciphertext)

def decryptMessage(myKey, myMessage):
	number_of_cols = math.ceil(len(myMessage)/myKey)
	number_of_rows = myKey
	shaded = (number_of_rows*number_of_cols) - len(myMessage)
	
	col = 0
	row = 0

	plain_text = ['']*number_of_cols
	
	for char in myMessage:
		plain_text[col] += char
		col += 1
		if (col == number_of_cols) or (col == number_of_cols - 1 and row >= number_of_rows - shaded):
			col = 0
			row += 1
	return ''.join(plain_text)
	


if __name__ == "__main__":
	main()
