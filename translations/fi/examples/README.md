# Aloittelijaystävällisiä tekoälyesimerkkejä

Tervetuloa! Tämä hakemisto sisältää yksinkertaisia, itsenäisiä esimerkkejä, jotka auttavat sinua pääsemään alkuun tekoälyn ja koneoppimisen kanssa. Jokainen esimerkki on suunniteltu aloittelijaystävälliseksi yksityiskohtaisten kommenttien ja vaiheittaisten selitysten kera.

## 📚 Esimerkkien yleiskatsaus

| Esimerkki | Kuvaus | Vaikeustaso | Esivaatimukset |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Ensimmäinen tekoälyohjelmasi – yksinkertainen kuvioiden tunnistus | ⭐ Aloittelija | Pythonin perusteet |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Rakennetaan neuroverkko alusta alkaen | ⭐⭐ Aloittelija+ | Python, perusmatematiikka |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Luokittele kuvia valmiilla mallilla | ⭐⭐ Aloittelija+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analysoi tekstin tunne (positiivinen/negatiivinen) | ⭐⭐ Aloittelija+ | Python |

## 🚀 Aloitus

### Esivaatimukset

Varmista, että sinulla on Python asennettuna (3.8 tai uudempi suositeltu). Asenna vaaditut paketit:

```bash
# Python-skripteille
pip install numpy

# Jupyter-muistikirjoille (kuvaluokitin)
pip install jupyter numpy pillow tensorflow
```

Tai käytä conda-ympäristöä pääopetussuunnitelmasta:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Esimerkkien suorittaminen

**Python-skriptit (.py tiedostot):**
```bash
python 01-hello-ai-world.py
```

**Jupyter-muistikirjat (.ipynb tiedostot):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Oppimispolku

Suosittelemme seuraamaan esimerkkejä järjestyksessä:

1. **Aloita "Hello AI World"** - Opettele kuvioiden tunnistuksen perusteet
2. **Rakenna yksinkertainen neuroverkko** - Ymmärrä, miten neuroverkot toimivat
3. **Kokeile kuvaluokitinta** - Näe tekoäly käytännössä oikeiden kuvien kanssa
4. **Analysoi tekstin tunne** - Tutustu luonnollisen kielen käsittelyyn

## 💡 Vinkkejä aloittelijoille

- **Lue koodikommentit huolellisesti** – Ne selittävät, mitä kukin rivi tekee
- **Kokeile eri asioita!** – Muuta arvoja ja katso, mitä tapahtuu
- **Älä huoli, jos et ymmärrä kaikkea heti** – Oppiminen vie aikaa
- **Esitä kysymyksiä** – Käytä [Keskustelualue](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Seuraavat askeleet

Kun olet suorittanut nämä esimerkit, tutustu koko opetussuunnitelmaan:
- [Johdanto tekoälyyn](../lessons/1-Intro/README.md)
- [Neuroverkot](../lessons/3-NeuralNetworks/README.md)
- [Koneen näkö](../lessons/4-ComputerVision/README.md)
- [Luonnollisen kielen käsittely](../lessons/5-NLP/README.md)

## 🤝 Osallistuminen

Löysitkö näistä esimerkeistä apua? Auta meitä parantamaan niitä:
- Ilmoita ongelmista tai ehdota parannuksia
- Lisää lisää esimerkkejä aloittelijoille
- Paranna dokumentaatiota ja kommentteja

---

*Muista: Jokainen asiantuntija on joskus ollut aloittelija. Iloista oppimista! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->