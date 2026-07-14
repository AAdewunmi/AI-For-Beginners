# ابتدائی افراد کے لئے دوستانہ AI مثالیں

خوش آمدید! یہ ڈائریکٹری آسان، خود مختار مثالیں رکھتی ہے جو آپ کو AI اور مشین لرننگ کے ساتھ شروعات کرنے میں مدد دیتی ہیں۔ ہر مثال کو ابتدائی افراد کے لئے آسان اور تفصیلی تبصروں اور مرحلہ وار وضاحتوں کے ساتھ ڈیزائن کیا گیا ہے۔

## 📚 مثالوں کا جائزہ

| مثال | وضاحت | مشکل کی سطح | پیشگی معلومات |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | آپ کا پہلا AI پروگرام - سادہ پیٹرن پہچان | ⭐ مبتدی | Python کی بنیادی باتیں |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | نیورل نیٹ ورک شروع سے بنائیں | ⭐⭐ مبتدی+ | Python، بنیادی ریاضی |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | پری ٹرینڈ ماڈل کے ساتھ تصویریں درجہ بندی کریں | ⭐⭐ مبتدی+ | Python، numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | متن کے جذبات کا تجزیہ کریں (مثبت/منفی) | ⭐⭐ مبتدی+ | Python |

## 🚀 شروع کرنا

### پیشگی معلومات

یقینی بنائیں کہ آپ کے پاس Python نصب ہے (3.8 یا اس سے اوپر کی سفارش کی جاتی ہے)۔ مطلوبہ پیکجز انسٹال کریں:

```bash
# پائتھن اسکرپٹس کے لیے
pip install numpy

# جیوپیٹر نوٹ بکس کے لیے (امیج درجہ بند کرنے والا)
pip install jupyter numpy pillow tensorflow
```

یا مرکزی نصاب سے conda ماحول استعمال کریں:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### مثالیں چلانا

**Python اسکرپٹس (.py فائلیں) کے لئے:**
```bash
python 01-hello-ai-world.py
```

**Jupyter نوٹ بکس (.ipynb فائلیں) کے لئے:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 تعلیمی راستہ

ہم تجویز کرتے ہیں کہ مثالوں کو اس ترتیب میں دیکھیں:

1. **"Hello AI World" سے شروع کریں** - پیٹرن پہچان کی بنیادی باتیں سیکھیں
2. **ایک سادہ نیورل نیٹ ورک بنائیں** - سمجھیں کہ نیورل نیٹ ورکس کیسے کام کرتے ہیں
3. **تصویریں درجہ بندی کرنے والا آزمائیں** - اصلی تصویروں کے ساتھ AI کو دیکھیں
4. **متن کے جذبات کا تجزیہ کریں** - قدرتی زبان کی پروسیسنگ کا مطالعہ کریں

## 💡 ابتدائی افراد کے لیے مشورے

- **کوڈ کے تبصرے غور سے پڑھیں** - یہ بتاتے ہیں کہ ہر لائن کیا کرتی ہے
- **تجربہ کریں!** - اقدار کو تبدیل کرکے دیکھیں کیا ہوتا ہے
- **سب کچھ سمجھنے کی فکر نہ کریں** - سیکھنے میں وقت لگتا ہے
- **سوال پوچھیں** - [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions) استعمال کریں

## 🔗 اگلے اقدامات

ان مثالوں کو مکمل کرنے کے بعد، مکمل نصاب دریافت کریں:
- [Introduction to AI](../lessons/1-Intro/README.md)
- [Neural Networks](../lessons/3-NeuralNetworks/README.md)
- [Computer Vision](../lessons/4-ComputerVision/README.md)
- [Natural Language Processing](../lessons/5-NLP/README.md)

## 🤝 حصہ ڈالنا

کیا آپ کو یہ مثالیں مددگار لگیں؟ ہماری مدد کریں انہیں بہتر بنانے میں:
- مسائل رپورٹ کریں یا بہتری کی تجاویز دیں
- مزید ابتدائی مثالیں شامل کریں
- دستاویزات اور تبصروں کو بہتر بنائیں

---

*یاد رکھیں: ہر ماہر ایک وقت میں مبتدی تھا۔ خوش رہیں اور سیکھیں! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->