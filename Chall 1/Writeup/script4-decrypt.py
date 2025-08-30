#decrypt-script
#part4 (last script)
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse exists")

def affine_decrypt(ciphertext, a=5, b=5):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_{}"
    m = len(alphabet)  # modulus = 39
    a_inv = mod_inverse(a, m)
    result = ""
    
    for char in ciphertext:
        if char not in alphabet:
            raise ValueError(f"Character '{char}' not in alphabet")
        y = alphabet.index(char)
        x = (a_inv * (y - b)) % m
        result += alphabet[x]
    return result


if __name__ == "__main__":
    ciphertext = input("Enter cipher: ").strip()
    plaintext = affine_decrypt(ciphertext)
    print("Decrypted Part:", plaintext)
