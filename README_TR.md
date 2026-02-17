<h1 align="center">
<a href="https://github.com/bhavsec/reconspider"><img src="https://raw.githubusercontent.com/bhavsec/reconspider/master/logo.png" width="200"></a>
</h1>

<h4 align="center"> En Gelişmiş Açık Kaynak İstihbarat (OSINT) Çerçevesi </h4>

<p align="center">
<a href="https://github.com/bhavsec/reconspider"><img src="https://img.shields.io/static/v1?label=version&message=1.0.7&color=blue"></a>
<a href="https://github.com/bhavsec/reconspider/issues?q=is:issue+is:closed"><img src="https://img.shields.io/github/issues-closed/bhavsec/reconspider?color=orange"></a>
<a href="https://travis-ci.com/bhavsec/reconspider"><img src="https://api.travis-ci.com/bhavsec/reconspider.svg"></a>
</p>

# ReconSpider

ReconSpider; IP adresleri, e-postalar, web siteleri ve organizasyonlar üzerinde tarama yaparak farklı kaynaklardan bilgi toplayan en gelişmiş Açık Kaynak İstihbarat (OSINT) çerçevesidir.

ReconSpider; Bilgi Güvenliği Araştırmacıları, Sızma Testçileri, Hata Avcıları ve Siber Suç Araştırmacıları tarafından hedefleri hakkında derinlemesine bilgi edinmek amacıyla kullanılabilir.

ReconSpider, ham verilerin tamamını toplar, bir pano üzerinde görselleştirir ve veriler üzerinde uyarı ile izleme imkânı sunar.

