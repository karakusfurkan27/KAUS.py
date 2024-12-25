### Kaza Önleme ve Uyarı Sistemi Projesi Readme

#### Proje Açıklaması
Bu proje, araçların güvenliğini artırmayı hedefleyen bir **Kaza Önleme ve Uyarı Sistemi**dir. Proje, araç hızını, engel mesafesini ve hava durumunu sürekli izler. Bu verilere göre, araçta oluşabilecek kaza risklerini analiz eder ve kullanıcıyı uyarır. Sistem, aynı zamanda araç bakım durumu takibini yaparak kullanıcıya bilgilendirme sağlar.

---

### Kullanılan Teknolojiler
- **Python**: Temel programlama dili
- **Tkinter**: Grafiksel kullanıcı arayüzü oluşturmak için kullanılmıştır.
- **SQLite**: Veri tabanı yönetimi için tercih edilmiştir.
- **random**: Rastgele veri üretimi için kullanılmıştır.
- **datetime**: Tarih ve zaman bilgisi işlemleri için kullanılmıştır.

---

### Özellikler
1. **Hız ve Mesafe Kontrolü**:
   - Araç hızı ve engel mesafesi gerçek zamanlı olarak güncellenir.
   - Engel mesafesi tehlikeli seviyeye ulaştığında kullanıcıya uyarı verilir.

2. **Hava Durumu İzleme**:
   - Hava durumu güncellenir ve "Karlı" hava koşullarında araç çalıştırılamaz.

3. **Bakım Takibi**:
   - Araç bakım zamanı geldiğinde kullanıcıya bilgi mesajı iletilir.

4. **Uyarı Sistemi**:
   - Sesli ve ışıklı uyarılar, tehlike durumlarını belirtmek için aktif hale gelir.

5. **Veri Kaydı**:
   - Tüm uyarılar ve durumlar SQLite veri tabanında kaydedilir.

6. **Kullanıcı Arayüzü**:
   - Kullanıcı dostu bir arayüz ile hız, mesafe, hava durumu ve bakım bilgileri anlık olarak gösterilir.

---

### Kurulum ve Kullanım
1. **Gerekli Kütüphaneler**:
   - Projeyi çalıştırmadan önce Python 3 yüklü olmalıdır.
   - Gerekli kütüphaneler (`sqlite3`, `tkinter`, `random`, `datetime`) Python’un standart kütüphaneleridir. Ek bir kurulum gerekmez.

2. **Projenin Çalıştırılması**:
   - `kaza_onleme.py` dosyasını bir Python IDE veya terminal kullanarak çalıştırın.
   - Arayüz açıldığında "Başlat" butonuna basarak sistemi başlatabilirsiniz.

3. **Arayüz Butonları**:
   - **Başlat**: Sistemi çalıştırır ve hız, mesafe, hava durumu gibi bilgileri gerçek zamanlı olarak izler.
   - **Durdur**: Sistemi durdurur ve tüm süreçleri pasif hale getirir.

---

### Proje Dosyaları
- `kaza_onleme.py`: Ana program dosyası.
- `kaus_veritabani.db`: SQLite veri tabanı dosyası. Kaza kayıtları bu dosyada tutulur.

---

### Ekran Görüntüleri
1. **Arayüz Başlangıç Ekranı**:
   - Araç hızı, engel mesafesi, hava durumu ve bakım durumu bilgilerini gösterir.
2. **Uyarı Durumu**:
   - Tehlikeli durumlarda arayüzde kırmızı bir uyarı mesajı görüntülenir.

---

### Geliştirme Notları
- **Gelecekteki İyileştirmeler**:
  - Daha detaylı hava durumu entegrasyonu yapılabilir.
  - Sesli uyarılar için ek bir ses dosyası desteği eklenebilir.
  - Farklı araç türleri için özelleştirilebilir hız ve mesafe sınırları eklenebilir.

- **Bilinen Sorunlar**:
  - Hız ve mesafe verileri rastgele üretildiği için gerçek bir sensör entegrasyonu yapılmamıştır.
  - Sistem çalışırken durdurma işlemi bazen gecikmeli gerçekleşebilir.

---

### Yazar
Bu proje, araç güvenliğini artırmaya yönelik bir simülasyon olarak geliştirilmiştir. Geri bildirim ve önerileriniz için iletişime geçmekten çekinmeyin. 
