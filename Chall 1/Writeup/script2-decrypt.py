#decrypt-script
import base64

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
step1 = caesar(cipher, +3)  # reverse Caesar(-3)
plain = base64.b64decode(step1).decode(errors="ignore")
print("Decrypted Part:", plain)
