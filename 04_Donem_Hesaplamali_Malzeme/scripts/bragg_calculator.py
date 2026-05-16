import math

def calculate_bragg(wavelength, angle_degree, n=1):
    """
    Bragg Yasası Hesaplayıcı: n * lambda = 2d * sin(theta)
    
    wavelength: X-ışını dalga boyu (Angstrom)
    angle_degree: Kırınım açısı (2-theta değil, theta)
    n: Kırınım derecesi (varsayılan 1)
    """
    theta_rad = math.radians(angle_degree)
    d_spacing = (n * wavelength) / (2 * math.sin(theta_rad))
    return d_spacing

if __name__ == "__main__":
    print("--- Bragg Yasası Kafes Mesafesi (d) Hesaplayıcı ---")
    
    try:
        wl = float(input("Dalga boyunu girin (Angstrom, örn: Cu-Ka için 1.5406): "))
        angle = float(input("Kırınım açısını girin (Theta derece cinsinden): "))
        
        result = calculate_bragg(wl, angle)
        
        print(f"\nSonuç: Kafes düzlemleri arası mesafe (d) = {result:.4f} Angstrom")
        
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")
    except ZeroDivisionError:
        print("Hata: Açı 0 olamaz.")
