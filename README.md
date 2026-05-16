# 🔬 İleri Malzemeler Müfredatı (Advanced Materials Curriculum)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Level: Academic](https://img.shields.io/badge/Level-Academic--Grade-red.svg)](#)
[![Field: Material Science](https://img.shields.io/badge/Field-Material--Science-green.svg)](#)

Bu depo, geleneksel malzeme biliminin ötesine geçerek; akıllı, nano-yapılı, biyomimetik ve ekstrem koşullara dayanıklı yeni nesil malzemelerin tasarım, sentez, karakterizasyon ve hesaplamalı simülasyon süreçlerini kapsayan disiplinlerarası bir mühendislik müfredatıdır.

Müfredat, hem teorik altyapıyı sağlamlaştırmak hem de günümüz endüstrisinin (havacılık, uzay, savunma, yarı iletkenler, enerji) ihtiyaç duyduğu pratik ve dijital becerileri (DFT, Moleküler Dinamik, Yapay Zeka) kazandırmak amacıyla 4 ana dönem (blok) halinde tasarlanmıştır.

---

## 🏗 Klasör Yapısı (Directory Structure)

Proje deposunun organize ve sürdürülebilir olması için aşağıdaki klasör mimarisi esas alınmıştır:

```text
ileri-malzemeler-mufredati/
├── README.md                          # Müfredat genel tanımı ve yol haritası
├── 01_Donem_Malzeme_Temelleri/        # Katıhal fiziği, termodinamik, kinetik
├── 02_Donem_Nano_ve_Akilli/           # Nanomalzemeler, metamalzemeler, akıllı yapılar
├── 03_Donem_Kompozit_ve_Ekstrem/      # İleri kompozitler, UHTC, FGM, biyomimetik
├── 04_Donem_Hesaplamali_Malzeme/      # DFT, MD simülasyonları, Malzeme Yapay Zekası
├── kaynaklar/                         # Akademik yayınlar, kitap listeleri, açık kaynak kodlar
└── görseller/                         # Tasarım varlıkları ve diyagramlar
```

---

## ⚡ Hızlı Erişim

| Kaynak | Açıklama |
| :--- | :--- |
| 📖 [Teknik Sözlük](./SOZLUK.md) | İleri malzeme terimleri ve tanımları |
| 🚀 [Vaka Çalışmaları](./03_Donem_Kompozit_ve_Ekstrem/VAKA_CALISMALARI.md) | Gerçek dünya uygulama örnekleri |
| 🎓 [Bitirme Projesi](./04_Donem_Hesaplamali_Malzeme/PROJE_REHBERI.md) | Proje geliştirme ve uygulama rehberi |
| 💻 [Simülasyon Araçları](./04_Donem_Hesaplamali_Malzeme/scripts) | Python tabanlı hesaplama araçları |

---

## 🎓 Detaylı Müfredat İçeriği

### 1. Dönem: İleri Malzeme Temelleri & Kuantum Mekaniği

Bu dönem, malzemelerin atomik, elektronik ve termodinamik düzeydeki davranışlarını anlamaya odaklanır. Makroskopik özelliklerin arkasındaki mikroskobik fiziği çözmeyi amaçlar.

*   **Katıhal Fiziği ve Kimyası:**
    *   Kristal yapı kusurları (Noktasal, çizgisel ve arayüzey kusurları) ve malzeme özelliklerine etkileri.
    *   Bant teorisi (Band Theory): Metaller, yarı iletkenler ve yalıtkanların elektronik yapısı.
    *   Reciprocal (Ters) örgü uzayı ve Brillouin bölgeleri.

*   **İleri Malzeme Termodinamiği:**
    *   Çok bileşenli sistemlerde faz dengeleri ve serbest enerji-bileşim diyagramları.
    *   Eriyelik (solubility) limitleri, ara fazlar ve nano-ölçekte termodinamik kararlılık dalgalanmaları.

*   **Kinetik ve Faz Dönüşümleri:**
    *   Katı hal difüzyon mekanizmaları (Fick Kanunları, atomik sıçrama teorileri).
    *   Çekirdeklenme (homojen/heterojen) ve büyüme kinetiği, TTT (Zaman-Sıcaklık-Dönüşüm) diyagramları.

---

### 2. Dönem: Nanomalzemeler ve Akıllı Yapılar

Ölçek küçüldükçe baskın hale gelen kuantum etkileri ile dış uyarılara (elektrik, manyetik, mekanik, sıcaklık) kontrollü tepki veren fonksiyonel malzemeler incelenir.

*   **Nanoteknoloji ve Düşük Boyutlu Malzemeler:**
    *   2D Malzemeler (Grafen, Bor Nitrür, MXene'ler) ve sentez yöntemleri (CVD, eksfoliasyon).
    *   1D Karbon Nanotüpler (CNT) ve 0D Kuantum Noktaları (Quantum Dots).
    *   Yüzey/hacim oranının artmasıyla değişen kimyasal reaktivite ve optik özellikler.

*   **Akıllı (Smart) Malzemeler:**
    *   Şekil Hafızalı Alaşımlar (SMA) ve martenzitik faz dönüşümleri.
    *   Piezoelektrik ve Ferroelektrik malzemeler: Sensör ve aktüatör mekanizmaları.
    *   Manyetorelojik ve Elektrorelojik sıvılar: Akışkanlık kontrolü.

*   **Metamalzemeler (Metamaterials):**
    *   Doğada bulunmayan elektromanyetik ve akustik özelliklerin tasarımı.
    *   Negatif kırılma indisli yapılar, sol-elli (left-handed) malzemeler ve akustik pelerinleme (cloaking).

---

### 3. Dönem: İleri Kompozitler ve Ekstrem Ortam Malzemeleri

Yüksek mukavemet/ağırlık rasyosu gerektiren yapılar ile ekstrem koşullara (yüksek radyasyon, 2000°C üzeri sıcaklıklar, korozif ortamlar) dayanıklı sistemlerin tasarımı.

*   **Fonksiyonel Derecelendirilmiş Malzemeler (Functionally Graded Materials - FGM):**
    *   Mikroyapısı veya bileşimi hacimsel olarak gradyanlı değişen heterojen malzemeler.
    *   Termal gerilmeleri azaltma mekanizmaları ve üretim teknikleri (Katmanlı imalat, toz metalurjisi).

*   **Ultra Yüksek Sıcaklık Seramikleri (UHTC):**
    *   Hipersonik uçuşlar, roket nozulları ve atmosfer yeniden giriş (re-entry) araçları için malzeme tasarımı.
    *   Hafniyum Diborür (HfB2), Zirkonyum Diborür (ZrB2) ve Karbon-Karbon kompozitleri.

*   **Ekstrem Ortam Malzemeleri:**
    *   Nükleer reaktörler için radyasyon hasarına (şişme, gevrekleşme) dirençli alaşımlar.
    *   Kriyojenik sıcaklıklarda yüksek tokluk gösteren yüksek entropi alaşımları (HEA).

*   **Biyomimetik ve Kendi Kendini Onaran Malzemeler:**
    *   Doğadaki yapılardan (sedef mikroyapısı, lotus yaprağı) esinlenilen mikro/nano mimariler.
    *   Mikrokapsül veya vasküler ağ içeren kendi kendini iyileştiren polimerler ve betonlar.

---

### 4. Dönem: Hesaplamalı Malzeme Bilimi & Malzeme Yapay Zekası

Deney öncesi malzeme özelliklerini tahmin etmek, atomik seviyede mekanizmaları incelemek ve veri odaklı yeni malzemeler keşfetmek için kullanılan dijital araçlar.

*   **Elektronik Seviye Modelleme (Yoğunluk Fonksiyonu Teorisi - DFT):**
    *   Schrödinger denkleminin çözümü, Hohenberg-Kohn teoremleri ve Kohn-Sham yaklaşımı.
    *   Bant yapısı (Band structure), Durum Yoğunluğu (DOS) analizi ve elastik sabitlerin hesaplanması.

*   **Atomik Seviye Modelleme (Moleküler Dinamik - MD):**
    *   Newton'un hareket denklemlerinin entegrasyonu, potansiyel fonksiyonları (EAM, ReaxFF).
    *   Çekme, basma, termal iletkenlik ve faz dönüşümlerinin nano saniye ölçeğinde simülasyonu.

*   **Malzeme Bilişimi (Materials Informatics):**
    *   Malzeme veri tabanlarının (Materials Project, OQMD, Citrination) kullanımı.
    *   Öznitelik mühendisliği (Compositional & Structural descriptors).
    *   Makine öğrenmesi (Rastgele Orman, Sinir Ağları) algoritmaları ile hızlı kristal yapı ve özellik tahmini.

---

## 🛠 Laboratuvar, Yazılım ve Araç Seti (Toolset)

Müfredatın pratik bacağında öğrencilerin ve araştırmacıların aşağıdaki araçlarda yetkinleşmesi hedeflenmektedir:

*   **Hesaplamalı Araçlar:**
    *   `LAMMPS`: Klasik Moleküler Dinamik simülasyonları.
    *   `Quantum ESPRESSO` / `VASP`: DFT tabanlı kuantum mekaniksel hesaplamalar.
    *   `OVITO` / `VMD`: Atomik simülasyon verilerinin görselleştirilmesi ve analizi.
    *   `ASE (Atomic Simulation Environment)`: Python ile atomik yapıların manipülasyonu.

*   **Sonlu Elemanlar Analizi (FEA):**
    *   `Abaqus` / `Ansys`: Makroskopik düzeyde kompozit ve akıllı malzemelerin mekanik ve termal simülasyonu.

*   **Karakterizasyon (Teorik ve Veri Analizi Bazlı):**
    *   XRD veri analizi için `HighScore Plus` veya açık kaynaklı alternatifler.
    *   SEM/TEM mikroyapı analizleri için `ImageJ`.

---

## 📚 Kaynak Kitaplar ve Akademik Referanslar

1.  *Introduction to Solid State Physics* - Charles Kittel
2.  *Thermodynamics of Materials* - David R. Gaskell
3.  *Phase Transformations in Metals and Alloys* - D.A. Porter, K.E. Easterling
4.  *Introduction to Nanotechnology* - Charles P. Poole Jr., Frank J. Owens
5.  *Computational Materials Science: An Introduction* - June Gunn Lee

---

## 💼 Kariyer Yolları ve Endüstriyel Uygulama

Bu müfredatı tamamlayan bireyler aşağıdaki sektörlerde uzmanlaşabilir:
- **Havacılık ve Uzay:** Hafif kompozit yapılar ve yüksek sıcaklık alaşımları uzmanlığı.
- **Biyomedikal:** İmplant tasarımı ve biyomimetik malzeme geliştirme.
- **Yarı İletken ve Elektronik:** Nano ölçekli cihazlar ve akıllı yüzeyler.
- **Enerji Sektörü:** Yeni nesil batarya ve hidrojen depolama sistemleri.

---

## 🤝 Katkıda Bulunma (Contributing)

Bu müfredat, malzeme bilimindeki gelişmelere paralel olarak sürekli güncellenen açık kaynaklı dinamik bir yapıdır.

*   Yeni ders içerikleri, laboratuvar föyleri veya Python analiz scriptleri eklemek için lütfen bir **Pull Request (PR)** açın.
*   Müfredatta eksik olduğunu düşündüğünüz konular veya kaynak önerileri için **Issues** sekmesini kullanabilirsiniz.

---
<p align="center">
  <i>Geleceği şekillendiren malzemeleri bugün öğrenin.</i><br>
  <b>İleri Malzemeler Akademisi © 2026</b>
</p>