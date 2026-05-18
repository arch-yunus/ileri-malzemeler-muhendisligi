# 💻 4. Dönem: Hesaplamalı Malzeme Bilimi & Malzeme Yapay Zekası

Bu dönem, malzemelerin özelliklerini laboratuvar sentezinden önce atomik, moleküler ve elektronik seviyelerde tahmin etmek, simüle etmek ve veri odaklı yapay zeka yaklaşımlarıyla yeni nesil malzemeler tasarlamak için kullanılan modern dijital metodolojileri kapsamaktadır.

---

## 🎯 Ders Öğrenim Hedefleri
- **Kuantum Mekaniksel Modelleme:** Yoğunluk Fonksiyonu Teorisi (DFT) temellerini ve Kohn-Sham denklemlerinin self-consistent field (SCF) çözüm yöntemlerini kavramak.
- **Kinetik Simülasyonlar:** Moleküler Dinamik (MD) entegrasyon algoritmalarını kurabilmek ve atomlar arası potansiyel modellerini amaca uygun seçmek.
- **Yapay Zeka & Veri Madenciliği:** Büyük malzeme veritabanlarını kullanarak öznitelik mühendisliği (descriptors) geliştirmek ve kristal yapı özelliklerini tahmin eden makine öğrenmesi modelleri eğitmek.

---

## 📖 Kapsamlı Konu Başlıkları & Teknik Detaylar

### 1. Elektronik Seviye Modelleme: Yoğunluk Fonksiyonu Teorisi (DFT)

Çok elektronlu bir sistemde Schrödinger denkleminin analitik olarak çözülmesi, elektronlar arası Coulomb etkileşiminden dolayı imkansızdır ($3N$ boyutlu dalga fonksiyonu problemi). DFT, sistemi dalga fonksiyonu yerine 3 boyutlu elektron yoğunluğu ($n(\vec{r})$) cinsinden çözerek bu karmaşıklığı azaltır.

*   **Hohenberg-Kohn Teoremleri:**
    1. Sistemin taban durumu (ground state) özellikleri, elektron yoğunluğunun ($n(\vec{r})$) tek değerli bir fonksiyonelidir.
    2. Doğru taban durumu elektron yoğunluğu, toplam enerjiyi minimize eden yoğunluktur.

*   **Kohn-Sham Denklemleri:**
    Etkileşimli elektron sistemini, efektif bir potansiyel ($V_{eff}$) içinde hareket eden etkileşimsiz hayali parçacıklar sistemine dönüştüren tek-parçacık Schrödinger denklemleridir:
    $$\left[ -\frac{1}{2}\nabla^2 + V_{eff}(\vec{r}) \right] \psi_i(\vec{r}) = \epsilon_i \psi_i(\vec{r})$$
    Efektif potansiyel terimi şu üç potansiyelin toplamıdır:
    $$V_{eff}(\vec{r}) = V_{ext}(\vec{r}) + V_H(\vec{r}) + V_{xc}(\vec{r})$$
    *   $V_{ext}(\vec{r})$: Çekirdeklerin elektronlara uyguladığı dış Coulomb potansiyeli.
    *   $V_H(\vec{r})$: Elektronlar arası klasik Hartree itme potansiyeli ($\nabla^2 V_H = -4\pi n$).
    *   $V_{xc}(\vec{r})$: Elektronlar arası kuantum mekaniksel Değiş-Tokuş ve Korelasyon (Exchange-Correlation) potansiyeli ($V_{xc} = \frac{\partial E_{xc}}{\partial n}$).

*   **Değiş-Tokuş Korelasyon Fonksiyonelleri:**
    *   **Yerel Yoğunluk Yaklaşımı (Local Density Approximation - LDA):** Yoğunluğun uzayda homojen olduğunu varsayar.
    *   **Genelleştirilmiş Gradyan Yaklaşımı (Generalized Gradient Approximation - GGA - PBE):** Yoğunluğun gradyanını da hesaba katar (yarı iletkenler ve metaller için standart).

---

### 2. Atomik Seviye Modelleme: Moleküler Dinamik (MD)

Moleküler Dinamik, atomların klasik Newton hareket denklemlerinin sayısal olarak entegre edilmesine dayanır. nanosaniye ölçeğinde sıcaklık, basınç ve mekanik gerilim tepkilerini modeller.

*   **Velocity Verlet Entegrasyon Algoritması:**
    MD simülasyonlarında her zaman adımında ($\Delta t \approx 1\text{ fs}$) atomların yeni konumları ($\vec{r}$) ve hızları ($\vec{v}$) şu denklemlerle güncellenir:
    $$\vec{r}(t + \Delta t) = \vec{r}(t) + \vec{v}(t)\Delta t + \frac{1}{2}\vec{a}(t)\Delta t^2$$
    $$\vec{v}(t + \Delta t) = \vec{v}(t) + \frac{1}{2} \left[ \vec{a}(t) + \vec{a}(t + \Delta t) \right] \Delta t$$
    Burada ivme ($\vec{a}$), atomlar arası potansiyel enerjinin ($U$) gradyanından (kuvvet $\vec{F} = m\vec{a} = -\nabla U$) elde edilir.

*   **Atomlar Arası Potansiyel Fonksiyonları (Force Fields):**
    *   **Lennard-Jones (LJ) Potansiyeli:** Soy gazlar ve van der Waals etkileşimleri için.
        $$U(r) = 4\epsilon \left[ \left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6 \right]$$
    *   **Gömülü Atom Yöntemi (Embedded Atom Method - EAM):** Metaller ve alaşımlar için elektron bulutu katkısını da içeren gelişmiş potansiyel.
    *   **ReaxFF (Reaksiyon Kuvvet Alanı):** Bağ kırılması ve oluşumunu modelleyen kimyasal reaktif potansiyel.

---

### 3. Malzeme Bilişimi (Materials Informatics)

*   **Veritabanı Madenciliği:**
    `Materials Project`, `AFLOW` ve `OQMD` gibi büyük veritabanlarından yüksek verimli tarama (High-Throughput Screening) ile istenen özelliklere (örn: yüksek elastik modül, optimal bant aralığı) sahip kararlı kristallerin keşfi.

*   **Malzeme Tanımlayıcıları (Material Descriptors):**
    Kristal yapıyı veya bileşimi yapay zeka modellerinin anlayabileceği vektörel formata dönüştürme yöntemleri:
    *   **SOAP (Smooth Overlap of Atomic Positions):** Atomların yerel çevre topolojisini Gauss fonksiyonları ile tanımlar.
    *   **Coulomb Matrix:** Moleküllerin elektrostatik etkileşim matrisi representation'ı.

*   **Özellik Tahmini:**
    Öznitelikler hazırlandıktan sonra, Rastgele Orman (Random Forest), GBDT (Gradient Boosting) veya Kristal Grafik Sinir Ağları (CGCNN) ile deneysel verilere ihtiyaç kalmadan bant aralığı, örgü parametreleri ve oluşum enerjisi tahmini.

---

## 🔬 Önerilen Laboratuvar ve Pratik Uygulamalar
1.  **Quantum ESPRESSO Uygulaması:** Silisyum (Si) veya Alüminyum (Al) kristalinin örgü parametresini bulmak için DFT tabanlı hacim-enerji optimizasyonu (Murnaghan durum denklemi fit'i) yapılması.
2.  **LAMMPS Uygulaması:** EAM potansiyeli kullanarak Bakır (Cu) nano-telinin çekme testi simülasyonu ve stress-strain eğrisinin elde edilmesi.

---
[Ana Sayfaya Dön](../README.md)
