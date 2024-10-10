# Atbash şifreleme fonksiyonu
def atbash_encrypt_decrypt(text):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Harf ise tersini bul
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            # Harf değilse aynen bırak
            result += char
    
    return result

# Kullanıcıdan girdi al
plain_text = input("Şifrelemek veya çözmek istediğiniz metni girin: ")



# Atbash şifreleme ve çözme işlemi
cipher_text = atbash_encrypt_decrypt(plain_text)
print(f"Sonuç: {cipher_text}")
