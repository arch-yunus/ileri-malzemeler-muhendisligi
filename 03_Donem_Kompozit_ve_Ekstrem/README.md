# 🏗 3. Dönem: İleri Kompozitler ve Ekstrem Ortam Malzemeleri

Bu dönem, yüksek mukavemet/ağırlık oranına sahip çok fazlı hiyerarşik yapıların tasarımı ile aşırı yüksek sıcaklıklar ($>2000^\circ\text{C}$), yoğun radyasyon hasarı ve kriyojenik ortamlar gibi ekstrem koşullara dayanıklı ileri düzey malzeme sistemlerini incelemektedir.

---

## 🎯 Ders Öğrenim Hedefleri
- **Heterojen Yapı Tasarımı:** Fonksiyonel Derecelendirilmiş Malzemelerin (FGM) hacim oranlarını ve termal gerilme dağılımlarını matematiksel modellerle optimize etmek.
- **Ekstrem Ortam Kimyası:** Ultra yüksek sıcaklık seramiklerinin oksidasyon koruma mekanizmalarını ve nükleer alaşımların radyasyon hasarı modellerini çözmek.
- **Biyomimetik Mühendislik:** Doğadaki hiyerarşik yapıları modelleyerek ıslanmazlık ve kendi kendini onarma (self-healing) kinetiği gibi fonksiyonellikleri sentetik malzemelere aktarmak.

---

## 📖 Kapsamlı Konu Başlıkları & Teknik Detaylar

### 1. İleri Kompozitler & Fonksiyonel Derecelendirilmiş Malzemeler (FGM)

Geleneksel kompozitlerdeki keskin arayüzeyler, yüksek sıcaklıklarda ısıl genleşme farkından dolayı gerilme yığılmalarına ve delaminasyona (tabaka ayrılmasına) neden olur.

*   **FGM Gradyan Profil Denklemleri (Güç Yasası - Power Law):**
    FGM yapılarında bileşim (örneğin metalden seramiğe) kalınlık boyunca gradyanlı olarak değişir. Seramik fazının hacimsel oranı ($V_c$), kalınlık yönündeki koordinata ($z$) bağlı olarak genellikle şu Güç Yasası (Power Law) ile formüle edilir:
    $$V_c(z) = \left( \frac{z + h/2}{h} \right)^n$$
    Burada $h$ plaka kalınlığı, $z \in [-h/2, h/2]$ kalınlık koordinatı ve $n$ gradyan indeksidir ($n \rightarrow 0$ saf seramik, $n \rightarrow \infty$ saf metal limitini verir). Lokal malzeme özellikleri (elastik modül $E(z)$, termal genleşme katsayısı $\alpha(z)$) bu hacim oranına göre Karışımlar Kuralı (Rule of Mixtures) ile hesaplanır.

*   **Isıl Gerilme Minimizasyonu:**
    Gradyanlı yapı sayesinde arayüzeylerdeki $\sigma_{thermal} \propto E \cdot \Delta\alpha \cdot \Delta T$ gerilme yığılması ortadan kaldırılır ve termal şok direnci maksimize edilir.

---

### 2. Ekstrem Ortam Malzemeleri (Extreme Environment Materials)

*   **Ultra Yüksek Sıcaklık Seramikleri (UHTC):**
    Hafniyum Diborür ($HfB_2$) ve Zirkonyum Diborür ($ZrB_2$), $3000^\circ\text{C}$'nin üzerindeki erime sıcaklıklarıyla hipersonik uçuşlar için tasarlanır. Oksidasyon koruma mekanizması, reaksiyon sonucu yüzeyde oluşan koruyucu silika ($SiO_2$) cam tabakası ve yüksek erime noktalı metal oksit ($ZrO_2/HfO_2$) iskeletinin pasif bariyer oluşturması esasına dayanır:
    $$2ZrB_2 + 5O_2 \rightarrow 2ZrO_2 + 2B_2O_3 (g)$$
    Sıcaklık $1500^\circ\text{C}$'yi aştığında sıvı $B_2O_3$ buharlaşır ve koruma görevi kararlı $ZrO_2$ ve eklenen SiC'den türeyen viskoz $SiO_2$ akışına kalır.

