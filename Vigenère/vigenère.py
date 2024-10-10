def generate_key(plain_text, key):
    key = list(key)
    if len(plain_text) == len(key):
        return key
    else:
        for i in range(len(plain_text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plain_text, key):
    cipher_text = []
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def decrypt_vigenere(cipher_text, key):
    plain_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plain_text.append(chr(x))
    return "".join(plain_text)


plain_text = input("Şifrelemek istediğiniz metni girin: ").upper().replace(" ", "")
key = input("Anahtarı girin: ").upper()

key = generate_key(plain_text, key)

cipher_text = encrypt_vigenere(plain_text, key)
print(f"Şifrelenmiş metin: {cipher_text}")

decrypted_text = decrypt_vigenere(cipher_text, key)
print(f"Çözümlenmiş metin: {decrypted_text}")
