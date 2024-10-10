from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# AES ile şifreleme fonksiyonu
def encrypt_AES(key, plain_text):
    # 16 byte uzunluğunda rastgele bir IV (initialization vector) oluşturulur
    iv = get_random_bytes(16)
    
    # AES-128 CBC modunda şifreleme nesnesi oluşturulur
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Metin bloklarını 16 byte'a pad ederek şifreleme yapılır
    encrypted_data = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
    
    # IV ve şifrelenmiş veri birleştirilir ve base64 ile kodlanır
    return base64.b64encode(iv + encrypted_data).decode('utf-8')

# AES ile deşifreleme fonksiyonu
def decrypt_AES(key, cipher_text):
    # Base64 ile kodlanmış şifrelenmiş veriyi çöz
    encrypted_data = base64.b64decode(cipher_text)
    
    # İlk 16 byte IV (initialization vector), geri kalanı şifrelenmiş veri
    iv = encrypted_data[:16]
    encrypted_message = encrypted_data[16:]
    
    # AES-128 CBC modunda deşifreleme nesnesi oluşturulur
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Şifrelenmiş veri deşifre edilir ve padding kaldırılır
    decrypted_data = unpad(cipher.decrypt(encrypted_message), AES.block_size)
    
    return decrypted_data.decode('utf-8')

# Anahtar oluşturma (AES-128 için 16 byte uzunluğunda bir anahtar gerekir)
key = get_random_bytes(16)

# Kullanıcıdan girdi al
plain_text = input("Şifrelemek istediğiniz metni girin: ")

# Şifreleme işlemi
cipher_text = encrypt_AES(key, plain_text)
print(f"Şifrelenmiş metin: {cipher_text}")

# Deşifreleme işlemi
decrypted_text = decrypt_AES(key, cipher_text)
print(f"Çözümlenmiş metin: {decrypted_text}")
