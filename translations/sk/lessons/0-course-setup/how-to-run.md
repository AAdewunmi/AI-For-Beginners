# Ako spustiť kód

Tento učebný plán obsahuje veľa spustiteľných príkladov a laboratórií, ktoré budete chcieť spustiť. Aby ste to mohli urobiť, potrebujete možnosť vykonávať Python kód v Jupyter Notebookoch, ktoré sú súčasťou tohto učebného plánu. Máte niekoľko možností, ako spustiť kód:

## Spustenie lokálne na vašom počítači

Na spustenie kódu lokálne na vašom počítači je potrebná inštalácia Pythonu. Jedným z odporúčaní je nainštalovať **[miniconda](https://conda.io/en/latest/miniconda.html)** – je to pomerne ľahká inštalácia, ktorá podporuje správcu balíkov `conda` pre rôzne Python **virtuálne prostredia**.

Po nainštalovaní minicondy si naklonujte repozitár a vytvorte virtuálne prostredie, ktoré budete používať pre tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Používanie Visual Studio Code s Python rozšírením

Tento učebný plán je najlepšie používať pri otvorení v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python rozšírením](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Poznámka**: Po naklonovaní a otvorení priečinka vo VS Code vám automaticky odporučí nainštalovať Python rozšírenia. Tiež si musíte nainštalovať minicondu, ako bolo popísané vyššie.

> **Poznámka**: Ak vám VS Code navrhne znovu otvoriť repozitár v kontajneri, mali by ste tento návrh odmietnuť, aby ste použili lokálnu inštaláciu Pythonu.

### Používanie Jupyteru v prehliadači

Môžete tiež použiť Jupyter prostredie z prehliadača na vašom počítači. Klasický Jupyter aj JupyterHub poskytujú pohodlné vývojové prostredie s automatickým dopĺňaním, zvýraznením kódu a pod.

Na spustenie Jupyteru lokálne prejdite do priečinka kurzu a vykonajte:

```bash
jupyter notebook
```
 alebo
```bash
jupyterhub
```
 Potom môžete prechádzať k ľubovoľným `.ipynb` súborom, otvárať ich a začať pracovať.

### Spustenie v kontajneri

Jednou z alternatív inštalácie Pythonu je spustiť kód v kontajneri. Keďže náš repozitár obsahuje špeciálny priečinok `.devcontainer`, ktorý určuje, ako sa má kontajner pre tento repozitár zostaviť, VS Code ponúka možnosť znovu otvoriť kód v kontajneri. To bude vyžadovať inštaláciu Dockeru a je to zložitejšie, preto to odporúčame skúsenejším používateľom.

## Spustenie v cloude

Ak nechcete inštalovať Python lokálne a máte prístup k nejakým cloudovým zdrojom, dobrou alternatívou je spúšťať kód v cloude. Existuje niekoľko spôsobov, ako to môžete urobiť:

* Použitie **[GitHub Codespaces](https://github.com/features/codespaces)**, čo je virtuálne prostredie vytvorené pre vás na GitHube, prístupné prostredníctvom rozhrania VS Code v prehliadači. Ak máte prístup ku Codespaces, stačí kliknúť na tlačidlo **Code** v repozitári, spustiť codespace a môžete okamžite začať.
* Použitie **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ponúka voľné výpočtové zdroje v cloude pre ľudí ako ste vy, aby mohli testovať kód na GitHube. Na hlavnej stránke nájdete tlačidlo na otvorenie repozitára v Bindri – to vás rýchlo zavedie na stránku bindra, ktorá zostaví podkladový kontajner a bezproblémovo spustí webové rozhranie Jupyter.

> **Poznámka**: Na prevenciu zneužitia má Binder zablokovaný prístup k niektorým webovým zdrojom. To môže spôsobiť, že niektoré časti kódu, ktoré sťahujú modely a/alebo dataset zo siete, nemusia fungovať. Možno budete musieť nájsť nejaké alternatívne riešenie. Tiež výpočtové zdroje, ktoré Binder poskytuje, sú pomerne základné, takže tréning bude pomalý, najmä v neskorších, zložitejších lekciách.

## Spustenie v cloude s GPU

Niektoré z neskorších lekcií v tomto učebnom pláne by veľmi profitovali zo podpory GPU. Napríklad tréning modelu môže byť inak bolestivo pomalý. Môžete postupovať niektorým z nasledujúcich spôsobov, najmä ak máte prístup ku cloudu buď cez [Azure pre študentov](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), alebo cez vašu inštitúciu:

* Vytvorte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a pripojte sa k nej cez Jupyter. Môžete si potom klonovať repozitár priamo na túto mašinu a začať s učením. NC-series VM podporujú GPU.

> **Poznámka**: Niektoré predplatné, vrátane Azure pre študentov, neposkytujú GPU podporu automaticky. Možno budete musieť požiadať o ďalšie GPU jadrá cez technickú podporu.

* Vytvorte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a potom využite funkciu Notebook tam. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, ako naklonovať repozitár do Azure ML notebooku a začať ho používať.

Môžete tiež použiť Google Colab, ktorý má zadarmo určitú podporu GPU, a nahrať tam Jupyter Notebooky na spustenie jeden po druhom.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->