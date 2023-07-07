### Python If-Else Kullanımı Örneği - 1 ###
ayrac =  '--------------------';
print(ayrac,"\n< Python If-Else Kullanım Örneği #1 >\n"+ayrac)
ogrenciAdi = input("-> Öğrencinin Adını Girin: ")
ogrenciSoyadi = input ("-> Öğrencinin Soyadını Girin: ")
print(ayrac,"\n->",ogrenciAdi,ogrenciSoyadi,"olarak sisteme öğrenci kaydı gerçekleştirildi.\n"+ayrac)
vizeNotu = float(input("-> Öğrencinin Vize Notunu Girin: "))
finalNotu = float(input("-> Öğrencinin Final Notunu Girin: "))
ogrenciOrtalamasi = float ((vizeNotu * 0.4) + (finalNotu * 0.6))
if ((ogrenciOrtalamasi >= 60) and (ogrenciOrtalamasi <= 100)):
    print(ayrac,"\n-> Öğrenci bilgileri kontrol edildikten sonra 'başarılı' bir öğrenci olduğu kararına varıldı.\n-> Öğrencinin Ortalaması:",ogrenciOrtalamasi,"\n"+ayrac)
else:
    print(ayrac,"\n-> Öğrenci bilgileri kontrol edildikten sonra 'başarısız' bir öğrenci olduğu kararına varıldı.\n-> Öğrencinin Ortalaması:",ogrenciOrtalamasi,"\n"+ayrac)