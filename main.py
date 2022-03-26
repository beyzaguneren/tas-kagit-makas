import random
elemanlar = ["taş","kağıt","makas"]
taş = elemanlar[0]
kağıt = elemanlar[1]
makas = elemanlar[2]
print("taş kağıt makas oyunumuza hoşgeldiniz,çıkmak için q basbilirsiniz")

while True:
    seçim = input("taş kağıt makas arasından hamlenizi yazınız")
    bilgisayar_seçimi = random.choice(elemanlar)
    if seçim == taş:

        if bilgisayar_seçimi == taş:
            print ("berabere")
        elif bilgisayar_seçimi == kağıt:
            print("kaybettiniz")
        else:
            print("tebrikler kazandınız")
    if seçim == kağıt:
        if bilgisayar_seçimi == taş:
            print("tebrikler kazandınız")
        elif bilgisayar_seçimi == kağıt:
            print("berabere")
        else:
            print("kaybettiniz")
    if seçim == makas:
        if bilgisayar_seçimi == taş:
            print("kaybettiniz")
        elif bilgisayar_seçimi == kağıt:
            print("kazandınız")
        else:
            print("berabere")
    if seçim == ("q"):
        print("oyun kapatılıyor...")
        break