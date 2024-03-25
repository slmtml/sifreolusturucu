import random
harfler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    sifre_uzunlugu=int(input("Şifre uzunluğu giriniz:"))
    sifre= ""
    for i in range(sifre_uzunlugu):
        harf=random.choice(harfler)
        sifre+=harf

    print("Şifre uzunluğu: ",sifre_uzunlugu,"Şifreniz: ",sifre)
