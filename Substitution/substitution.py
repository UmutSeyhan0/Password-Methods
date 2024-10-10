import string

# Alfabe ve anahtar belirleme
alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
key = "zyxwvutsrqponmlkjihgfedcba"  # Örnek anahtar: ters çevrilmiş alfabe

# Şifreleme fonksiyonu
def encrypt_substitution(plain_text, key):
    table = str.maketrans(alphabet, key)  # Karakter dönüşüm tablosu oluşturma
    return plain_text.translate(table)

# Deşifreleme fonksiyonu
def decrypt_substitution(cipher_text, key):
    table = str.maketrans(key, alphabet)  # Karakter dönüşüm tablosu oluşturma
    return cipher_text.translate(table)

# Kullanıcıdan girdi al
plain_text = input("Şifrelemek istediğiniz metni girin: ").lower()

# Şifreleme
cipher_text = encrypt_substitution(plain_text, key)
print(f"Şifrelenmiş metin: {cipher_text}")

# Deşifreleme
decrypted_text = decrypt_substitution(cipher_text, key)
print(f"Çözümlenmiş metin: {decrypted_text}")
