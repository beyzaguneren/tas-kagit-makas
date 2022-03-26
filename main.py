import random
elemanlar = ["taş","kağıt","makas"]
taş = elemanlar[0]
kağıt = elemanlar[1]
makas = elemanlar[2]
print("taş kağıt makas oyunumuza hoşgeldiniz,çıkmak için q basbilirsiniz")
bilgisayar_puanı = (0)
oyuncu_puanı = (0)
while True:
    seçim = input("taş kağıt makas arasından hamlenizi yazınız")
    bilgisayar_seçimi = random.choice(elemanlar)
    if seçim == taş:
        if bilgisayar_seçimi == taş:
            print ("berabere")
        elif bilgisayar_seçimi == kağıt:
            print("kaybettiniz,ez")
            bilgisayar_puanı = (bilgisayar_puanı+1)
        else:
            print("tebrikler kazandınız")
            oyuncu_puanı = (oyuncu_puanı+1)
    if seçim == kağıt:
        if bilgisayar_seçimi == taş:
            print("tebrikler kazandınız")
            oyuncu_puanı = (oyuncu_puanı+1)
        elif bilgisayar_seçimi == kağıt:
            print("berabere")
        else:
            print("kaybettiniz,ez")
            bilgisayar_puanı = (bilgisayar_puanı+1)
    if seçim == makas:
        if bilgisayar_seçimi == taş:
            print("kaybettiniz,ez")
            bilgisayar_puanı = (bilgisayar_puanı+1)
        elif bilgisayar_seçimi == kağıt:
            print("kazandınız")
            oyuncu_puanı = (oyuncu_puanı+1)
        else:
            print("berabere")
    print (str("oyuncunun puanı =" + str(oyuncu_puanı) + "bilgisayar puanı="+ str(bilgisayar_puanı)))
    if seçim == ("q"):
        print("oyun kapatılıyor...")
        break