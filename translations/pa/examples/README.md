# ਨਵੇਂ ਸਿਖਣ ਵਾਲਿਆਂ ਲਈ ਏਆਈ ਉਦਾਹਰਣਾਂ

ਸਵਾਗਤ ਹੈ! ਇਸ ਫੋਲਡਰ ਵਿੱਚ ਸਾਦੇ, ਖੁਦਮੁਖਤਾਰ ਉਦਾਹਰਣ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਏਆਈ ਅਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨਗੇ। ਹਰ ਉਦਾਹਰਣ ਨਵੇਂ ਸਿਖਣ ਵਾਲਿਆਂ ਲਈ موزੂਨ ਹੈ ਜੋ ਵਿਸਥਾਰ ਨਾਲ ਟਿੱਪਣੀਆਂ ਅਤੇ ਕਦਮ-ਦਰ-ਕਦਮ ਵਿਆਖਿਆਵਾਂ ਨਾਲ banaayi gayi hai.

## 📚 ਉਦਾਹਰਣਾਂ ਦਾ ਜਾਇਜ਼ਾ

| Example | Description | Difficulty | Prerequisites |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | ਤੁਹਾਡਾ ਪਹਿਲਾ ਏਆਈ ਪ੍ਰੋਗਰਾਮ - ਸਾਦਾ ਪੈਟਰਨ ਪਹਿਚਾਣ | ⭐ Beginner | Python ਬੁਨਿਆਦੀ ਜਾਣਕਾਰੀ |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | ਸ਼ੁਰੂ ਤੋਂ ਨਿਰਮਾਣ ਕਰੋ ਇਕ ਨਿਊਰਲ ਨੈੱਟਵਰਕ | ⭐⭐ Beginner+ | Python, ਬੁਨਿਆਦੀ ਗਣਿਤ |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | ਪ੍ਰੀ-ਟ੍ਰੇਨਡ ਮਾਡਲ ਨਾਲ ਚਿੱਤਰਾਂ ਦੀ ਵਰਗੀਕਰਨ ਕਰੋ | ⭐⭐ Beginner+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | ਲਿਖਤ ਦਾ ਭਾਵਨਾ ਵਿਸ਼ਲੇਸ਼ਣ (ਸਕਾਰਾਤਮਕ/ਨਕਾਰਾਤਮਕ) | ⭐⭐ Beginner+ | Python |

## 🚀 ਸ਼ੁਰੂਆਤ ਕਰਨਾ

### ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ

ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ Python ਇੰਸਟਾਲ ਹੈ (3.8 ਜਾਂ ਉਸ ਤੋਂ ਉੱਪਰ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)। ਜ਼ਰੂਰੀ ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ:

```bash
# ਪਾਈਥਨ ਸਕ੍ਰਿਪਟਾਂ ਲਈ
pip install numpy

# ਜੁਪੀਟਰ ਨੋਟਬੁੱਕਾਂ ਲਈ (ਇਮੇਜ ਕਲਾਸੀਫਾਇਰ)
pip install jupyter numpy pillow tensorflow
```

ਜਾਂ ਮੁੱਖ ਕਰੀਕੁਲਮ ਦੇ ਕੋੰਡਾ ਇੰਵਾਇਰਨਮੈਂਟ ਦੀ ਵਰਤੋਂ ਕਰੋ:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### ਉਦਾਹਰਣ ਚਲਾਉਣਾ

**Python ਸਕ੍ਰਿਪਟਾਂ (.py ਫਾਇਲਾਂ) ਲਈ:**
```bash
python 01-hello-ai-world.py
```

**Jupyter ਨੋਟਬੁੱਕਾਂ (.ipynb ਫਾਇਲਾਂ) ਲਈ:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 ਸਿੱਖਣ ਦਾ ਰਾਹ

ਅਸੀਂ ਸੁਝਾਅ ਦਿੰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਉਦਾਹਰਣਾਂ ਨੂੰ ਕ੍ਰਮਵਾਰ ਫੋਲੋ ਕਰੋ:

