# Modüler ters bulma fonksiyonu (mod 26 için)
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Affine şifreleme fonksiyonu
def affine_encrypt(plain_text, a, b):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():  # Yalnızca harfler şifrelenir
            x = ord(char.upper()) - ord('A')  # Harfi A = 0, B = 1, ..., Z = 25 şeklinde numaraya çevir
            encrypted_char = (a * x + b) % 26  # Affine şifreleme formülü
            cipher_text += chr(encrypted_char + ord('A'))  # Şifrelenmiş sayıyı tekrar harfe çevir
        else:
            cipher_text += char  # Harf olmayan karakterler aynen kalır
    return cipher_text

# Affine deşifreleme fonksiyonu
def affine_decrypt(cipher_text, a, b):
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)  # Mod 26'ya göre çarpma anahtarının tersini bul
    if a_inv is None:
        raise ValueError("Anahtar a'nin mod 26'ya göre tersi yok!")

    for char in cipher_text:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')  # Şifrelenmiş harfi numaraya çevir
            decrypted_char = (a_inv * (y - b)) % 26  # Affine deşifreleme formülü
            decrypted_text += chr(decrypted_char + ord('A'))  # Çözümlenmiş sayıyı tekrar harfe çevir
        else:
            decrypted_text += char  # Harf olmayan karakterler aynen kalır
    return decrypted_text

# Kullanıcıdan girdi al
plain_text = input("Şifrelemek istediğiniz metni girin: ").upper()
a = int(input("Çarpma anahtarını (a) girin: "))
b = int(input("Toplama anahtarını (b) girin: "))

# Modüler tersin varlığını kontrol et (mod 26'ya göre ters bulunamazsa hata verir)
if mod_inverse(a, 26) is None:
    raise ValueError("Çarpma anahtarı a'nın mod 26'ya göre tersi yok! Lütfen geçerli bir değer girin.")

# Şifreleme işlemi
cipher_text = affine_encrypt(plain_text, a, b)
print(f"Şifrelenmiş metin: {cipher_text}")

# Deşifreleme işlemi
decrypted_text = affine_decrypt(cipher_text, a, b)
print(f"Çözümlenmiş metin: {decrypted_text}")
