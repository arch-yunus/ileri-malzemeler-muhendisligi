# 🎓 İleri Malzemeler Akademisi: Bitirme Projesi Rehberi

Bu rehber, müfredat süresince edindiğiniz teorik ve pratik (özellikle hesaplamalı) bilgi birikimini, özgün bir malzeme bilimi veya mühendisliği problemi üzerinde sentezleyerek çözmenizi hedefleyen bitirme projesinin standartlarını, şablonlarını ve değerlendirme kriterlerini içermektedir.

---

## 📅 Proje Geliştirme Aşamaları ve Zaman Çizelgesi

### 1. Aşama: Konu Seçimi ve Problem Tanımı (Hafta 1-2)
Aşağıdaki tematik alanlardan birini seçerek odaklanmış bir araştırma sorusu belirleyin:
*   **Hesaplamalı Tasarım:** Belirli bir alaşımın veya 2D yapının (örn: MXene) bant yapısını DFT ile veya mekanik/termal özelliklerini MD simülasyonları ile incelemek.
*   **Ekstrem Ortam Tasarımı:** Belirli bir havacılık/uzay bileşeni (örn: roket nozulu) için FGM veya UHTC esaslı malzeme katman tasarımı ve termal gerilme analizi.
*   **Biyomimetik Çözümler:** Lotus etkisi veya kemik implantı uyumu için yüzey mikro-nano yapısının modellenmesi.

### 2. Aşama: Literatür Taraması ve Kritik Analiz (Hafta 3-4)
*   Seçilen konuyla ilgili Web of Science veya Google Scholar üzerinden en az 8 adet yüksek etki faktörlü (high impact) akademik makaleyi inceleyin.
*   Mevcut literatürdeki "bilgi boşluğunu" (knowledge gap) ve sizin projenizin bu boşluğu nasıl dolduracağını raporunuzda açıkça temellendirin.

### 3. Aşama: Simülasyon, Modelleme ve Veri Analizi (Hafta 5-8)
*   Önerilen araçları (`Quantum ESPRESSO`, `LAMMPS`, `Abaqus`, Python vb.) kullanarak simülasyonlarınızı veya analitik hesaplamalarınızı koşturun.
*   Elde edilen simülasyon sonuçlarının yakınsamasını (convergence) test edin ve fiziksel olarak anlamlılığını irdeleyin.

### 4. Aşama: Teknik Raporlama ve Sunum (Hafta 9-10)
*   Teknik raporunuzu aşağıda verilen uluslararası standartlardaki LaTeX veya Markdown şablonuna göre yazın.
*   Projenizi akademik jüri önünde 15 dakikalık teknik bir sunumla savunun.

---

## 📝 Teknik Rapor Standart Yapısı

Proje raporunuzun aşağıdaki bölümlerden oluşması zorunludur:
1.  **Özet (Abstract):** Araştırma probleminin, yöntemin ve elde edilen en kritik nicel sonucun 250 kelimeyi geçmeyen özeti.
2.  **Giriş (Introduction):** Konunun arka planı, literatür özeti, araştırma hipotezi ve motivasyon.
3.  **Yöntem (Methodology):** Kullanılan modelleme veya deneysel yöntemlerin tüm parametreleri (örn: DFT için cutoff enerjisi, k-noktaları; MD için zaman adımı, ensemble tipi).
4.  **Bulgular ve Tartışma (Results & Discussion):** Elde edilen verilerin grafikler, tablolar ve diyagramlarla sunulması, literatür verileri ile karşılaştırılması ve fiziksel analizi.
5.  **Sonuçlar (Conclusions):** Çalışmadan çıkarılan temel yargılar ve gelecek çalışmalar için öneriler.
6.  **Referanslar (References):** IEEE veya APA formatında hazırlanmış kaynakça listesi.

---

## 💻 Hesaplamalı Araçlar İçin Girdi (Input) Şablonları

Öğrencilerin hesaplamalı projelerinde referans alabilecekleri standart girdi kod mimarileri aşağıda paylaşılmıştır:

### 1. Yoğunluk Fonksiyonu Teorisi (DFT) - Quantum ESPRESSO Giriş Şablonu
Aşağıdaki girdi dosyası (`Si.scf.in`), Silisyum (Si) kristalinin taban durumu enerjisini hesaplamak için self-consistent field (SCF) kuantum mekaniksel simülasyon kodudur:

