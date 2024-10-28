def yıkık():
    #=- YIKIK YAZILIM  -=#
    from time import sleep
    a='.\nAlways\nFrequently\nSometimes\nRarely\nNever'.splitlines()# uygulamada kulnadığım satır
    while 1:
        try:
            a.remove(a[0])
            print(f"dating {6-len(a)}:\n", " $- how often do you want to dating me","\n  #-" ,a[0])
        except:
            print("you're a disgrace... give my time back")
            break
        sleep(1)
    #=- Not(is important): böyle salakça şeylerle işim olmaz işin sadece dalgasındyım  -=#

def sıra(dik,nm): #we here sorting dictionary by nm. nm is a dictionary element(and nm is number)
    b=[]
    c=[]
    for i in dik:
        b.append(float(i[nm]))
    b.sort(reverse=True)
    for i in b:
        for x in a:
            if float(x[nm])==i: c.append(x)
    return c

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(start, end): # ikiz asal sayıları bulur ve yazar
    twin_primes = []
    for num in range(start, end - 1):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

class Sifreleme:
    def __init__(self, anahtar):
        self.anahtar = anahtar

    # 1. Sezar Şifreleme Metodu
    def sezar_sifrele(self, text, kaydirma=3):
        sifreli_text = ""
        for harf in text:
            # Harf alfabeye dahilse şifrele, değilse olduğu gibi ekle
            if harf.isalpha():
                shift_base = ord('A') if harf.isupper() else ord('a')
                sifreli_text += chr((ord(harf) - shift_base + kaydirma) % 26 + shift_base)
            else:
                sifreli_text += harf
        return sifreli_text

    def sezar_coz(self, sifreli_text, kaydirma=3):
        # Şifreyi çözmek için ters kaydırma yapıyoruz
        return self.sezar_sifrele(sifreli_text, -kaydirma)

    # 2. Vigenere Şifreleme Metodu
    def vigenere_sifrele(self, text):
        sifreli_text = ""
        anahtar_index = 0
        for harf in text:
            # Harf alfabeye dahilse şifrele, değilse olduğu gibi ekle
            if harf.isalpha():
                shift_base = ord('A') if harf.isupper() else ord('a')
                kaydirma = ord(self.anahtar[anahtar_index % len(self.anahtar)].lower()) - ord('a')
                sifreli_text += chr((ord(harf) - shift_base + kaydirma) % 26 + shift_base)
                anahtar_index += 1
            else:
                sifreli_text += harf
        return sifreli_text

    def vigenere_coz(self, sifreli_text):
        cozulmus_text = ""
        anahtar_index = 0
        for harf in sifreli_text:
            # Harf alfabeye dahilse çöz, değilse olduğu gibi ekle
            if harf.isalpha():
                shift_base = ord('A') if harf.isupper() else ord('a')
                kaydirma = ord(self.anahtar[anahtar_index % len(self.anahtar)].lower()) - ord('a')
                cozulmus_text += chr((ord(harf) - shift_base - kaydirma) % 26 + shift_base)
                anahtar_index += 1
            else:
                cozulmus_text += harf
        return cozulmus_text

    # 3. XOR Şifreleme Metodu
    def xor_sifrele(self, text):
        sifreli_text = ""
        for i in range(len(text)):
            sifreli_harf = chr(ord(text[i]) ^ ord(self.anahtar[i % len(self.anahtar)]))
            sifreli_text += sifreli_harf
        return sifreli_text

    def xor_coz(self, sifreli_text):
        # XOR işlemi tersinir olduğu için aynı fonksiyonla çözebiliriz
        return self.xor_sifrele(sifreli_text)


    #anahtar = "ANAHTAR"  # Vigenere ve XOR şifreleme için anahtar kelime
    #
    #sifreleme = Sifreleme(anahtar)
    #
    ## Sezar Şifreleme Örneği
    #text = "MERHABA DUNYA"
    #sezar_sifreli = sifreleme.sezar_sifrele(text, 4)
    #sezar_cozulen = sifreleme.sezar_coz(sezar_sifreli, 4)
    #print("Sezar Şifreli:", sezar_sifreli)
    #print("Sezar Çözülen:", sezar_cozulen)
    #
    ## Vigenere Şifreleme Örneği
    #vigenere_sifreli = sifreleme.vigenere_sifrele(text)
    #vigenere_cozulen = sifreleme.vigenere_coz(vigenere_sifreli)
    #print("\nVigenere Şifreli:", vigenere_sifreli)
    #print("Vigenere Çözülen:", vigenere_cozulen)
    #
    ## XOR Şifreleme Örneği
    #xor_sifreli = sifreleme.xor_sifrele(text)
    #xor_cozulen = sifreleme.xor_coz(xor_sifreli)
    #print("\nXOR Şifreli:", xor_sifreli)
    #print("XOR Çözülen:", xor_cozulen)
