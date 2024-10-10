import numpy as np

# Harfleri sayılara çevirme fonksiyonu
def harf_to_sayi(harf):
    return ord(harf.upper()) - ord('A')

# Sayıları harflere çevirme fonksiyonu
def sayi_to_harf(sayi):
    return chr(int(sayi) + ord('A'))

# Şifrelenecek metni anahtar matris ile çarpma fonksiyonu
def sifrele(metin, key_matrix):
    # Harfleri sayılara çevir
    sayilar = [harf_to_sayi(harf) for harf in metin]
    
    # Sayı dizisini anahtar matrisi ile çarp
    sonuc = np.dot(key_matrix, sayilar) % 26  # Mod 26 ile çarptık (Alfabe 26 harften oluşuyor)
    
    # Sayıları tekrar harfe çevir
    sifreli_metin = ''.join([sayi_to_harf(sayi) for sayi in sonuc])
    
    return sifreli_metin

# Anahtar matrisi ve şifrelenecek metni kullanıcıdan al
def kullanici_girdisi():
    metin = input("Şifrelenecek metni girin (harf sayısı matrise uygun olmalı): ").upper()
    
    boyut = int(input("Anahtar matrisinin boyutunu girin (örn. 2 için 2x2, 3 için 3x3): "))
    
    key_matrix = []
    print(f"Anahtar matrisin elemanlarını girin ({boyut}x{boyut} boyutlu bir matris için {boyut**2} sayı):")
    
    for i in range(boyut):
        row = list(map(int, input(f"{i + 1}. satır elemanlarını girin: ").split()))
        key_matrix.append(row)
    
    key_matrix = np.array(key_matrix)
    
    if len(metin) % boyut != 0:
        print(f"Metnin harf sayısı {boyut}'a tam bölünmelidir.")
        return
    
    return metin, key_matrix

# Ana fonksiyon
def hill_sifreleme():
    metin, key_matrix = kullanici_girdisi()
    sifreli_metin = sifrele(metin, key_matrix)
    
    print(f"Şifrelenmiş metin: {sifreli_metin}")

# Programı çalıştır
hill_sifreleme()
