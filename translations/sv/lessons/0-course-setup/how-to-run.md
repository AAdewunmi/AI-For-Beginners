# Hur man kör koden

Denna kursplan innehåller många körbara exempel och laborationer som du vill köra. För att göra detta behöver du möjligheten att köra Python-kod i Jupyter Notebooks som tillhandahålls som en del av denna kurs. Du har flera alternativ för att köra koden:

## Kör lokalt på din dator

För att köra koden lokalt på din dator behövs en Python-installation. Ett rekommenderat alternativ är att installera **[miniconda](https://conda.io/en/latest/miniconda.html)** – det är en ganska lätt installation som stöder `conda` paket hanterare för olika Python **virtuella miljöer**.

Efter att du installerat miniconda, klona repositoryt och skapa en virtuell miljö som ska användas för denna kurs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Använda Visual Studio Code med Python Extension

Denna kursplan används bäst när du öppnar den i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Obs**: När du har klonat och öppnat katalogen i VS Code kommer det automatiskt att föreslå att du installerar Python-tillägg. Du måste också installera miniconda som beskrivs ovan.

> **Obs**: Om VS Code föreslår att du öppnar repositoryt igen i en container bör du tacka nej till detta för att kunna använda den lokala Python-installationen.

### Använda Jupyter i webbläsaren

Du kan också använda en Jupyter-miljö från webbläsaren på din egen dator. Både klassisk Jupyter och JupyterHub erbjuder en bekväm utvecklingsmiljö med automatisk komplettering, kodmarkering etc.

För att starta Jupyter lokalt, gå till kurskatalogen och kör:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan sedan navigera till valfri `.ipynb`-fil, öppna den och börja arbeta.

### Köra i container

Ett alternativ till Python-installation är att köra koden i en container. Eftersom vårt repository innehåller en speciell `.devcontainer`-mapp som instruerar hur man bygger en container för detta repo, erbjuder VS Code möjligheten att öppna koden i en container. Detta kräver Docker-installation och är mer komplext, så vi rekommenderar detta för mer erfarna användare.

## Köra i molnet

Om du inte vill installera Python lokalt och har tillgång till molnresurser är ett bra alternativ att köra koden i molnet. Det finns flera sätt att göra detta:

* Använd **[GitHub Codespaces](https://github.com/features/codespaces)**, vilket är en virtuell miljö skapad för dig på GitHub, tillgänglig via ett VS Code webbläsargränssnitt. Om du har tillgång till Codespaces kan du bara klicka på **Code**-knappen i repo, starta en codespace och komma igång på nolltid.
* Använd **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) erbjuder gratis datorkraft i molnet för personer som du att testa kod från GitHub. Det finns en knapp på framsidan för att öppna repositoryt i Binder – detta tar dig snabbt till binder-webbplatsen, som bygger en underliggande container och startar ett Jupyter webgränssnitt för dig sömlöst.

> **Obs**: För att förhindra missbruk har Binder blockerat åtkomst till vissa webbresurser. Detta kan hindra vissa delar av koden från att fungera, särskilt de som hämtar modeller och/eller dataset från det offentliga Internet. Du kan behöva hitta några lösningar. Dessutom är de datorkraftresurser som Binder tillhandahåller ganska grundläggande, så träning kommer att vara långsam, särskilt i senare och mer komplexa lektioner.

## Köra i molnet med GPU

Vissa av de senare lektionerna i denna kursplan skulle ha stor nytta av GPU-stöd. Modellträning, till exempel, kan vara smärtsamt långsam annars. Det finns några alternativ du kan följa, särskilt om du har tillgång till molnet antingen via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) eller via din institution:

* Skapa [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) och anslut till den via Jupyter. Du kan då klona repo direkt på maskinen och börja lära dig. NC-seriens VM:er har GPU-stöd.

> **Obs**: Vissa prenumerationer, inklusive Azure for Students, erbjuder inte GPU-stöd direkt. Du kan behöva begära extra GPU-kärnor med en teknisk supportförfrågan.

* Skapa [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) och använd sedan Notebook-funktionen där. [Denna video](https://azure-for-academics.github.io/quickstart/azureml-papers/) visar hur man klonar ett repository till Azure ML-notebook och börjar använda det.

Du kan också använda Google Colab, som har viss gratis GPU-stöd, och ladda upp Jupyter Notebooks där för att köra dem en efter en.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->