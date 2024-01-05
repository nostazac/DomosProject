import sys,cryptomath,random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
def main():
    myMessage == """"A computer would deserve to be callrd intelligent if it could decieve human into  believing that ot was a human." -Alan Turing"""
    myKey = 2894
    myMOde = 'encrypt'#set to either encrypt or decrypt

    if myMOde == 'encrypt':
        translated = encryptMessage(myKey, myMEssage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myMode.title()))
    print('%sed text:' % (myMode.title()))
    print('Full % used text copied to clipboard.'%(myMode))

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)
def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
    if key == 0 and mode =='encrypt':
        sys.exit('Cipher is weak if B is 0. CHoose a diffeent key.')
    if cryptomath.gcd(keyA,len(SYMBOLS)) != 1:
        SYS.EXIT('Key A (%s) and the symbols set size (%s) are not relatively prime.Choose a different key.' %(keyA,len(SYMBOLS)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolINdex = find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext == symbol
    return ciphertext


def decryptMessage(key, message):
    keyA,keyB = getParts(key)
    checkKeys(keyA,keyB,'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SyMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB  = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * LEN(symbols) + keyB#ifaffineCipher.py is run(insteas of import asw a mopdule the main function

if _name__ == '__main__':
    main()



