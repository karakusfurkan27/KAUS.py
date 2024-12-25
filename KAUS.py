import time
import random
from datetime import datetime
import sqlite3
import tkinter as tk
from tkinter import messagebox

class KazaOnlemeUyariSistemi:
    def __init__(self):
        self.tehlikeli_mesafe = 5  # Tehlikeli mesafe sınırı (örnek: metre)
        self.arac_hizi = 0  # Aracın mevcut hızı (km/saat)
        self.engel_mesafesi = 100  # Engelin mevcut mesafesi (örnek: metre)
        self.acil_durum_sayaci = 0  # Sürekli tehlike durumlarını takip için sayaç
        self.max_acil_durum = 3  # Maksimum arka arkaya tehlike sayısı
        self.sesli_uyari = True  # Sesli uyarı sistemi
        self.isik_uyari = True  # Işık uyarı sistemi
        self.hava_durumu = "Güzel"  # Varsayılan hava durumu
        self.arac_calistirabilir = True  # Araç çalışma durumu
        self.last_maintenance_date = datetime.now()  # Son bakım tarihi
        self.maintenance_interval_days = 30  # Bakım periyodu gün cinsinden
        self.database_olustur()

    def database_olustur(self):
        """Veri tabanı oluşturur ve gerekli tabloları ekler."""
        self.conn = sqlite3.connect("kaus_veritabani.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS kaza_kayitlari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarih TEXT,
            arac_hizi INTEGER,
            engel_mesafesi INTEGER,
            uyari_mesaji TEXT,
            hava_durumu TEXT
        )
        ''')
        self.conn.commit()

    def veri_kaydet(self, mesaj):
        """Uyarı durumlarını veri tabanına kaydeder."""
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
        INSERT INTO kaza_kayitlari (tarih, arac_hizi, engel_mesafesi, uyari_mesaji, hava_durumu) 
        VALUES (?, ?, ?, ?, ?)
        ''', (tarih, self.arac_hizi, self.engel_mesafesi, mesaj, self.hava_durumu))
        self.conn.commit()

    def arac_hizini_guncelle(self):
        """Aracın hızını rastgele bir değerle günceller."""
        self.arac_hizi = random.randint(0, 120)
        return self.arac_hizi

    def engel_mesafesini_guncelle(self):
        """Engel mesafesini rastgele bir değerle günceller."""
        self.engel_mesafesi = random.randint(1, 100)
        return self.engel_mesafesi

    def hava_durumunu_guncelle(self):
        """Hava durumunu rastgele bir değerle günceller."""
        hava_durumlari = ["Güzel", "Yağmurlu", "Sisli", "Karlı"]
        self.hava_durumu = random.choice(hava_durumlari)
        if self.hava_durumu == "Karlı":
            self.arac_calistirabilir = False  # Karlı havada araç çalışmaz
        elif self.hava_durumu == "Güzel":
            self.arac_calistirabilir = True  # Hava güzelse araç çalışabilir
        return self.hava_durumu

    def bakım_kontrol(self):
        """Aracın bakım zamanını kontrol eder."""
        bugun = datetime.now()
        gun_farki = (bugun - self.last_maintenance_date).days
        if gun_farki >= self.maintenance_interval_days:
            mesaj = f"Bakım zamanı geldi! Son bakım {gun_farki} gün önce yapıldı."
            self.veri_kaydet(mesaj)
            return "Bakım", mesaj
        return "Güvenli", "Bakım durumu iyi."

    def kaza_riski_kontrol(self):
        """Kaza riski olup olmadığını kontrol eder."""
        if not self.arac_calistirabilir:
            mesaj = "Karlı hava koşulları nedeniyle araç durduruldu!"
            self.veri_kaydet(mesaj)
            return "Tehlike", mesaj

        if self.engel_mesafesi <= self.tehlikeli_mesafe:
            self.acil_durum_sayaci += 1
            mesaj = "Çarpışma riski yüksek! Hemen durun!"
            self.veri_kaydet(mesaj)
            return "Tehlike", mesaj
        elif self.engel_mesafesi <= self.arac_hizi / 2:
            self.acil_durum_sayaci = 0
            mesaj = "Tehlikeli mesafe! Hızınızı azaltın!"
            self.veri_kaydet(mesaj)
            return "Uyarı", mesaj
        else:
            self.acil_durum_sayaci = 0
            return "Güvenli", "Durum güvenli."

    def __del__(self):
        """Veri tabanı bağlantısını kapatır."""
        self.conn.close()

class KazaOnlemeUyariSistemiGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kaza Önleme ve Uyarı Sistemi")
        self.master.geometry("500x400")

        self.kaus = KazaOnlemeUyariSistemi()

        # Başlık
        self.title_label = tk.Label(master, text="Kaza Önleme ve Uyarı Sistemi", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Hız ve Mesafe Bilgileri
        self.hiz_label = tk.Label(master, text="Araç Hızı: 0 km/s", font=("Arial", 12))
        self.hiz_label.pack(pady=5)

        self.mesafe_label = tk.Label(master, text="Engel Mesafesi: 100 metre", font=("Arial", 12))
        self.mesafe_label.pack(pady=5)

        self.hava_label = tk.Label(master, text="Hava Durumu: Güzel", font=("Arial", 12))
        self.hava_label.pack(pady=5)

        self.bakim_label = tk.Label(master, text="Bakım Durumu: İyi", font=("Arial", 12))
        self.bakim_label.pack(pady=5)

        # Uyarı Alanı
        self.uyari_label = tk.Label(master, text="Durum: Güvenli", font=("Arial", 12), fg="green")
        self.uyari_label.pack(pady=10)

        # Butonlar
        self.baslat_button = tk.Button(master, text="Başlat", command=self.baslat_sistemi)
        self.baslat_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.durdur_button = tk.Button(master, text="Durdur", command=self.durdur_sistemi)
        self.durdur_button.pack(side=tk.RIGHT, padx=20, pady=20)

        self.running = False

    def baslat_sistemi(self):
        if not self.kaus.arac_calistirabilir:
            messagebox.showerror("Hata", "Karlı hava koşulları nedeniyle araç çalıştırılamaz!")
            return
        self.running = True
        self.sistemi_calistir()

    def durdur_sistemi(self):
        self.running = False
        messagebox.showinfo("Sistem Durduruldu", "Kaza Önleme Sistemi durduruldu!")
        self.uyari_label.config(text="Durum: Pasif", fg="red")

    def sistemi_calistir(self):
        if self.running:
            hiz = self.kaus.arac_hizini_guncelle()
            mesafe = self.kaus.engel_mesafesini_guncelle()
            hava = self.kaus.hava_durumunu_guncelle()
            bakim_durumu, bakim_mesaj = self.kaus.bakım_kontrol()
            durum, mesaj = self.kaus.kaza_riski_kontrol()

            self.hiz_label.config(text=f"Araç Hızı: {hiz} km/s")
            self.mesafe_label.config(text=f"Engel Mesafesi: {mesafe} metre")
            self.hava_label.config(text=f"Hava Durumu: {hava}")
            self.bakim_label.config(text=f"Bakım Durumu: {bakim_mesaj}")

            if durum == "Tehlike":
                self.uyari_label.config(text=mesaj, fg="red")
            elif durum == "Uyarı":
                self.uyari_label.config(text=mesaj, fg="orange")
            else:
                self.uyari_label.config(text=mesaj, fg="green")

            self.master.after(1000, self.sistemi_calistir)

# Arayüzü çalıştır
if __name__ == "__main__":
    root = tk.Tk()
    app = KazaOnlemeUyariSistemiGUI(root)
    root.mainloop()
