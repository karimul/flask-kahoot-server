shifter = 2
alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"

def encrypt(word):
    encrypted = ""

    for char in word:
        charIndex = alphanumeric.index(char)
        newCharIndex = charIndex + shifter
        
        if newCharIndex >= len(alphanumeric):
            newCharIndex = newCharIndex % len(alphanumeric)

        newChar = alphanumeric[newCharIndex]
        encrypted += newChar
    
    return encrypted

def decrypt(word):
    decrypted = ""

    for char in word:
        charIndex = alphanumeric.index(char)
        newCharIndex = charIndex - shifter

        if newCharIndex < 0:
            newCharIndex += len(alphanumeric)

        newChar = alphanumeric[newCharIndex]
        decrypted += newChar

    return decrypted
