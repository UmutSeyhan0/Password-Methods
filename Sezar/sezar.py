
def encrypt(text,s):
    result = ""

    
    for i in range(len(text)):
        char = text[i]

        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

       
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


text =input("şifrelemek istediğiniz metni giriniz:") 
s =int(input("anahtarı giriniz:"))

print ("metin  : " + text)
print ("anahtar : " + str(s))
print ("şifrelenmiş metin: " + encrypt(text,s))
