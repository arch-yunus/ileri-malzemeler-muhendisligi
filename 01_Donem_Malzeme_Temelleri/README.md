# 📑 1. Dönem: İleri Malzeme Temelleri & Kuantum Mekaniği

Bu dönem, malzemelerin makroskopik özelliklerini belirleyen atomik, elektronik ve termodinamik temel süreçlerin kuantum mekaniksel ve fizikokimyasal kökenlerini incelemektedir. Amaç, atomlar arası bağlardan başlayarak katıların davranışını matematiksel modellerle tahmin etmektir.

---

## 🎯 Ders Öğrenim Hedefleri
- **Kuantum Yapı Analizi:** Kristal kafeslerde elektronların davranışını periyodik potansiyel modelleriyle çözmek.
- **Termodinamik Kararlılık:** Çok bileşenli faz diyagramlarını Gibbs serbest enerjisi ve kimyasal potansiyel dengesiyle analitik olarak açıklamak.
- **Dönüşüm Kinetiği:** Katı hal difüzyon mekanizmalarını diferansiyel denklemlerle modellemek ve faz dönüşüm oranlarını JMAK kinetiğiyle hesaplamak.

---

## 📖 Kapsamlı Konu Başlıkları & Teknik Detaylar

### 1. Katıhal Fiziği ve Kimyası (Solid State Physics & Chemistry)

Katıların makroskopik mekanik ve elektriksel özellikleri, elektronların kristal kafes içindeki enerji durumlarına bağlıdır.

*   **Bloch Teoremi ve Periyodik Potansiyeller:**
    Kristal kafes periyodik bir yapıya sahip olduğundan, tek bir elektron için potansiyel enerji $V(\vec{r}) = V(\vec{r} + \vec{R})$ bağıntısını sağlar (burada $\vec{R}$ kristal çeviri vektörüdür). Schrödinger denkleminin çözümü olan dalga fonksiyonları Bloch formundadır:
    $$\psi_{\vec{k}}(\vec{r}) = u_{\vec{k}}(\vec{r}) e^{i \vec{k} \cdot \vec{r}}$$
    Burada $u_{\vec{k}}(\vec{r})$ kafes periyoduna sahip fonksiyondur ($u_{\vec{k}}(\vec{r}) = u_{\vec{k}}(\vec{r} + \vec{R})$). Bu bağıntı, katıların bant yapısının teorik temelini oluşturur.

*   **Bant Teorisi (Band Theory) ve Fermi-Dirac Dağılımı:**
    Kovalent veya metalik bağlar oluştukça atomik yörüngeler üst üste biner ve sürekli enerji bantlarını (Valans ve İletkenlik Bantları) oluşturur. Elektronların bu bantlardaki termal dağılımı Fermi-Dirac istatistiği ile tanımlanır:
    $$f(E) = \frac{1}{e^{(E - E_F)/k_B T} + 1}$$
    Burada $E_F$ Fermi enerji seviyesidir. Bu dağılım metallerin, yarı iletkenlerin (sıcaklıkla iletkenlik artışı) ve yalıtkanların temel ayrımını yapar.

*   **Dislokasyon Teorisi ve Peierls-Nabarro Kayma Gerilmesi:**
    Kristal kafesteki dislokasyonların (çizgisel kusurların) hareketi plastik deformasyonu sağlar. Bir dislokasyonun kristal kafeste ilerlemesi için aşması gereken minimum iç direnç olan Peierls-Nabarro gerilmesi ($\tau_{pn}$) şu şekilde formüle edilir:
    $$\tau_{pn} = G \exp\left( -\frac{2\pi a}{b(1-\nu)} \right)$$
    Burada $G$ kayma modülü, $b$ Burger's vektörü, $a$ kafes düzlemleri arası mesafe ve $\nu$ Poisson oranıdır. Bu model, malzemelerin teorik kayma dayanımının neden gerçek dayanımlarından çok daha yüksek olduğunu açıklar.

---

### 2. İleri Malzeme Termodinamiği (Advanced Thermodynamics of Materials)

