# Kezdőknek Szóló AI Példák

Üdvözlünk! Ez a könyvtár egyszerű, önálló példákat tartalmaz, hogy segítsen elindulni az AI és a gépi tanulás világában. Minden példa kezdőbarát, részletes megjegyzésekkel és lépésről lépésre történő magyarázatokkal.

## 📚 Példák Áttekintése

| Példa | Leírás | Nehézség | Előfeltételek |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Az első AI programod – egyszerű minta felismerés | ⭐ Kezdő | Python alapjai |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Hozz létre egy neurális hálózatot a semmiből | ⭐⭐ Kezdő+ | Python, alap matematikai ismeretek |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Kép osztályozás előre betanított modellel | ⭐⭐ Kezdő+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Szövegérzelem elemzése (pozitív/negatív) | ⭐⭐ Kezdő+ | Python |

## 🚀 Kezdjünk neki

### Előfeltételek

Győződj meg róla, hogy telepítve van a Python (3.8 vagy újabb verzió ajánlott). Telepítsd a szükséges csomagokat:

```bash
# Python szkriptekhez
pip install numpy

# Jupyter jegyzetfüzetekhez (kép osztályozó)
pip install jupyter numpy pillow tensorflow
```

Vagy használd a conda környezetet a fő tananyagból:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Példák futtatása

**Python szkriptekhez (.py fájlok):**
```bash
python 01-hello-ai-world.py
```

**Jupyter jegyzetfüzetekhez (.ipynb fájlok):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Tanulási útvonal

Ajánljuk, hogy a példákat sorrendben kövesd:

1. **Kezdd a "Hello AI World"-del** – Ismerd meg az alapvető minta felismerést
2. **Építs egy egyszerű neurális hálózatot** – Értsd meg, hogyan működnek a neurális hálózatok
3. **Próbáld ki a kép osztályozót** – Nézd meg az AI működését valós képekkel
4. **Elemzd a szövegérzelmeket** – Fedezd fel a természetes nyelvfeldolgozást

## 💡 Tippek kezdőknek

- **Olvasd el alaposan a kód megjegyzéseit** – Elmagyarázzák, mit csinál minden sor
- **Kísérletezz!** – Próbálj meg értékeket változtatni és figyeld meg, mi történik
- **Ne aggódj, ha nem értesz mindent elsőre** – A tanulás időt vesz igénybe
- **Tegyél fel kérdéseket** – Használd a [Vita fórumot](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Következő lépések

Miután elvégezted ezeket a példákat, fedezd fel a teljes tananyagot:
- [Bevezetés az AI-ba](../lessons/1-Intro/README.md)
- [Neurális hálózatok](../lessons/3-NeuralNetworks/README.md)
- [Számítógépes látás](../lessons/4-ComputerVision/README.md)
- [Természetes nyelvfeldolgozás](../lessons/5-NLP/README.md)

## 🤝 Hozzájárulás

Hasznosnak találtad ezeket a példákat? Segíts nekünk fejleszteni őket:
- Jelents hibákat vagy javasolj fejlesztéseket
- Adj hozzá több példát kezdőknek
- Fejleszd a dokumentációt és a megjegyzéseket

---

*Emlékezz: minden szakértő egyszer kezdő volt. Jó tanulást! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->