1. **"Hello AI World" ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ** - ਪੈਟਰਨ ਪਹਿਚਾਣ ਦੇ ਮੂਲ ਸਿੱਖੋ
2. **ਇੱਕ ਸਾਦਾ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਬਣਾਓ** - ਸਮਝੋ ਕਿ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ
3. **ਚਿੱਤਰ ਵਰਗੀਕਰਨ ਕੋਸ਼ਿਸ਼ ਕਰੋ** - ਅਸਲੀ ਚਿੱਤਰਾਂ ਨਾਲ ਏਆਈ ਦੇਖੋ
4. **ਲਿਖਤ ਭਾਵਨਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ** - ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੋਸੈਸਿੰਗ ਦੀ ਸੈਰ ਕਰੋ

## 💡 ਨਵੇਂ ਸਿਖਣ ਵਾਲਿਆਂ ਲਈ ਸੁਝਾਅ

- **ਕੋਡ ਟਿੱਪਣੀਆਂ ਧਿਆਨ ਨਾਲ ਪੜ੍ਹੋ** - ਉਹ ਹਰ ਲਾਈਨ ਦਾ ਕਾਰਜ ਸਮਝਾਉਂਦੀਆਂ ਹਨ
- **ਪ੍ਰਯੋਗ ਕਰੋ!** - ਮੁੱਲਾਂ ਨੂੰ ਬਦਲ ਕੇ ਦੇਖੋ ਕੀ ਹੁੰਦਾ ਹੈ
- **ਸਭ ਕੁਝ ਸਮਝਣ ਦੀ ਚਿੰਤਾ ਨਾ ਕਰੋ** - ਸਿੱਖਿਆ ਵਿੱਚ ਸਮਾਂ ਲੱਗਦਾ ਹੈ
- **ਸਵਾਲ ਪੁੱਛੋ** - [ਚਰਚਾ ਬੋਰਡ](https://github.com/microsoft/AI-For-Beginners/discussions) ਦੀ ਵਰਤੋਂ ਕਰੋ

## 🔗 ਅਗਲੇ ਕਦਮ

ਇਹ ਉਦਾਹਰਣਾਂ ਖਤਮ ਕਰਨ ਤੋਂ ਬਾਅਦ ਪੂਰੇ ਕਰੀਕੁਲਮ ਨੂੰ ਖੋਜੋ:
- [ਐਆਈ ਦਾ ਪਰੀਚਯ](../lessons/1-Intro/README.md)
- [ਨਿਊਰਲ ਨੈੱਟਵਰਕ](../lessons/3-NeuralNetworks/README.md)
- [ਕੰਪਿਊਟਰ ਵਿਜ਼ਨ](../lessons/4-ComputerVision/README.md)
- [ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੋਸੈਸਿੰਗ](../lessons/5-NLP/README.md)

## 🤝 ਯੋਗਦਾਨ

ਕੀ ਇਹ ਉਦਾਹਰਣ ਤੁਹਾਨੂੰ ਮਦਦਗਾਰ ਲੱਗੇ? ਉਹਨਾਂ ਨੂੰ ਬਹਿਤਰ ਬਣਾਉਣ ਵਿੱਚ ਸਾਡੀ ਮਦਦ ਕਰੋ:
- ਸਮੱਸਿਆਵਾਂ ਦੀ ਰਿਪੋਰਟ ਕਰੋ ਜਾਂ ਸੁਝਾਅ ਦਿਓ
- ਨਵੇਂ ਸਿਖਣ ਵਾਲਿਆਂ ਲਈ ਹੋਰ ਉਦਾਹਰਣ ਸ਼ਾਮਲ ਕਰੋ
- ਦਸਤਾਵੇਜ਼ ਅਤੇ ਟਿੱਪਣੀਆਂ ਸੁਧਾਰੋ

---

*ਯਾਦ ਰੱਖੋ: ਹਰ ਮਹਿਰਤ ਇੱਕ ਵਾਰ ਨਵੇਂ ਸਿਖਣ ਵਾਲੇ ਹੁੰਦੇ ਹਨ। ਖੁਸ਼ ਰਹੋ ਸਿੱਖਣ ਵਿੱਚ! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->