import math

# --- İleri Malzemeler Akademisi: Kompozit Plaka Özellikleri Hesaplayıcı ---
# Bu script, fiber ve matris hacim oranlarına göre tek tabaka (ply) kompozitin 
# boyuna elastik modülü (E1), enine elastik modülü (E2), Poisson oranı (v12) ve 
# kayma modülünü (G12) Karışımlar Kuralı ve Halpin-Tsai modellerini kullanarak hesaplar.

PRESETS = {
    "fiber": {
        "1": {"name": "Karbon Fiber (AS4)", "E": 231.0, "G": 28.0, "v": 0.20},
        "2": {"name": "E-Glass (Cam) Fiber", "E": 72.0, "G": 30.0, "v": 0.22},
        "3": {"name": "Aramid (Kevlar 49) Fiber", "E": 131.0, "G": 9.0, "v": 0.35}
    },
    "matrix": {
        "1": {"name": "Epoksi Matris (Standart Aerospace)", "E": 3.4, "G": 1.3, "v": 0.35},
        "2": {"name": "PEEK Matris (Biyomedikal/Yüksek Tokluk)", "E": 4.0, "G": 1.4, "v": 0.40},
        "3": {"name": "Polimid Matris (Yüksek Sıcaklık)", "E": 3.1, "G": 1.1, "v": 0.34}
    }
}

def calculate_e1(ef, em, vf):
    """
    Boyuna Elastik Modül (E1) - Karışımlar Kuralı (Voigt)
    E1 = Ef * Vf + Em * (1 - Vf)
    """
    vm = 1.0 - vf
    return ef * vf + em * vm

def calculate_e2_reuss(ef, em, vf):
    """
    Enine Elastik Modül (E2) - Ters Karışımlar Kuralı (Reuss)
    1/E2 = Vf/Ef + Vm/Em
    """
    vm = 1.0 - vf
    return (ef * em) / (em * vf + ef * vm)

def calculate_e2_halpin_tsai(ef, em, vf, xi=2.0):
    """
    Enine Elastik Modül (E2) - Halpin-Tsai Modeli
    xi: Dairesel fiberler için genellikle 2.0 alınır (geometrik faktör)
    """
    eta = ((ef / em) - 1.0) / ((ef / em) + xi)
    num = 1.0 + xi * eta * vf
    den = 1.0 - eta * vf
    return em * (num / den)

def calculate_v12(vf, vm, vf_ratio):
    """
    Poisson Oranı (v12) - Karışımlar Kuralı
    v12 = vf * Vf + vm * Vm
    """
    vm_ratio = 1.0 - vf_ratio
    return vf * vf_ratio + vm * vm_ratio

def calculate_g12_reuss(gf, gm, vf):
    """
    Kayma Modülü (G12) - Ters Karışımlar Kuralı (Reuss)
    """
    vm = 1.0 - vf
    return (gf * gm) / (gm * vf + gf * vm)

def calculate_g12_halpin_tsai(gf, gm, vf, xi=1.0):
    """
    Kayma Modülü (G12) - Halpin-Tsai Modeli
    xi: Kayma için genellikle 1.0 alınır
    """
    eta = ((gf / gm) - 1.0) / ((gf / gm) + xi)
    num = 1.0 + xi * eta * vf
    den = 1.0 - eta * vf
    return gm * (num / den)

def print_separator():
    print("-" * 65)

