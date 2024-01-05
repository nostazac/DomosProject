#comment due to void module
#import pyperclip

def main():
	myMessage = input("Text to decrypt: ")
	myKey = int(input("Encryption key: "))
	ciphertext = encryptedMessage(myKey, myMessage)
	#print pipe in case of empty space
	print(ciphertext + '|')


def encryptedMessage(key, message):
	ciphertext = [''] * key
	for column in range(key):
		currentIndex = column
		while currentIndex < len(message):
			ciphertext[column] += message[currentIndex]
		#move current index as per the key
		currentIndex += key

	#return and join the ciphertext
	return ''.join(ciphertext)

if __name__ == '__main__':
	main()

