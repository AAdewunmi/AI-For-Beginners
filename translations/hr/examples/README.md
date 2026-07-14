# Primjeri Prikladni Za Početnike u AI

Dobro došli! Ovaj direktorij sadrži jednostavne, samostalne primjere koji vam pomažu započeti s AI i strojnim učenjem. Svaki primjer je dizajniran da bude prikladan za početnike s detaljnim komentarima i korak-po-korak objašnjenjima.

## 📚 Pregled Primjera

| Primjer | Opis | Težina | Preduvjeti |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Vaš prvi AI program - jednostavno prepoznavanje obrazaca | ⭐ Početnik | Osnove Pythona |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Izgradite neuronsku mrežu iz temelja | ⭐⭐ Početnik+ | Python, osnovna matematika |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Klasificirajte slike pomoću unaprijed istreniranog modela | ⭐⭐ Početnik+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analizirajte sentiment teksta (pozitivan/negativan) | ⭐⭐ Početnik+ | Python |

## 🚀 Početak

### Preduvjeti

Provjerite imate li instaliran Python (preporučeno verzija 3.8 ili novija). Instalirajte potrebne pakete:

```bash
# Za Python skripte
pip install numpy

# Za Jupyter bilježnice (klasifikator slika)
pip install jupyter numpy pillow tensorflow
```

Ili koristite conda okruženje iz glavnog kurikuluma:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Pokretanje Primjera

**Za Python skripte (.py datoteke):**
```bash
python 01-hello-ai-world.py
```

**Za Jupyter bilježnice (.ipynb datoteke):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Put Učenja

Preporučujemo da slijedite primjere redom:

1. **Započnite s "Hello AI World"** - Naučite osnove prepoznavanja obrazaca
2. **Izgradite Jednostavnu Neuronsku Mrežu** - Razumite kako neuronske mreže funkcioniraju
3. **Isprobajte Image Classifier** - Pogledajte AI u akciji s pravim slikama
4. **Analizirajte Sentiment Teksta** - Istražite obradu prirodnog jezika

## 💡 Savjeti za Početnike

- **Pažljivo čitajte komentare u kodu** - Oni objašnjavaju što koja linija radi
- **Eksperimentirajte!** - Pokušajte mijenjati vrijednosti i vidjeti što se događa
- **Ne brinite ako ne razumijete sve odmah** - Učenje zahtijeva vrijeme
- **Postavljajte pitanja** - Koristite [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Sljedeći Koraci

Nakon što završite ove primjere, istražite cijeli kurikulum:
- [Uvod u AI](../lessons/1-Intro/README.md)
- [Neuronske Mreže](../lessons/3-NeuralNetworks/README.md)
- [Računalni Vid](../lessons/4-ComputerVision/README.md)
- [Obrada Prirodnog Jezika](../lessons/5-NLP/README.md)

## 🤝 Sudjelovanje

Jesu li vam ovi primjeri pomogli? Pomozite nam ih poboljšati:
- Prijavite probleme ili predložite poboljšanja
- Dodajte više primjera za početnike
- Poboljšajte dokumentaciju i komentare

---

*Zapamtite: Svaki stručnjak nekada je bio početnik. Sretno u učenju! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->