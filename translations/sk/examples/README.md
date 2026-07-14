# Príklady AI vhodné pre začiatočníkov

Vitajte! Tento adresár obsahuje jednoduché, samostatné príklady, ktoré vám pomôžu začať s AI a strojovým učením. Každý príklad je navrhnutý tak, aby bol priateľský k začiatočníkom s podrobnými komentármi a krok za krokom vysvetleniami.

## 📚 Prehľad príkladov

| Príklad | Popis | Obtiažnosť | Predpoklady |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Váš prvý AI program – jednoduché rozpoznávanie vzorov | ⭐ Začiatočník | Základy Pythonu |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Vytvorte neurónovú sieť od základov | ⭐⭐ Začiatočník+ | Python, základná matematika |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Klasifikujte obrázky s predtrénovaným modelom | ⭐⭐ Začiatočník+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analyzujte sentiment textu (pozitívny/negatívny) | ⭐⭐ Začiatočník+ | Python |

## 🚀 Začíname

### Predpoklady

Uistite sa, že máte nainštalovaný Python (odporúčaná verzia 3.8 alebo novšia). Nainštalujte potrebné balíčky:

```bash
# Pre Python skripty
pip install numpy

# Pre Jupyter notebooky (klasifikátor obrázkov)
pip install jupyter numpy pillow tensorflow
```

Alebo použite conda prostredie z hlavného kurzu:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Spúšťanie príkladov

**Pre Python skripty (.py súbory):**
```bash
python 01-hello-ai-world.py
```

**Pre Jupyter notebooky (.ipynb súbory):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Učebná cesta

Odporúčame nasledovať príklady v tomto poradí:

1. **Začnite s „Hello AI World“** – Naučte sa základy rozpoznávania vzorov
2. **Postavte jednoduchú neurónovú sieť** – Pochopte, ako fungujú neurónové siete
3. **Vyskúšajte klasifikátor obrázkov** – Pozrite si AI v akcii s reálnymi obrázkami
4. **Analyzujte sentiment textu** – Preskúmajte spracovanie prirodzeného jazyka

## 💡 Tipy pre začiatočníkov

- **Starostlivo čítajte komentáre v kóde** – Vysvetľujú, čo každý riadok robí
- **Experimentujte!** – Skúšajte meniť hodnoty a sledujte, čo sa stane
- **Nestrašte sa, ak všetko hneď nepochopíte** – Učenie si vyžaduje čas
- **Pýtajte sa otázky** – Použite [diskusnú platformu](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Ďalšie kroky

Po dokončení týchto príkladov preskúmajte celý kurz:
- [Úvod do AI](../lessons/1-Intro/README.md)
- [Neurónové siete](../lessons/3-NeuralNetworks/README.md)
- [Počítačové videnie](../lessons/4-ComputerVision/README.md)
- [Spracovanie prirodzeného jazyka](../lessons/5-NLP/README.md)

## 🤝 Príspevky

Páčia sa vám tieto príklady? Pomôžte nám ich zlepšiť:
- Nahláste chyby alebo navrhnite vylepšenia
- Pridajte viac príkladov pre začiatočníkov
- Zlepšite dokumentáciu a komentáre

---

*Pamätajte: Každý expert bol raz začiatočník. Šťastné učenie! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->