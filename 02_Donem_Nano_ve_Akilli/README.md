# 🌀 2. Dönem: Nanomalzemeler ve Akıllı Yapılar

Bu dönem, ölçek etkisinin (size effect) malzemenin fiziksel ve kimyasal özelliklerini nasıl domine ettiğini ve dış uyarıcılara (sıcaklık, mekanik stres, elektrik/manyetik alanlar) dinamik olarak tepki verebilen fonksiyonel akıllı sistemlerin tasarım prensiplerini kapsamaktadır.

---

## 🎯 Ders Öğrenim Hedefleri
- **Kuantum Sınırlandırma (Quantum Confinement):** Boyut küçülmesinin elektronik ve optik özellikler üzerindeki etkisini matematiksel Durum Yoğunluğu (DOS) modelleriyle kavramak.
- **Aktif Malzeme Karakterizasyonu:** Şekil hafızalı alaşımlar ve piezoelektrik sistemlerin elektro-mekanik-termal dönüşüm denklemlerini kurabilmek.
- **Elektromanyetik Metamalzemeler:** Doğada bulunmayan negatif kırılma indisli yapıların dalga yayılım davranışlarını Maxwell denklemleriyle analiz etmek.

---

## 📖 Kapsamlı Konu Başlıkları & Teknik Detaylar

### 1. Nanoteknoloji ve Düşük Boyutlu Malzemeler (Low-Dimensional Materials)

Boyut nano ölçeğe (1-100 nm) indiğinde, malzemelerin yüzey alanı/hacim oranı katlanarak artar ve elektron dalga boyu malzemenin fiziksel boyutlarıyla kıyaslanabilir hale geldiğinden kuantum sınırlandırma başlar.

*   **Boyuta Göre Durum Yoğunluğu (Density of States - DOS) Denklemleri:**
    Birim hacim ve birim enerji aralığındaki elektron durumlarının sayısını tanımlayan $N(E)$ fonksiyonu, malzemenin boyutuna göre köklü değişim gösterir:
    *   **3D Hacimsel Malzeme (Bulk):** Sürekli enerji seviyeleri.
        $$N(E) = \frac{1}{2\pi^2} \left( \frac{2m^*}{\hbar^2} \right)^{3/2} E^{1/2} \propto \sqrt{E}$$
    *   **2D Kuantum Kuyusu (Quantum Well - Grafen, MXene):** Basamaklı yapı.
        $$N(E) = \frac{m^*}{\pi \hbar^2} \sum_{i} \theta(E - E_i)$$
    *   **1D Kuantum Teli (Quantum Wire - CNT):** Tekil uçlar (Van Hove singularities).
        $$N(E) = \frac{1}{\pi \hbar} \left( \frac{2m^*}{E - E_i} \right)^{1/2} \propto \frac{1}{\sqrt{E}}$$
    *   **0D Kuantum Noktası (Quantum Dot):** Kesikli delta fonksiyonları (yapay atomlar).
        $$N(E) = 2 \sum_{i} \delta(E - E_i)$$
    *(Burada $m^*$ elektronun etkin kütlesi, $\hbar$ indirgenmiş Planck sabiti ve $\theta(x)$ Heaviside basamak fonksiyonudur).*

*   **Sentez Kinetiği (Kimyasal Buhar Biriktirme - CVD):**
    Grafen veya karbon nanotüp sentezinde, gaz fazındaki prekürsörlerin metal katalizör (Ni, Cu) yüzeyinde ayrışması, adsorpsiyonu ve yüzey difüzyonu termodinamik çekirdeklenme hızıyla kontrol edilir. Sıcaklık ve gaz kısmi basınç oranları ($H_2 / CH_4$) kristal kalitesini belirler.

---

### 2. Akıllı (Smart) Malzemeler

Akıllı malzemeler, fiziksel uyarılara geri dönüştürülebilir yapısal veya faz değişim tepkileri verir.

