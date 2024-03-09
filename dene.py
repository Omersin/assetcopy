import os
import requests
import shutil

def tarayici(klasor_yolu, hedef_url):
    # Klasördeki dosya ve klasörleri listeleyin
    dosya_listesi = os.listdir(klasor_yolu)

    # Her dosya veya klasör için işlem yapın
    for dosya_adi in dosya_listesi:
        dosya_yolu = os.path.join(klasor_yolu, dosya_adi)

        # Eğer bir klasörse, altındaki dosyaları tarayın
        if os.path.isdir(dosya_yolu):
            alt_klasor_yolu = os.path.join(klasor_yolu, dosya_adi)
            tarayici(alt_klasor_yolu, hedef_url + dosya_adi + '/')

        # Eğer bir dosyaysa, dosyayı indirin ve üzerine yazın
        elif os.path.isfile(dosya_yolu):
            try:
                hedef_dosya_url = hedef_url + dosya_adi
                response = requests.get(hedef_dosya_url, stream=True)
                with open(dosya_yolu, 'wb') as dosya:
                    shutil.copyfileobj(response.raw, dosya)
                print(f"{dosya_adi} başarıyla indirildi ve üzerine yazıldı.")
            except Exception as e:
                print(f"Hata: {e}")

klasor_yolu = r'D:\Web\HTML Temp\Kategorize\Kurumsal\insidehtml-10\insidehtml-10\inside\images'
hedef_url = 'https://team90degree.com/html/tf/inside-preview/images/'

tarayici(klasor_yolu, hedef_url)
print("İşlem tamamlandı.")
