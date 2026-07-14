# Primeri AI za začetnike

Dobrodošli! Ta imenik vsebuje preproste, samostojne primere, ki vam pomagajo začeti z umetno inteligenco in strojno učenje. Vsak primer je zasnovan tako, da je prijazen do začetnikov z podrobnimi komentarji in pojasnili korak za korakom.

## 📚 Pregled primerov

| Primer | Opis | Težavnost | Predpogoji |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Vaš prvi AI program – prepoznavanje preprostih vzorcev | ⭐ Začetnik | Osnove Pythona |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Ustvarite nevronsko mrežo iz nič | ⭐⭐ Začetnik+ | Python, osnovna matematika |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Razvrščanje slik z vnaprej usposobljenim modelom | ⭐⭐ Začetnik+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analiza čustvenega tona besedila (pozitivno/negativno) | ⭐⭐ Začetnik+ | Python |

## 🚀 Začetek

### Predpogoji

Poskrbite, da imate nameščen Python (priporočena različica 3.8 ali novejša). Namestite zahtevane pakete:

```bash
# Za Python skripte
pip install numpy

# Za Jupyter zvezke (razvrščevalnik slik)
pip install jupyter numpy pillow tensorflow
```

Ali uporabite conda okolje iz glavnega učnega načrta:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Zagon primerov

**Za Python skripte (.py datoteke):**
```bash
python 01-hello-ai-world.py
```

**Za Jupyter zapiske (.ipynb datoteke):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Učni načrt

Priporočamo, da sledite primerom po vrstnem redu:

1. **Začnite s "Hello AI World"** – Spoznajte osnove prepoznavanja vzorcev
2. **Zgradite preprosto nevronsko mrežo** – Razumite, kako delujejo nevronske mreže
3. **Preizkusite razvrščevalec slik** – Oglejte si AI pri delu z resničnimi slikami
4. **Analizirajte čustveni ton besedila** – Raziskujte obdelavo naravnega jezika

## 💡 Nasveti za začetnike

- **Pozorno preberite komentarje v kodi** – Pojasnjujejo, kaj naredi vsak vrstica
- **Eksperimentirajte!** – Spreminjajte vrednosti in opazujte, kaj se zgodi
- **Ne skrbite, če ne razumete vsega takoj** – Učenje zahteva čas
- **Postavljajte vprašanja** – Uporabite [forum za razpravo](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Naslednji koraki

Ko končate s temi primeri, si oglejte celotni učni načrt:
- [Uvod v AI](../lessons/1-Intro/README.md)
- [Nevronske mreže](../lessons/3-NeuralNetworks/README.md)
- [Računalniški vid](../lessons/4-ComputerVision/README.md)
- [Obdelava naravnega jezika](../lessons/5-NLP/README.md)

## 🤝 Prispevki

So vam ti primeri v pomoč? Pomagajte nam jih izboljšati:
- Poročajte o težavah ali predlagajte izboljšave
- Dodajte več primerov za začetnike
- Izboljšajte dokumentacijo in komentarje

---

*Zapomnite si: Vsak strokovnjak je bil nekoč začetnik. Srečno učenje! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->