*   **Şekil Hafızalı Alaşımlar (SMA) ve Clausius-Clapeyron Termodinamiği:**
    Nitinol ($NiTi$), yüksek sıcaklıktaki simetrik kübik **Ostenit (A)** fazından, düşük sıcaklıktaki düşük simetrili monoklinik **Martenzit (M)** fazına difüzyonsuz (kesme modlu) olarak dönüşür. Uygulanan mekanik stres ($\sigma$) ile martenzit başlangıç sıcaklığı ($M_s$) arasındaki ilişki Clausius-Clapeyron bağıntısı ile açıklanır:
    $$\frac{d\sigma}{dT} = -\frac{\Delta H_{tr}}{T_0 \cdot \varepsilon_{tr}}$$
    Burada $\Delta H_{tr}$ faz dönüşüm gizli ısısı, $\varepsilon_{tr}$ dönüşüm birim şekil değişimi ve $T_0$ denge sıcaklığıdır.

*   **Piezoelektriklik Bünye Denklemleri (Constitutive Equations):**
    Piezoelektrik malzemeler (örn: $Pb(Zr, Ti)O_3$ - PZT, $BaTiO_3$), simetri merkezine sahip olmayan kristallerdir. Mekanik gerilme ($\sigma$) uygulandığında elektrik polarizasyonu ($D$) oluşur (doğrudan etki) veya elektrik alanı ($E$) uygulandığında mekanik şekil değişimi ($S$) meydana gelir (ters etki):
    $$D_i = d_{ijk} \sigma_{jk} + \varepsilon_{ij}^T E_j$$
    $$S_{ij} = s_{ijkl}^E \sigma_{kl} + d_{kij} E_k$$
    Burada $d_{ijk}$ piezoelektrik katsayı tensörü, $s_{ijkl}^E$ sabit elektrik alanındaki elastik uyumluluk tensörü ve $\varepsilon_{ij}^T$ sabit gerilmedeki dielektrik geçirgenlik tensörüdür.

---

### 3. Metamalzemeler (Metamaterials)

Metamalzemeler, özelliklerini kimyasal bileşimlerinden değil, yapay olarak tasarlanmış periyodik birim hücre geometrilerinden (alt-dalga boyu rezonatörler) alırlar.

*   **Negatif Kırılma İndisi ($n < 0$) ve Maxwell Denklemleri:**
    Doğadaki malzemelerin dielektrik geçirgenliği ($\varepsilon$) ve manyetik geçirgenliği ($\mu$) pozitiftir. Yapay split-ring rezonatörler ve tel ızgaralar kullanılarak belirli bir frekans bandında hem $\varepsilon < 0$ hem de $\mu < 0$ elde edilebilir. Bu durumda kırılma indisi negatif olur:
    $$n = -\sqrt{\varepsilon_r \mu_r}$$
    Bu sol-elli (left-handed) ortamlarda, Poynting vektörü ($\vec{S} = \vec{E} \times \vec{H}$) ile dalga vektörü ($\vec{k}$) zıt yönlüdür. Işık kaynağa doğru bükülür, bu da mükemmel lenslerin (superlens) ve görünmezlik pelerinlerinin (cloaking) temelini oluşturur.

---

## 🔬 Önerilen Laboratuvar ve Pratik Uygulamalar
1.  **Finite Element Method (FEM) Simülasyonu:** Ansys veya Abaqus kullanılarak piezoelektrik bir konsol kirişin (cantilever) mekanik titreşim altında ürettiği voltajın (enerji hasadı - energy harvesting) simüle edilmesi.
2.  **Karakterizasyon Analizi:** Şekil hafızalı alaşımın DSC (Diferansiyel Taramalı Kalorimetri) eğrilerinden faz geçiş sıcaklıklarının ($A_s, A_f, M_s, M_f$) ve latent ısıların hesaplanması.

---
[Ana Sayfaya Dön](../README.md)
