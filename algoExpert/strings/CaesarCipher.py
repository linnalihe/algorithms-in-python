def caesarCipherEncryptor(string, key):
    # Write your code here.
	newString = [ord(char) for char in string]
	for i in range(len(newString)):
		newString[i] = chr((newString[i] - ord('a') + key) % 26 + ord('a'))
    return "".join(newString)
