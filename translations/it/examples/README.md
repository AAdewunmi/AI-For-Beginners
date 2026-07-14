# Esempi di Intelligenza Artificiale per Principianti

Benvenuto! Questa directory contiene esempi semplici e autonomi per aiutarti a iniziare con l'intelligenza artificiale e il machine learning. Ogni esempio è progettato per essere adatto ai principianti con commenti dettagliati e spiegazioni passo passo.

## 📚 Panoramica degli Esempi

| Esempio | Descrizione | Difficoltà | Prerequisiti |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Il tuo primo programma AI - semplice riconoscimento di pattern | ⭐ Principiante | Nozioni base di Python |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Costruisci una rete neurale da zero | ⭐⭐ Principiante+ | Python, matematica di base |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Classifica immagini con un modello pre-addestrato | ⭐⭐ Principiante+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analizza il sentimento del testo (positivo/negativo) | ⭐⭐ Principiante+ | Python |

## 🚀 Per Iniziare

### Prerequisiti

Assicurati di avere Python installato (consigliata la versione 3.8 o superiore). Installa i pacchetti richiesti:

```bash
# Per script Python
pip install numpy

# Per notebook Jupyter (classificatore di immagini)
pip install jupyter numpy pillow tensorflow
```

Oppure usa l'ambiente conda dal curriculum principale:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Esecuzione degli Esempi

**Per gli script Python (.py):**
```bash
python 01-hello-ai-world.py
```

**Per i notebook Jupyter (.ipynb):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Percorso di Apprendimento

Si consiglia di seguire gli esempi in questo ordine:

1. **Inizia con "Hello AI World"** - Impara le basi del riconoscimento di pattern
2. **Costruisci una rete neurale semplice** - Comprendi come funzionano le reti neurali
3. **Prova il classificatore di immagini** - Vedi l'AI in azione con immagini reali
4. **Analizza il sentimento del testo** - Esplora il trattamento del linguaggio naturale

## 💡 Consigli per Principianti

- **Leggi attentamente i commenti nel codice** - Spiegano cosa fa ogni riga
- **Sperimenta!** - Prova a cambiare i valori e guarda cosa succede
- **Non preoccuparti di capire tutto subito** - Imparare richiede tempo
- **Fai domande** - Usa il [Forum di Discussione](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Passi Successivi

Dopo aver completato questi esempi, esplora il curriculum completo:
- [Introduzione all'AI](../lessons/1-Intro/README.md)
- [Reti Neurali](../lessons/3-NeuralNetworks/README.md)
- [Visione Artificiale](../lessons/4-ComputerVision/README.md)
- [Elaborazione del Linguaggio Naturale](../lessons/5-NLP/README.md)

## 🤝 Contribuire

Hai trovato utili questi esempi? Aiutaci a migliorarli:
- Segnala problemi o suggerisci miglioramenti
- Aggiungi altri esempi per principianti
- Migliora la documentazione e i commenti

---

*Ricorda: ogni esperto è stato una volta un principiante. Buono studio! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->