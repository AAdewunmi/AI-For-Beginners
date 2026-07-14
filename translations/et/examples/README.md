# Algajatele Sobivad Tehisintellekti Näited

Tere tulemast! See kataloog sisaldab lihtsaid üksikuid näiteid, mis aitavad sul alustada tehisintellekti ja masinõppega. Iga näide on loodud algajasõbralikuna koos põhjalike kommentaaride ja samm-sammuliste selgitustega.

## 📚 Näidete Ülevaade

| Näide | Kirjeldus | Raskusaste | Nõuded |
|---------|-------------|------------|---------------|
| [Tere, AI maailm](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Sinu esimene tehisintellekti programm - lihtne mustrituvastus | ⭐ Algaja | Pythoni põhiteadmised |
| [Lihtne närvivõrk](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Ehita närvivõrk nullist | ⭐⭐ Algaja+ | Python, põhiline matemaatika |
| [Pildiklassifitseerija](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Klassifitseeri pilte eelõpetatud mudeliga | ⭐⭐ Algaja+ | Python, numpy |
| [Teksti meeleolu](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analüüsi teksti meelolu (positiivne/negatiivne) | ⭐⭐ Algaja+ | Python |

## 🚀 Alustamine

### Nõudmised

Veendu, et sinul on Python installitud (soovitatav 3.8 või uuem). Paigalda vajalikud paketid:

```bash
# Pythoni skriptide jaoks
pip install numpy

# Jupyteri märkmike jaoks (pildiklassifikaator)
pip install jupyter numpy pillow tensorflow
```

Või kasuta conda keskkonda põhikursusest:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Näidete Käivitamine

**Python skriptide (.py failid) jaoks:**
```bash
python 01-hello-ai-world.py
```

**Jupyter märkmeraamatute (.ipynb failid) jaoks:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Õppimise Tee

Soovitame järgida näiteid järjekorras:

1. **Alusta "Tere, AI maailm"-ga** - Õpi mustrituvastuse põhialuseid
2. **Ehita lihtne närvivõrk** - Mõista, kuidas närvivõrgud töötavad
3. **Proovi pildiklassifitseerijat** - Vaata tehisintellekti toimimas pärispiltidega
4. **Analüüsi teksti meeleolu** - Uuri loomuliku keele töötlust

## 💡 Nõuanded Algajatele

- **Loe koodi kommentaare hoolikalt** - Need selgitavad, mida iga rida teeb
- **Katseta!** - Proovi muuta väärtusi ja vaata, mis juhtub
- **Ära muretse, kui kõike kohe ei mõista** - Õppimine võtab aega
- **Esita küsimusi** - Kasuta [Arutelufoorumit](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Järgmised Sammud

Kui oled need näited lõpetanud, uurige kogu õppekava:
- [Sissejuhatus tehisintellekti](../lessons/1-Intro/README.md)
- [Närvivõrgud](../lessons/3-NeuralNetworks/README.md)
- [Arvutinägemine](../lessons/4-ComputerVision/README.md)
- [Loodusliku Keele Töötlus](../lessons/5-NLP/README.md)

## 🤝 Panustamine

Kas leidsid need näited kasulikuks? Aita meil neid parandada:
- Teata probleemidest või tee ettepanekuid
- Lisa rohkem näiteid algajatele
- Paranda dokumentatsiooni ja kommentaare

---

*Pea meeles: iga ekspert oli kord algaja. Edukat õppimist! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->