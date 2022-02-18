# VFS_Appointment_Checker
Appointment Checker for VFS Global 

Gereksinimler:

PYTHON3 
Selenium
ChromeDriver

1 - Öncelikle Python3 indirmeniz gerekiyor
    Microsoft Store'dan Pyhon diye aratarak kolaylıkla indirebilirsiniz.
    Pythonın sisteminize kurduktan sonra Komut sistemine python yazdığınızda aşağıdakine benzer bir sonuç görmelisiniz.
    ![image](https://user-images.githubusercontent.com/33903008/154581828-5b7bb56b-7c4b-4d39-b3a9-50f15a984555.png)
    
   Eğer böyle bir çıktı göremediyseniz aşağıdaki linkteki adımları takip edin
    
    
   https://www.kodaylak.com/2018/09/ortam-degiskenlerine-python-path-ekleme.html


2 - Selenium ikinci gereken bileşen
    Aşağıdaki linkteki websitesinden soldaki 'Download files' başlığına tıkladığınızda sağ tarafta çıkan .whl ile biten dosyayı indirin.
    https://pypi.org/project/selenium/
   Bu dosyayıda çift tıklayarak çalıştırın.


3 - ChromeDriver yüklenmesi - bu adımda aşağıdaki linkten Google chrome sürümünüze ait versiyonu indirin
    https://chromedriver.chromium.org/downloads
    
   Chrome versiyon için Chrome açıldığında sağ üstteki üç noktaya tıklayıp 'Yardım' -> 'Google Chrome hakkında' kısmından görebilirsiniz.
    İndirdiğiniz dosyayı bir klasör içine çıkarın. Mesela bilgisayardaki C:\webdriver altına olabilir.
    ![image](https://user-images.githubusercontent.com/33903008/154586658-237c2175-6e0c-43a2-92b4-34004c49a8ae.png)

   Daha sonra bilgisayarıma sağ tıklayıp Özelliklere tıkladığınızda 'Gelişmiş sistem ayarları' na tıklayın 
    Burada sağ altta Ortam değişkenlerine tıklayın. Burada karşınızda iki bölmeli bir alan gelecek.
    Buradan alltaki kısımdaki 'Path' üzerine tıklayıp düzenle diyin.
    ![image](https://user-images.githubusercontent.com/33903008/154583666-6120a77b-15e3-4c5d-9417-800dd5281d0e.png)
    
   Burada 'Yeni' kısmına tıklayıp Chromedriverın bulunduğu klasörün adresini yazın.
    
Bu adımları tamamladıktan sonra CheckVFS2 adlı dosyayı birlite aç diyip notepadi seçin 
içindeki gerekli alanları aradğınız randevuya göre değiştirin.
İşlem tamamlandığında kaydedip kapatın.

CheckVFS2.py adlı dosyayı çift tıklayıp çalıştırın.
    
