import sys, cryptomath, random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
	myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
	#myMessage = """7bYZLn;EV8xY#LE IYI8g8x48YVLYk8YZ|  8IYS]V8  Su8]VYS'YSVYZLE IYI8Z8S48Y|YdEn|]YS]VLYk8 S84S]uYVd|VYSVY#|gYdEn|])7Y:b |]Y<ExS]u"""
	myKey = getKeyRandom()
	myMode = 'encrypt'

	if myMode == 'encrypt':
		translated = encryptMessage(myKey, myMessage)
	elif myMode == 'decrypt':
		translated = decryptMessage(myKey, myMessage)
	print('Key: %s' %(myKey))
	print('%sed text:' %(myMode.title()))
	print(translated)

def getKeyParts(key):
	keyA = key //len(SYMBOLS)
	keyB = key % len(SYMBOLS)
	return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
	if keyA == 1 and mode == 'encrypt':
		sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
	if keyB == 0 and mode == 'encrypt':
		sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
	if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
		sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' %(len(SYMBOLS)-1))
	if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
		sys.exit('Key A (%s) and the symbol size (%s) are not relatively prime. Choos a different key.' % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):
	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, 'encrypt')
	ciphertext = ''
	for symbol in message:
		if symbol in SYMBOLS:
			symIndex = SYMBOLS.find(symbol)
			ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
		else:
			ciphertext += symbol
	f = open('encrypted.txt', 'w')
	f.write(ciphertext)
	f.close()
	return ciphertext

def decryptMessage(key, message):
	keyA, keyB = getKeyParts(key)
	checkKeys(keyA, keyB, 'decrypt')
	plaintext = ''
	modInverseofKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

	for symbol in message:
		if symbol in SYMBOLS:
			symIndex = SYMBOLS.find(symbol)
			plaintext += SYMBOLS[((symIndex - keyB)*modInverseofKeyA) % len(SYMBOLS)]
		else:
			plaintext += symbol
	return plaintext	

def getKeyRandom():
	while True:
		keyA = random.randint(2, len(SYMBOLS))
		keyB = random.randint(2, len(SYMBOLS))
		if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
			return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
	main()
