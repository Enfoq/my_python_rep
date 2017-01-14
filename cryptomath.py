#Cryptomath module with 2 functions: Greatest Common Diviser and Module Inverse
#For some cryptograpyhy ciphers
#
#

def gcd(a, b):
	while a!=0:
		a, b = b % a, a
	return b

def findModInverse(a, m):
	#Return the modular inverse of a % m, wich is
	#the number x such that a*x % m = 1
	
	if gcd(a,m) !=1:
		return None #no mod inverse if a & m aren`t relatively prime
	k1, k2, k3 = 1, 0, a
	v1, v2, v3 = 0, 1, m

	while v3 != 0:
		q = k3//v3
		v1, v2, v3, k1, k2, k3 = (k1 - q * v1), (k2 - q * v2), (k3 - q * v3), v1, v2, v3
	return k1 % m

