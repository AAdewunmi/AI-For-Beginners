# Begynder-venlige AI-eksempler

Velkommen! Dette bibliotek indeholder simple, selvstændige eksempler til at hjælpe dig i gang med AI og maskinlæring. Hvert eksempel er designet til at være begynder-venligt med detaljerede kommentarer og trin-for-trin forklaringer.

## 📚 Oversigt over eksempler

| Eksempel | Beskrivelse | Sværhedsgrad | Forudsætninger |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Dit første AI-program - enkel mønstergenkendelse | ⭐ Begynder | Grundlæggende Python |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Byg et neuralt netværk fra bunden | ⭐⭐ Begynder+ | Python, grundlæggende matematik |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Klassificer billeder med en foruddannet model | ⭐⭐ Begynder+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analyser tekstfølelse (positiv/negativ) | ⭐⭐ Begynder+ | Python |

## 🚀 Kom i gang

### Forudsætninger

Sørg for, at du har Python installeret (version 3.8 eller nyere anbefales). Installer nødvendige pakker:

```bash
# Til Python-scripts
pip install numpy

# Til Jupyter-notebooks (billedklassifikator)
pip install jupyter numpy pillow tensorflow
```

Eller brug conda-miljøet fra hovedpensum:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Kør eksemplerne

**For Python-scripts (.py filer):**
```bash
python 01-hello-ai-world.py
```

**For Jupyter-notebooks (.ipynb filer):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Læringsvej

Vi anbefaler at følge eksemplerne i denne rækkefølge:

1. **Start med "Hello AI World"** - Lær det grundlæggende om mønstergenkendelse
2. **Byg et simpelt neuralt netværk** - Forstå, hvordan neurale netværk fungerer
3. **Prøv billedklassifikatoren** - Se AI i aktion med rigtige billeder
4. **Analyser tekstfølelse** - Udforsk naturlig sprogbehandling

## 💡 Tips til begyndere

- **Læs kodekommentarerne grundigt** - De forklarer, hvad hver linje gør
- **Eksperimenter!** - Prøv at ændre værdier og se, hvad der sker
- **Bekymr dig ikke om at forstå alt med det samme** - Læring tager tid
- **Stil spørgsmål** - Brug [diskussionsbordet](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Næste skridt

Efter at have gennemført disse eksempler, kan du udforske hele pensum:
- [Introduktion til AI](../lessons/1-Intro/README.md)
- [Neurale netværk](../lessons/3-NeuralNetworks/README.md)
- [Computer Vision](../lessons/4-ComputerVision/README.md)
- [Naturlig sprogbehandling](../lessons/5-NLP/README.md)

## 🤝 Bidrag

Synes du, disse eksempler er hjælpsomme? Hjælp os med at forbedre dem:
- Rapporter problemer eller foreslå forbedringer
- Tilføj flere eksempler for begyndere
- Forbedr dokumentation og kommentarer

---

*Husk: Enhver ekspert har engang været begynder. God læring! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->