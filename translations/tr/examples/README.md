# Yeni Başlayanlar İçin Yapay Zeka Örnekleri

Hoş geldiniz! Bu dizin, yapay zeka ve makine öğrenimine başlamanıza yardımcı olacak basit, bağımsız örnekler içerir. Her örnek, ayrıntılı yorumlar ve adım adım açıklamalarla yeni başlayan dostu olacak şekilde tasarlanmıştır.

## 📚 Örneklerin Genel Bakışı

| Örnek | Açıklama | Zorluk | Önkoşullar |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | İlk yapay zeka programınız - basit desen tanıma | ⭐ Yeni Başlayan | Python temelleri |
| [Basit Sinir Ağı](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Baştan bir sinir ağı inşa edin | ⭐⭐ Yeni Başlayan+ | Python, temel matematik |
| [Görüntü Sınıflandırıcı](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Önceden eğitilmiş modelle görüntü sınıflandırma | ⭐⭐ Yeni Başlayan+ | Python, numpy |
| [Metin Duygu Analizi](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Metin duygu analizi (pozitif/negatif) | ⭐⭐ Yeni Başlayan+ | Python |

## 🚀 Başlarken

### Önkoşullar

Python'un yüklü olduğundan emin olun (3.8 veya daha üstü önerilir). Gerekli paketleri kurun:

```bash
# Python betikleri için
pip install numpy

# Jupyter not defterleri için (görüntü sınıflandırıcı)
pip install jupyter numpy pillow tensorflow
```

Veya ana ders programından conda ortamını kullanın:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Örnekleri Çalıştırmak

**Python scriptleri (.py dosyaları) için:**
```bash
python 01-hello-ai-world.py
```

**Jupyter not defterleri (.ipynb dosyaları) için:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Öğrenme Yolu

Örnekleri sırasıyla takip etmenizi öneririz:

1. **"Hello AI World" ile başlayın** - Desen tanımanın temellerini öğrenin
2. **Basit Bir Sinir Ağı Kurun** - Sinir ağlarının nasıl çalıştığını anlayın
3. **Görüntü Sınıflandırıcıyı Deneyin** - Gerçek görüntülerle yapay zekayı görün
4. **Metin Duygu Analizini Yapın** - Doğal dil işlemede keşfedin

## 💡 Yeni Başlayanlar İçin İpuçları

- **Kod yorumlarını dikkatle okuyun** - Her satırın ne yaptığını açıklar
- **Deney yapın!** - Değerleri değiştirip ne olduğunu görün
- **Her şeyi anlamaya çalışırken endişelenmeyin** - Öğrenmek zaman alır
- **Sorular sorun** - [Tartışma panosunu](https://github.com/microsoft/AI-For-Beginners/discussions) kullanın

## 🔗 Sonraki Adımlar

Bu örnekleri tamamladıktan sonra tam ders programını keşfedin:
- [Yapay Zekaya Giriş](../lessons/1-Intro/README.md)
- [Sinir Ağları](../lessons/3-NeuralNetworks/README.md)
- [Bilgisayarla Görme](../lessons/4-ComputerVision/README.md)
- [Doğal Dil İşleme](../lessons/5-NLP/README.md)

## 🤝 Katkıda Bulunma

Bu örnekleri faydalı buldunuz mu? Geliştirmemize yardımcı olun:
- Sorunları bildirin veya geliştirme önerin
- Yeni başlayanlar için daha fazla örnek ekleyin
- Dokümantasyon ve yorumları iyileştirin

---

*Unutmayın: Her uzman bir zamanlar acemiydi. İyi öğrenmeler! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->