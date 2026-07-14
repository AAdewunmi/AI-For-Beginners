# Jak spustit kód

Tento učební plán obsahuje spoustu spustitelných příkladů a laboratoří, které budete chtít spustit. Abyste to mohli udělat, potřebujete možnost spouštět Python kód v Jupyter Noteboocích, které jsou součástí tohoto učebního plánu. Máte několik možností, jak kód spustit:

## Spuštění lokálně na vašem počítači

Pro spuštění kódu lokálně na vašem počítači je potřeba nainstalovat Python. Jedním z doporučení je instalace **[miniconda](https://conda.io/en/latest/miniconda.html)** - jde o poměrně lehkou instalaci, která podporuje správce balíčků `conda` pro různé Python **virtuální prostředí**.

Po instalaci minicondy naklonujte repozitář a vytvořte virtuální prostředí, které budete používat pro tento kurz:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Použití Visual Studio Code s Python rozšířením

Tento učební plán je nejlepší používat po otevření v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python rozšířením](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Poznámka**: Jakmile naklonujete a otevřete složku ve VS Code, automaticky vám navrhne instalovat Python rozšíření. Dále je potřeba nainstalovat miniconda, jak je popsáno výše.

> **Poznámka**: Pokud vám VS Code navrhne znovu otevřít repozitář v kontejneru, měli byste to odmítnout, abyste mohli používat lokální instalaci Pythonu.

### Použití Jupyteru v prohlížeči

Můžete také použít Jupyter prostředí z prohlížeče na svém vlastním počítači. Jak klasický Jupyter, tak JupyterHub poskytují pohodlné vývojové prostředí s automatickým doplňováním, zvýrazněním kódu atd.

Pro spuštění Jupyteru lokálně přejděte do složky kurzu a spusťte:

```bash
jupyter notebook
```
nebo
```bash
jupyterhub
```
Poté můžete přejít k jakémukoliv `.ipynb` souboru, otevřít ho a začít pracovat.

### Spuštění v kontejneru

Alternativou k instalaci Pythonu je spustit kód v kontejneru. Náš repozitář obsahuje speciální složku `.devcontainer`, která udává, jak kontejner pro tento repozitář sestavit, a VS Code nabízí možnost kód znovu otevřít v kontejneru. To vyžaduje instalaci Dockeru a je to složitější, proto doporučujeme tuto možnost spíše pokročilým uživatelům.

## Spuštění v cloudu

Pokud nechcete instalovat Python lokálně a máte přístup k nějakým cloudovým zdrojům, dobrou alternativou je spustit kód v cloudu. Existuje několik způsobů, jak to udělat:

* Použití **[GitHub Codespaces](https://github.com/features/codespaces)**, což je virtuální prostředí vytvořené pro vás na GitHubu, přístupné přes VS Code v prohlížeči. Pokud máte přístup ke Codespaces, stačí kliknout na tlačítko **Code** v repozitáři, spustit codespace a můžete začít během chvíle.
* Použití **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nabízí zdarma výpočetní zdroje v cloudu, aby lidé jako vy mohli vyzkoušet nějaký kód na GitHubu. Na hlavní stránce je tlačítko pro otevření repozitáře v Binderu - to by vás rychle mělo přesměrovat na stránku binderu, která sestaví základní kontejner a spustí pro vás Jupyter webové rozhraní bez problémů.

> **Poznámka**: Aby se zabránilo zneužití, má Binder blokovaný přístup k některým webovým zdrojům. To může znemožnit běh některých částí kódu, které stahují modely a/nebo datasety z veřejného internetu. Možná budete muset najít nějaká obcházení. Také výpočetní zdroje poskytované Binderem jsou poměrně základní, takže trénink bude pomalý, zejména v pozdějších, složitějších lekcích.

## Spuštění v cloudu s GPU

Některé z pozdějších lekcí v tomto učebním plánu by výrazně profitovaly z podpory GPU. Trénink modelů může být jinak bolestivě pomalý. Existuje několik možností, které můžete využít, obzvlášť pokud máte přístup k cloudu buď přes [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) nebo přes vaši instituci:

* Vytvořte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) a připojte se k ní přes Jupyter. Můžete pak naklonovat repozitář přímo na stroj a začít se učit. VM řady NC mají podporu GPU.

> **Poznámka**: Některé předplatné, včetně Azure for Students, neposkytují podporu GPU automaticky. Možná budete muset požádat o dodatečné GPU jádra pomocí technické podpory.

* Vytvořte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) a použijte tam funkci Notebook. [Toto video](https://azure-for-academics.github.io/quickstart/azureml-papers/) ukazuje, jak naklonovat repozitář do Azure ML notebooku a začít ho používat.

Můžete také použít Google Colab, který nabízí nějakou bezplatnou podporu GPU, a tam nahrát Jupyter Notebooky ke spouštění jeden po druhém.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->