ReconSpider aynı zamanda kapsamlı bir saldırı yüzeyi taraması gerçekleştirmek için [Wave](https://github.com/adithyan-ak/WAVE), [Photon](https://github.com/s0md3v/Photon) ve [Recon Dog](https://github.com/s0md3v/ReconDog) araçlarının yeteneklerini de bünyesinde barındırır.

# Neden ReconSpider Olarak Adlandırıldı?

```ReconSpider```  =  ```Recon```  +  ```Spider```


**Recon** = **Keşif (Reconnaissance)**

Keşif; bir düşmanın veya olası düşmanın faaliyetleri ve kaynakları ya da belirli bir bölgenin coğrafi özellikleri hakkında çeşitli tespit yöntemleriyle bilgi edinmeye yönelik bir görevdir.


**Spider = Web Tarayıcısı**

Bazen örümcek (spider) veya örümcek bot (spiderbot) olarak da adlandırılan ve çoğunlukla tarayıcı (crawler) olarak kısaltılan bir web tarayıcısı; genellikle web dizinleme (web örümcekliği) amacıyla World Wide Web'i sistematik biçimde gezen bir internet botudur.


# İçindekiler

1. [Sürüm (beta)](https://github.com/bhavsec/reconspider#version-beta)
2. [Araca Genel Bakış](https://github.com/bhavsec/reconspider#overview-of-the-tool)
3. [Zihin Haritası (v1)](https://github.com/bhavsec/reconspider#mind-map-v1)
4. [Lisans Bilgileri](https://github.com/bhavsec/reconspider#license-information)
5. [ReconSpider Başlık Ekranı](https://github.com/bhavsec/reconspider#reconspider-banner)
6. [Belgeler](https://github.com/bhavsec/reconspider#documentation)
7. [Ortamın Kurulumu](https://github.com/bhavsec/reconspider#setting-up-the-environment)
8. [API Anahtarlarının Güncellenmesi](https://github.com/bhavsec/reconspider#updating-api-keys)
9. [Kullanım](https://github.com/bhavsec/reconspider#usage)
10. [İletişim](https://github.com/bhavsec/reconspider#contact)
11. [Wiki ve Kullanım Kılavuzu](https://github.com/bhavsec/reconspider#reconspider-full-wiki-and-how-to-guide)
12. [Güncellemeler](https://github.com/bhavsec/reconspider#frequent--seamless-updates)


# Sürüm (beta)

	ReconSpider   :     1.0.7


# Araca Genel Bakış

* IP adresleri, e-postalar, web siteleri ve organizasyonlar üzerinde OSINT taraması yaparak farklı kaynaklardan bilgi toplar.
* Sonuçları ilişkilendirir ve bir arada sunar, birleştirilmiş biçimde görüntüler.
* Belirli bir komut dosyası kullanır / birleştirilmiş veri için otomatik OSINT başlatır.
* Şu an yalnızca Komut Satırı Arayüzü (CLI) üzerinden kullanılabilmektedir.


# Zihin Haritası (v1)

API'ler, servisler, teknikler ve daha fazlasına ilişkin araç bilgilerini görsel olarak düzenlenmiş biçimde görmek için zihin haritamıza göz atın.

https://bhavsec.com/img/reconspider_map.png


# Lisans Bilgileri

```
ReconSpider ve ilgili belgeler GPL-3.0 (Genel Kamu Lisansı v3.0) kapsamındadır.
```


## ReconSpider Başlık Ekranı

```
__________                               _________       __     ___            
\______   \ ____   ____  ____   ____    /   _____/_____ |__| __| _/___________
 |       _// __ \_/ ___\/  _ \ /    \   \_____  \\____ \|  |/ __ |/ __ \_  __ \
 |    |   \  ___/\  \__(  <_> )   |  \  /        \  |_> >  / /_/ \  ___/|  | \/
 |____|_  /\___  >\___  >____/|___|  / /_______  /   __/|__\____ |\___  >__|   
        \/     \/     \/           \/          \/|__|           \/    \/       



SEÇENEĞİ SEÇMEK İÇİN 0 - 13 ARASI BİR SAYI GİRİN

1.  IP                           IP  Adresinden  bilgi  topla
2.  DOMAIN                       Verilen  DOMAIN  hakkında  bilgi  topla
3.  PHONENUMBER                  Telefon  numarası  hakkında  bilgi  topla
4.  DNS MAP                      Hedefe  ait  DNS  kayıtlarını  haritalandır
5.  METADATA                     Verilen  dosyanın  tüm  meta  verilerini  çıkar
6.  REVERSE IMAGE SEARCH         Alan  adı  veya  IP  adresi  eşlemesi  bul
7.  HONEYPOT                     Gerçek  sistem  mi  tuzak  mı  kontrol  et
8.  MAC ADDRESS LOOKUP           MAC  adresi  hakkında  bilgi  edin
9.  IPHEATMAP                    IP  konumlarının  ısı  haritasını  çıkar
10. TORRENT                      IP'nin  torrent  indirme  geçmişini  topla
11. USERNAME                     Sosyal  medyadaki  hesap  bilgilerini  çıkar
12. IP2PROXY                     IP'nin  VPN  /  Proxy  kullanıp  kullanmadığını  kontrol  et
13. MAIL BREACH                  Verilen  domainde  sızdırılmış  mail  kontrol  et
99. UPDATE                       ReconSpider'ı  en  son  sürüme  güncelle

0. EXIT                         ReconSpider'dan  terminalinize  çıkış  yap
```


# Belgeler

ReconSpider'ı kurmak ve kullanmak son derece kolaydır. Kurulum süreci oldukça basittir.

1. ReconSpider GitHub deposunu indirme veya klonlama.
2. Tüm bağımlılıkların kurulması.
3. Veritabanının yapılandırılması.

Hadi Başlayalım!!


### Ortamın Kurulumu

Adım 1 - ReconSpider'ı Linux sisteminize klonlayın.

ReconSpider'ı indirmek için GitHub deposunu klonlamanız yeterlidir. Depoyu klonlamak için aşağıdaki komutu kullanabilirsiniz:

```
git clone https://github.com/bhavsec/reconspider.git
```

Adım 2 - Sisteminizde python3 ve python3-pip'in kurulu olduğundan emin olun.

Terminalinize aşağıdaki komutu yazarak kontrol edebilirsiniz:

```
sudo apt install python3 python3-pip
```

Adım 3 - Tüm bağımlılıkları kurun.

Depoyu klonlayıp Python kurulumunu doğruladıktan sonra **reconspider** adlı dizini bulacaksınız. O dizine gidin ve aşağıdaki komutlarla kurulumu gerçekleştirin:

```
cd reconspider
sudo python3 setup.py install
```

Adım 4 - Veritabanını yapılandırın.

**IP2Proxy Veritabanı**

```
https://lite.ip2location.com/database/px8-ip-proxytype-country-region-city-isp-domain-usagetype-asn-lastseen
```

Veritabanını indirin, arşivden çıkarın ve `reconspider/plugins/` dizinine taşıyın.


# API Anahtarlarının Güncellenmesi

ReconSpider'da bulunan API'ler ÜCRETSİZ olmakla birlikte aylık sınırlı ve kısıtlı kullanım kotasına sahiptir. Lütfen `setup.py` dosyasındaki mevcut API'leri yeni API'lerle güncelleyin ve değişikliklerin geçerli olması için yeniden kurulum yapın.

> Uyarı: API'lerin güncellenmemesi beklenen çıktının görüntülenmemesine veya hata oluşmasına yol açabilir.

Aşağıdaki web sitelerinde hesap oluşturarak API anahtarlarınızı edinmeniz gerekmektedir:

* Shodan.io - https://developer.shodan.io/api
* NumVerify - https://numverify.com/documentation
* IP Stack - https://ipstack.com/documentation
* Google Maps - https://developers.google.com/maps/documentation/places/web-service/get-api-key


# Kullanım

ReconSpider son derece kullanışlı ve kolay kullanımlı bir araçtır. Yapmanız gereken tek şey parametrelere değer girmektir.
ReconSpider'ı başlatmak için şunu yazın:

```
python3 reconspider.py
```

**1. IP**

Bu seçenek, girilen IP adresine ait tüm bilgileri kamuya açık kaynaklardan toplar.

```
ReconSpider >> 1
IP >> 8.8.8.8
```

**2. DOMAIN**

Bu seçenek, girilen URL adresinin tüm bilgilerini toplar ve güvenlik açıklarını kontrol eder.

```
Reconspider >> 2
HOST (URL / IP) >> vulnweb.com
PORT >> 443
```

**3. PHONENUMBER (TELEFON NUMARASI)**

Bu seçenek, girilen telefon numarası hakkında bilgi toplamanızı sağlar.

```
Reconspider >> 3
PHONE NUMBER (919485247632) >>
```

**4. DNS MAP (DNS HARİTASI)**

Bu seçenek, hedef organizasyona ait DNS kayıtlarıyla sanal bir DNS haritası oluşturarak organizasyonun saldırı yüzeyini haritalandırmanızı sağlar.

```
ReconSpider >> 4
DNS MAP (URL) >> vulnweb.com
```

**5. METADATA (ÜST VERİ)**

Bu seçenek, dosyanın tüm meta verilerini çıkarmanızı sağlar.

```
Reconspider >> 5
Metadata (PATH) >> /root/Downloads/images.jpeg
```

**6. REVERSE IMAGE SEARCH (TERS GÖRSEL ARAMA)**

Bu seçenek, internette mevcut olan benzer görselleri ve ilgili bilgileri edinmenizi sağlar.

```
Reconspider >> 6
REVERSE IMAGE SEARCH (PATH) >> /root/Downloads/images.jpeg
Arama sonucu web tarayıcısında açılsın mı? (E/H) : e
```

**7. HONEYPOT (TUZAK SİSTEM)**

Bu seçenek tuzak sistemleri tespit etmenizi sağlar! Bir IP'nin tuzak olma olasılığı, 0.0 ile 1.0 arasında değişen "Honeyscore" değeriyle ölçülür.

```
ReconSpider >> 7
HONEYPOT (IP) >> 1.1.1.1
```

**8. MAC ADDRESS LOOKUP (MAC ADRESİ SORGULAMA)**

Bu seçenek, MAC adresine ait üretici, adres, ülke gibi ayrıntılı bilgileri öğrenmenizi sağlar.

```
Reconspider >> 8
MAC ADDRESS LOOKUP (Ör:08:00:69:02:01:FC) >>
```

**9. IPHEATMAP (IP ISI HARİTASI)**

Bu seçenek, girilen tekli veya çoklu IP adreslerinin konumlarını doğru koordinatlarla birleştirerek ısı haritası oluşturur.

```
Reconspider >> 9

    1) Tek IP izle
    2) Birden fazla IP izle
SEÇENEK >>
```

**10. TORRENT**

Bu seçenek, bir IP adresinin torrent indirme geçmişini toplamanızı sağlar.

```
Reconspider >> 10
IPADDRESS (Ör:192.168.1.1) >>
```

**11. USERNAME (KULLANICI ADI)**

Bu seçenek, girilen kullanıcı adına ait hesap bilgilerini Instagram, Twitter ve Facebook gibi sosyal medya platformlarından toplamanızı sağlar.

```
Reconspider >> 11

1.Facebook
2.Twitter
3.Instagram

Kullanıcı Adı >>
```

**12. IP2PROXY**

Bu seçenek, bir IP adresinin kimliğini gizlemek amacıyla VPN veya Proxy kullanıp kullanmadığını tespit etmenizi sağlar.

```
Reconspider >> 12
IPADDRESS (Ör:192.168.1.1) >>
```

**13. MAIL BREACH (E-POSTA SIKIŞMASI)**

Bu seçenek, girilen domaine ait sızdırılmış tüm e-posta adreslerini tespit etmenizi sağlar.

```
Reconspider >> 13
DOMAIN (Ör:intercom.io) >>
```

**99. UPDATE (GÜNCELLE)**

Bu seçenek güncellemeleri kontrol etmenizi sağlar. Daha yeni bir sürüm mevcutsa ReconSpider, mevcut dosyaların üzerine yazmadan güncellemeleri indirir ve bulunduğunuz dizine entegre eder.

```
ReconSpider >> 99
Güncellemeler kontrol ediliyor..
```

**0. EXIT (ÇIKIŞ)**

Bu seçenek, ReconSpider çerçevesinden çıkarak kullandığınız işletim sisteminin terminaline dönmenizi sağlar.

```
ReconSpider >> 0
Görüşürüz, hoşça kal..
```


# Geliştirici ile İletişim

Özel olarak görüşmek ister misiniz?

    Twitter:            @bhavsec
    Facebook:           fb.com/bhavsec
    Instagram:          instagram.com/bhavsec
    LinkedIn:           linkedin.com/in/bhavsec
    E-posta:            bhavsec@gmail.com
    Web Sitesi:         bhavsec.com


# ReconSpider Tam Wiki ve Kullanım Kılavuzu

Her seçenek ve özelliğin ayrıntılı açıklaması için lütfen [ReconSpider Wiki Kılavuzu](https://github.com/bhavsec/reconspider/wiki)'nu inceleyin.


# Sık ve Kesintisiz Güncellemeler

ReconSpider aktif geliştirme sürecindedir; hata düzeltmeleri, performans iyileştirmeleri ve yeni özellikler için güncellemeler yayımlanmaktadır. Özel hata yönetimi henüz uygulanmamış olup tüm odak, gerekli işlevselliğin oluşturulmasına yöneliktir.


# Özel Teşekkürler ve Katkıda Bulunanlar

* [Aravindha](https://github.com/Aravindha1234u)
* [Ishan Batish](https://www.linkedin.com/in/ishanbatish/)
* [Adithyan AK](https://github.com/adithyan-ak)
* [S0md3v](https://github.com/s0md3v/)
* [Parshant](mailto:parshant.dhall@gmail.com)