Malzemelerin hangi fazda bulunacağını ve faz sınırlarının nerede çizileceğini serbest enerji dengesi belirler.

*   **Gibbs Serbest Enerjisi ve Çok Bileşenli Sistemler:**
    Sabit sıcaklık ($T$) ve basınç ($P$) altında bir sistemin kararlılık kriteri Gibbs Serbest Enerjisinin ($G$) minimum olmasıdır:
    $$G = H - TS$$
    Çok bileşenli (örneğin A ve B atomlarından oluşan) katı çözeltilerde, $i$. bileşenin kimyasal potansiyeli ($\mu_i$), sistemin serbest enerjisinin o bileşene göre kısmi türevidir:
    $$\mu_i = \left( \frac{\partial G}{\partial n_i} \right)_{T, P, n_{j \neq i}}$$
    İki fazın ($\alpha$ ve $\beta$) termodinamik dengede olabilmesi için her bir bileşenin kimyasal potansiyeli her iki fazda da eşit olmalıdır:
    $$\mu_A^\alpha = \mu_A^\beta \quad \text{ve} \quad \mu_B^\alpha = \mu_B^\beta$$

*   **Spinodal Ayrışma (Spinodal Decomposition):**
    Geleneksel faz dönüşümlerinde bir çekirdeklenme bariyeri varken, serbest enerjinin bileşime göre ikinci türevinin negatif olduğu bölgede ($\frac{\partial^2 G}{\partial X^2} < 0$) alaşım bariyersiz olarak doğrudan ayrışır. Bu duruma spinodal ayrışma denir ve nano ölçekte homojen dağılımlı fazların eldesinde kritik öneme sahiptir.

---

### 3. Kinetik ve Faz Dönüşümleri (Kinetics & Phase Transformations)

Termodinamik bir faz dönüşümünün gerçekleşebileceğini söylese de, bunun ne kadar sürede gerçekleşeceğini kinetik belirler.

*   **Fick Difüzyon Kanunları:**
    Katı haldeki kütle taşınımı (difüzyon), konsantrasyon gradyanı ile tahrik edilir.
    *   **Fick'in 1. Kanunu (Kararlı Durum):**
        $$J = -D \frac{\partial C}{\partial x}$$
    *   **Fick'in 2. Kanunu (Kararsız Durum):**
        $$\frac{\partial C}{\partial t} = \frac{\partial}{\partial x} \left( D \frac{\partial C}{\partial x} \right)$$
    Burada $D$ difüzyon katsayısı olup sıcaklığa bağımlılığı Arrhenius denklemi ile verilir:
    $$D = D_0 \exp\left( -\frac{Q}{R T} \right)$$
    $Q$ difüzyon aktivasyon enerjisi ($J/mol$), $R$ gaz sabiti ve $T$ mutlak sıcaklıktır ($K$).

*   **Johnson-Mehl-Avrami-Kolmogorov (JMAK) Kinetiği:**
    Katı hal faz dönüşümlerinde (örneğin yeniden kristallenme veya çökelme sertleşmesi) dönüşen faz hacim oranı ($Y$), zamanın ($t$) fonksiyonu olarak S-tipi (sigmoidal) bir eğri izler:
    $$Y = 1 - \exp(-k t^n)$$
    Burada $k$ sıcaklığa bağlı dönüşüm hızı sabiti, $n$ ise çekirdeklenme boyutunu ve büyüme geometrisini tanımlayan Avrami indeksidir. Bu denklem, ısıl işlem sürelerinin endüstriyel ölçekte tasarlanmasında anahtar araçtır.

---

## 🔬 Önerilen Laboratuvar ve Pratik Uygulamalar
1.  **Matlab/Python Modellemesi:** JMAK denklemini kullanarak farklı sıcaklıklar için TTT diyagramlarının oluşturulması ve faz dönüşüm sürelerinin simüle edilmesi.
2.  **Difüzyon Çifti Simülasyonu:** Fick'in 2. Kanunu kullanılarak iki farklı metalin arayüzeyindeki konsantrasyon profilinin zamana bağlı nümerik çözümü.

---
[Ana Sayfaya Dön](../README.md)
