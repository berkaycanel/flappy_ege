# 🎮 Flappy Ege

Klasik Flappy Bird oyununun Ege versiyonu! Streamlit ile yapılmış, tam oynanabilir HTML/JavaScript oyun.

## 🚀 Kurulum

### Dosyalar

Aşağıdaki dosyaların hepsinin aynı klasörde olması gerekiyor:
- `flappy_ege.py` (ana oyun dosyası)
- `IMG_3869.jpg` (Ege'nin fotoğrafı)
- `requirements.txt`
- `README.md`

### Yerel Çalıştırma

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. **ÖNEMLİ:** `IMG_3869.jpg` dosyasını `flappy_ege.py` ile aynı klasöre koyun!

3. Oyunu başlatın:
```bash
streamlit run flappy_ege.py
```

4. Tarayıcınızda otomatik olarak açılacaktır (genellikle `http://localhost:8501`)

## 🌐 Streamlit Cloud'a Deploy

1. GitHub'a şu dosyaları yükleyin:
   - `flappy_ege.py`
   - `IMG_3869.jpg` ⚠️ **MUTLAKA EKLE!**
   - `requirements.txt`
   - `README.md`

2. [Streamlit Cloud](https://streamlit.io/cloud)'a gidin

3. "New app" butonuna tıklayın

4. GitHub repository'nizi seçin

5. Main file path: `flappy_ege.py`

6. Deploy butonuna tıklayın!

## 🎯 Nasıl Oynanır?

### Kontroller (3 Farklı Yol!)
1. **SPACE** tuşuna bas
2. **YUKARI OK (↑)** tuşuna bas  
3. **OYUN ALANINA TIKLA** (mouse ile)

### Amaç
- Ege'yi havada tutmaya çalış
- Yeşil borulara çarpma
- Her geçtiğin boru = 1 puan
- En yüksek skoru yap!

## 📋 Özellikler

✨ HTML5 Canvas ile gerçek oyun deneyimi
🎮 Klavye + Mouse kontrolü
🎨 Gerçek fotoğraf kullanımı
🏆 LocalStorage ile en yüksek skor kaydı
💫 Smooth animasyonlar
📱 Responsive tasarım
🚀 Production-ready
⚡ 60 FPS performans

## 🛠️ Teknolojiler

- Python 3.8+
- Streamlit
- HTML5 Canvas
- JavaScript
- LocalStorage API

## 📝 Önemli Notlar

⚠️ **MUTLAKA**: `IMG_3869.jpg` dosyasını ana dizine koy!
- Oyun bu dosya olmadan çalışmaz
- Dosya adı tam olarak `IMG_3869.jpg` olmalı
- Dosya `flappy_ege.py` ile aynı klasörde olmalı

## 🎮 Oyun Mekanikleri

- **Gravity**: 0.6
- **Jump Strength**: -12
- **Pipe Speed**: 3 px/frame
- **Pipe Gap**: 200 px
- **Bird Size**: 50x50 px
- **FPS**: ~60

## 🐛 Sorun Giderme

**Oyun açılmıyor:**
- `IMG_3869.jpg` dosyasının doğru yerde olduğundan emin ol

**Resim görünmüyor:**
- Dosya adının tam olarak `IMG_3869.jpg` olduğunu kontrol et
- Büyük/küçük harf duyarlı!

**Deploy'da hata:**
- GitHub'a `IMG_3869.jpg` dosyasını yüklediğinden emin ol

## 👨‍💻 Geliştirici

Made with ❤️

## 📄 Lisans

MIT License - İstediğiniz gibi kullanabilirsiniz!

---

**Not:** Oyun tamamen eğlence amaçlıdır. Streamlit Cloud'da ücretsiz deploy edilebilir!