*   **Yüksek Entropi Alaşımları (High Entropy Alloys - HEA):**
    Geleneksel alaşımlar tek bir ana metale dayanırken, HEA'lar 5 veya daha fazla elementi eşit/yakına yakın oranlarda içerir. Katı çözeltinin (solid solution) intermetalik fazlara karşı termodinamik kararlılığı, yüksek konfigürasyonel entropi ($\Delta S_{conf}$) ile sağlanır:
    $$\Delta S_{conf} = -R \sum_{i=1}^{N} x_i \ln x_i$$
    Eşit mol oranlı $N$ bileşenli bir alaşımda bu değer $\Delta S_{conf} = R \ln N$ maksimumuna ulaşır. $\Delta G_{mix} = \Delta H_{mix} - T\Delta S_{mix}$ denkleminde yüksek $T\Delta S$ terimi, serbest enerjiyi düşürerek basit kararlı tek fazlı (FCC veya BCC) yapıları stabilize eder ve olağanüstü kriyojenik tokluk kazandırır.

*   **Radyasyon Hasarı (Displacements Per Atom - dpa):**
    Nükleer reaktörlerde hızlı nötronlar atomları kafes bölgelerinden sökerek Frenkel çiftleri oluşturur. Bu birikimli hasar, Norgett-Robinson-Torrens (NRT) dpa modeli ile hesaplanır ve alaşımlarda helyum kabarcığı birikimi ile gevrekleşmeye yol açar.

---

### 3. Biyomimetik ve Kendi Kendini Onaran Malzemeler

*   **Süperhidrofobiklik ve Wetting (Lotus Etkisi) Modelleri:**
    Doğadaki Lotus yaprağı, nano-yapılı mumsu pürüzlülüğü sayesinde su damlacıklarını iter. Bu yüzey davranışı iki klasik modelle açıklanır:
    *   **Wenzel Modeli (Homojen Islanma):** Sıvı yüzeydeki pürüzleri tamamen doldurur.
        $$\cos\theta^* = r \cos\theta_Y$$
    *   **Cassie-Baxter Modeli (Heterojen Islanma):** Sıvı altında hava cepleri kalır.
        $$\cos\theta^* = f_1 \cos\theta_Y - f_2$$
    *(Burada $\theta^*$ görünür temas açısı, $\theta_Y$ pürüzsüz yüzey Young açısı, $r$ pürüzlülük oranı ($r \ge 1$) ve $f_1, f_2$ katı-sıvı ve gaz-sıvı temas alan fraksiyonlarıdır).*

*   **Kendi Kendini İyileştirme (Self-Healing) Kinetiği:**
    Malzemede çatlak oluştuğunda, mikrokapsüller kırılır ve salınan monomer (örn: disiklopentadien - DCPD), matrise dağıtılmış Grubbs' katalizörü ile temas ederek Halka Açılması Metatez Polimerizasyonu (ROMP) reaksiyonunu başlatır. Çatlak arayüzü polimerleşerek mukavemetini yeniden kazanır.

---

## 🔬 Önerilen Laboratuvar ve Pratik Uygulamalar
1.  **Deneysel Temas Açısı Ölçümü:** Farklı yüzey pürüzlülüklerine sahip numunelerin gonyometrede su temas açısı ölçümleri ile Wenzel/Cassie modellerinin doğrulanması.
2.  **FGM Isıl Analiz Simülasyonu:** Kalınlık boyunca alüminyum-seramik oranının değiştiği bir diskin termal şok yükü altındaki gerilme dağılımının Python ile sonlu farklar yöntemi kullanılarak çözülmesi.

---
[Ana Sayfaya Dön](../README.md)
