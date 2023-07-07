vize = int(input("Vize Notunuz..:"))
final = int(input("Final Notunuz..:"))
ort = vize*0.4 + final*0.6
if ort<50:
    print ("FF")
elif ort<60:
    print ("CC")
elif ort<70:
    print ("CB")
elif ort<80:
    print ("BB")
elif ort<90:
    print ("AB")
elif ort>=90:
    print ("AA")

print (ort)


while True:

    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        break
    if (işlem == "1"):
        kumanda.tv_aç()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        print(kumanda)
    elif (işlem == "4"):
        print("Kanal Sayısı: ",len(kumanda))
    elif (işlem == "5"):
        kanallar = input("Eklemek İstediğiniz Kanalları ',' ile ayırarak girin:")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:

            kumanda.kanal_ekle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        kumanda.sesi_azalt_artir()
    else:
        print("Geçersiz İşlem...")
