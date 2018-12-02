"""
Another Mediocre Creation by Christina Andronescu
this program will take a message of your choice and encrypt it or decrypt it. For
encryption, in layman terms, this program takes all the even-numbered letters and
odd-numbered letters and places the even ones at the front and the odd ones at the
the end of a resulting, printed string. Decryption is the reverse of that with
consideration of the message's length (number of characters).

I'd like to thank the Academy and these 2 vids:
https://www.youtube.com/watch?v=qOlJwi9mu2Q
https://www.youtube.com/watch?v=uaCumJi4Iuw
"""

well = input("you wanna decrypt or encrypt? type either 'encrypt' or 'decrypt': ")
plainText = input("type el mensaje aquí: ")

def scramble(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if (charCount%2==0):
            #even character
            evenChars = evenChars + ch
        else:
            #odd characters
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars #order of it
    return cipherText

def unscramble(cipherText):
    #separate the 2 strings
    # // is integer division
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength] #odd chars is equal to the cipher text sliced up until the very beginning to half length
    evenChars = cipherText[halfLength:] #even picks up where left off for the other half of the text
    
    plainText = ""
    
    for i in range(halfLength): #will put 2 characters together at one time (1 even, 1 odd)
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]
        
    if len(evenChars) > len(oddChars): #to accomodate for an uneven amount of evens/odds
        plainText = plainText + evenChars[-1]
        
    return plainText
    plain = scramble(message)
    print(plain)

if (well == "encrypt"):
    print(scramble(plainText))

if (well == "decrypt"):
    print(unscramble(plainText))
