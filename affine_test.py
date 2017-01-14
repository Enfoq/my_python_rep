import affine_c, cryptomath

message = 'Make things as simple as possible, but not simpler.'

for keyA in range(2,100):
	key = keyA * len(affine_c.SYMBOLS) + 1

	if cryptomath.gcd(keyA, len(affine_c.SYMBOLS)) == 1:
		print(keyA, affine_c.encryptMessage(key, message))
