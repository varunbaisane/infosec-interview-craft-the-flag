#decrypt script
#part1
def atbash(text):
    result = ""
    for c in text:
        if c.isalpha():
            if c.islower():
                result += chr(ord('z') - (ord(c) - ord('a')))
            else:
                result += chr(ord('Z') - (ord(c) - ord('A')))
        else:
            result += c
    return result

def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

cipher = input("Enter cipher: ")
step1 = caesar(cipher, +5)  
plain = atbash(step1)      
print("Decrypted Part:", plain)