def main():
    print_separator()
    print("      [i] İLERİ MALZEMELER AKADEMİSİ: KOMPOZİT PLAKA ANALİZİ [i]      ")
    print("      (Rule of Mixtures & Halpin-Tsai Elastic Constants)      ")
    print_separator()

    # --- 1. Adım: Fiber Seçimi ---
    print("\n[Adım 1] Takviye Elemanı (Fiber) Seçimi:")
    for key, value in PRESETS["fiber"].items():
        print(f"  {key}-) {value['name']} (E={value['E']} GPa, G={value['G']} GPa, v={value['v']})")
    print("  4-) Özel Tanımla (Kendi Değerlerinizi Girin)")
    
    choice_f = input("Seçiminiz (1-4): ").strip()
    if choice_f in ["1", "2", "3"]:
        f_name = PRESETS["fiber"][choice_f]["name"]
        ef = PRESETS["fiber"][choice_f]["E"]
        gf = PRESETS["fiber"][choice_f]["G"]
        vf = PRESETS["fiber"][choice_f]["v"]
    else:
        print("\nÖzel Fiber Değerlerini Girin:")
        f_name = "Özel Fiber"
        ef = float(input("  Elastik Modül (Ef, GPa): "))
        gf = float(input("  Kayma Modülü (Gf, GPa): "))
        vf = float(input("  Poisson Oranı (vf): "))

    # --- 2. Adım: Matris Seçimi ---
    print("\n[Adım 2] Matris Elemanı Seçimi:")
    for key, value in PRESETS["matrix"].items():
        print(f"  {key}-) {value['name']} (E={value['E']} GPa, G={value['G']} GPa, v={value['v']})")
    print("  4-) Özel Tanımla (Kendi Değerlerinizi Girin)")
    
    choice_m = input("Seçiminiz (1-4): ").strip()
    if choice_m in ["1", "2", "3"]:
        m_name = PRESETS["matrix"][choice_m]["name"]
        em = PRESETS["matrix"][choice_m]["E"]
        gm = PRESETS["matrix"][choice_m]["G"]
        vm = PRESETS["matrix"][choice_m]["v"]
    else:
        print("\nÖzel Matris Değerlerini Girin:")
        m_name = "Özel Matris"
        em = float(input("  Elastik Modül (Em, GPa): "))
        gm = float(input("  Kayma Modülü (Gm, GPa): "))
        vm = float(input("  Poisson Oranı (vm): "))

    # --- 3. Adım: Hacim Oranı Seçimi ---
    print("\n[Adım 3] Hacimsel Dağılım Oranları:")
    while True:
        try:
            vf_ratio = float(input("  Fiber Hacim Oranı (Vf, 0.0 ile 1.0 arasında, örn: 0.60): "))
            if 0.0 <= vf_ratio <= 1.0:
                break
            print("Hata: Oran 0.0 ile 1.0 arasında olmalıdır.")
        except ValueError:
            print("Hata: Geçerli bir sayı girin.")

    vm_ratio = 1.0 - vf_ratio

    # --- 4. Hesaplamalar ---
    e1 = calculate_e1(ef, em, vf_ratio)
    e2_reuss = calculate_e2_reuss(ef, em, vf_ratio)
    e2_ht = calculate_e2_halpin_tsai(ef, em, vf_ratio, xi=2.0)
    v12 = calculate_v12(vf, vm, vf_ratio)
    g12_reuss = calculate_g12_reuss(gf, gm, vf_ratio)
    g12_ht = calculate_g12_halpin_tsai(gf, gm, vf_ratio, xi=1.0)

    # --- 5. Raporlama ---
    print("\n")
    print_separator()
    print("                 [+] HESAPLAMA RAPORU & ANALİZ ÇIKTISI                ")
    print_separator()
    print(f"  Bileşen 1 (Takviye): {f_name}")
    print(f"  Bileşen 2 (Matris) : {m_name}")
    print(f"  Hacim Dağılımı     : %{vf_ratio*100:.1f} Fiber / %{vm_ratio*100:.1f} Matris")
    print_separator()
    print("  ÖZELLİK                     | YÖNTEM             | DEĞER     ")
    print_separator()
    print(f"  Boyuna Elastik Modül (E1)   | Karışımlar Kuralı  | {e1:.2f} GPa")
    print(f"  Enine Elastik Modül (E2)    | Reuss Modeli       | {e2_reuss:.2f} GPa")
    print(f"  Enine Elastik Modül (E2)    | Halpin-Tsai (xi=2) | {e2_ht:.2f} GPa (Önerilen)")
    print(f"  Poisson Oranı (v12)         | Karışımlar Kuralı  | {v12:.3f}")
    print(f"  Kayma Modülü (G12)          | Reuss Modeli       | {g12_reuss:.2f} GPa")
    print(f"  Kayma Modülü (G12)          | Halpin-Tsai (xi=1) | {g12_ht:.2f} GPa (Önerilen)")
    print_separator()
    print("\n[i] Fiziksel Analiz Notları:")
    print("  - E1 modülü fiberlerin doğrusal çekme dayanımı tarafından domine edilir.")
    print("  - E2 modülü enine yönde matrisin deformasyonuyla sınırlıdır. Reuss modeli")
    print("    düşük limit kabul edilirken, Halpin-Tsai deneysel verilere en yakın tahmindir.")
    print("  - Poisson oranı v12, doğrusal deformasyondaki enine büzülmeyi tanımlar.")
    print_separator()

if __name__ == "__main__":
    main()
