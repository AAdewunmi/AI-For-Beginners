# Příklady pro začátečníky s AI

Vítejte! Tento adresář obsahuje jednoduché, samostatné příklady, které vám pomohou začít s AI a strojovým učením. Každý příklad je navržen tak, aby byl přívětivý pro začátečníky s podrobnými komentáři a krok za krokem vysvětleními.

## 📚 Přehled příkladů

| Příklad | Popis | Obtížnost | Předpoklady |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Váš první program s AI - jednoduché rozpoznávání vzorů | ⭐ Začátečník | Základy Pythonu |
| [Jednoduchá neuronová síť](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Vytvořte neuronovou síť od začátku | ⭐⭐ Pokročilý začátečník | Python, základní matematika |
| [Klasifikátor obrázků](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Klasifikujte obrázky s předtrénovaným modelem | ⭐⭐ Pokročilý začátečník | Python, numpy |
| [Sentiment textu](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analyzujte sentiment textu (pozitivní/negativní) | ⭐⭐ Pokročilý začátečník | Python |

## 🚀 Začínáme

### Předpoklady

Ujistěte se, že máte nainstalovaný Python (doporučeno verze 3.8 nebo vyšší). Nainstalujte požadované balíčky:

```bash
# Pro Python skripty
pip install numpy

# Pro Jupyter notebooky (klasifikátor obrazů)
pip install jupyter numpy pillow tensorflow
```

Nebo použijte conda prostředí z hlavního kurzu:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Spuštění příkladů

**Pro Python skripty (.py soubory):**
```bash
python 01-hello-ai-world.py
```

**Pro Jupyter notebooky (.ipynb soubory):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Studijní cesta

Doporučujeme postupovat podle příkladů v tomto pořadí:

1. **Začněte s „Hello AI World“** - Naučte se základy rozpoznávání vzorů
2. **Postavte jednoduchou neuronovou síť** - Pochopte, jak neuronové sítě fungují
3. **Vyzkoušejte klasifikátor obrázků** - Uvidíte AI v akci s reálnými obrázky
4. **Analyzujte sentiment textu** - Prozkoumejte zpracování přirozeného jazyka

## 💡 Tipy pro začátečníky

- **Pečlivě si přečtěte komentáře v kódu** - Vysvětlují, co každý řádek dělá
- **Experimentujte!** - Zkoušejte měnit hodnoty a sledujte, co se stane
- **Nebuďte znepokojeni, když nerozumíte hned všemu** - Učení vyžaduje čas
- **Ptejte se** - Použijte [diskuzní fórum](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Další kroky

Po dokončení těchto příkladů prozkoumejte celý kurz:
- [Úvod do AI](../lessons/1-Intro/README.md)
- [Neuronové sítě](../lessons/3-NeuralNetworks/README.md)
- [Počítačové vidění](../lessons/4-ComputerVision/README.md)
- [Zpracování přirozeného jazyka](../lessons/5-NLP/README.md)

## 🤝 Přispění

Považujete tyto příklady za užitečné? Pomozte nám je zlepšit:
- Nahlaste problémy nebo navrhněte zlepšení
- Přidejte více příkladů pro začátečníky
- Vylepšete dokumentaci a komentáře

---

*Pamatujte: Každý expert byl jednou začátečník. Přejeme šťastné učení! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->