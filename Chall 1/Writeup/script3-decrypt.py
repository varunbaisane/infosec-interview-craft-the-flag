#decrypt-script
def char_to_val(c):
    if c.isalpha():
        return ord(c) - ord('a') + 1
    elif c.isdigit():
        return int(c) + 27
    elif c == "_":
        return None
    return None

def val_to_char(v):
    if 1 <= v <= 26:
        return chr(ord('a') + v - 1)
    elif 27 <= v <= 36:
        return str(v - 27)
    return "_"

def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

cipher = input("Enter cipher: ")
step1 = caesar(cipher, +2)
plain = ""
for c in step1:
    if c == "_":
        plain += "_"
    else:
        y = char_to_val(c)
        x = (29 * (y - 5)) % 36
        if x == 0: 
            x = 36
        plain += val_to_char(x)
print("Decrypted Part:", plain)