```text
&CONTROL
    calculation = 'scf'
    restart_mode = 'from_scratch'
    prefix = 'silicon'
    pseudo_dir = './pseudo/'
    outdir = './out/'
/
&SYSTEM
    ibrav = 2,                     ! Face-Centered Cubic (FCC) kafes yapısı
    celldm(1) = 10.26,             ! Örgü parametresi (Bohr cinsinden)
    nat = 2,                       ! Birim hücredeki toplam atom sayısı
    ntyp = 1,                      ! Atom türü sayısı (Sadece Si)
    ecutwfc = 40.0,                ! Dalga fonksiyonu kinetik enerji cutoff (Ry)
/
&ELECTRONS
    conv_thr = 1.0d-8,             ! SCF yakınsama kriteri (Ry)
    mixing_beta = 0.7,
/
ATOMIC_SPECIES
 Si  28.086  Si.pbe-n-kjpaw_psl.1.0.0.UPF  ! Atom sembolü, kütlesi ve pseudopotential dosyası
ATOMIC_POSITIONS (alat)
 Si 0.00 0.00 0.00
 Si 0.25 0.25 0.25
K_POINTS (automatic)
 4 4 4 1 1 1                       ! Monkhorst-Pack k-noktaları kafesi ve kayması
```

---

### 2. Moleküler Dinamik (MD) - LAMMPS Giriş Şablonu
Aşağıdaki girdi dosyası (`in.tensile`), Bakır (Cu) nano-bloğunun oda sıcaklığında tek eksenli çekme testi simülasyonunu koşturarak mekanik stress-strain verilerini üretir:

```text
# --- Klasik Bakır Nano-Blok Çekme Testi Simülasyonu ---
units           metal
boundary        p p p             # Üç boyutta periyodik sınır koşulları
atom_style      atomic

# --- Kristal Yapı Tanımlama ---
lattice         fcc 3.615         # Bakır örgü sabiti (Angstrom)
region          box block 0 10 0 10 0 10
create_box      1 box
create_atoms    1 box

# --- Potansiyel Tanımlama (EAM) ---
pair_style      eam/alloy
pair_coeff      * * Cu_u3.eam.alloy Cu  # Bakır EAM alaşım potansiyeli

# --- Termodinamik Dengeleme (Relaxation) ---
velocity        all create 300.0 12345 dist gaussian
fix             1 all npt temp 300.0 300.0 1.0 iso 0.0 0.0 10.0
thermo          100
run             5000              # 5 ps dengeleme koşusu
unfix           1

# --- Çekme Testi (Deformasyon) ---
# Y ekseninde saniyede 10^9 oranında çekme uygulama
fix             2 all npt temp 300.0 300.0 1.0 x 0.0 0.0 10.0 z 0.0 0.0 10.0
fix             3 all deform 1 y erate 0.001 units box

# --- Çıktı Parametreleri ---
variable        strain equal "(ly - ly0) / ly0"
variable        stress equal "-pyy / 10000"  # GPa cinsinden stres dönüşümü
thermo_style    custom step temp v_strain v_stress press vol
thermo          200

# --- Simülasyonu Çalıştır ---
run             10000             # 10 ps deformasyon koşusu
```

---

## 🏆 Değerlendirme Kriterleri (Rubrik)

Bitirme projeleri jüri tarafından aşağıdaki ağırlıklarla 100 puan üzerinden değerlendirilecektir:

| Kriter | Ağırlık | Beklenti |
| :--- | :--- | :--- |
| **Literatür & Problem Tanımı** | %15 | Problemin güncelliği, literatürdeki boşluğun tespiti ve hipotezin netliği. |
| **Metodolojik Uygunluk** | %25 | Hesaplama parametrelerinin (DFT/MD) doğruluğu, yakınsama testlerinin yapılması. |
| **Veri Analizi & Fiziksel İrdeleme**| %30 | Elde edilen grafiklerin malzeme bilimi teorileriyle (örneğin faz dönüşümleri, dislokasyon hareketi) derinlemesine açıklanması. |
| **Rapor Kalitesi & Yapı** | %15 | Raporun akademik dil kalitesi, yazım kurallarına uygunluğu ve referansların eksiksizliği. |
| **Sunum & Savunma** | %15 | Süreye uyum, sunum görselliği ve jüri sorularına verilen teknik cevaplar. |

---
[Ana Sayfaya Dön](../README.md)
