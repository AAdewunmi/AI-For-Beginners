# Hoe de code uit te voeren

Deze leergang bevat veel uitvoerbare voorbeelden en labs die je wilt uitvoeren. Om dit te kunnen doen, heb je de mogelijkheid nodig om Python-code uit te voeren in Jupyter Notebooks die deel uitmaken van deze leergang. Je hebt verschillende opties om de code uit te voeren:

## Lokaal op je computer uitvoeren

Om de code lokaal op je computer uit te voeren, is een Python-installatie nodig. Een aanbeveling is om **[miniconda](https://conda.io/en/latest/miniconda.html)** te installeren - dit is een vrij lichte installatie die de `conda` pakketbeheerder ondersteunt voor verschillende Python **virtuele omgevingen**.

Nadat je miniconda hebt geïnstalleerd, kloon je de repository en maak je een virtuele omgeving aan die voor deze cursus gebruikt zal worden:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Gebruik van Visual Studio Code met de Python-extensie

Deze leergang is het beste te gebruiken door deze te openen in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) met de [Python-extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opmerking**: Zodra je de map kloont en opent in VS Code, zal het automatisch voorstellen om de Python-extensies te installeren. Je moet ook miniconda installeren zoals hierboven beschreven.

> **Opmerking**: Als VS Code je voorstelt om de repository opnieuw te openen in een container, moet je dit weigeren om de lokale Python-installatie te gebruiken.

### Gebruik van Jupyter in de browser

Je kunt ook een Jupyter-omgeving vanuit de browser op je eigen computer gebruiken. Zowel klassieke Jupyter als JupyterHub bieden een handige ontwikkelomgeving met automatische aanvulling, code-kleuring, enzovoort.

Om Jupyter lokaal te starten, ga je naar de map van de cursus en voer je het volgende uit:

```bash
jupyter notebook
```
of
```bash
jupyterhub
```
Je kunt dan naar elk `.ipynb`-bestand navigeren, deze openen en beginnen met werken.

### Uitvoeren in een container

Een alternatief voor een Python-installatie is het uitvoeren van de code in een container. Omdat onze repository een speciale `.devcontainer`-map bevat die aangeeft hoe je een container bouwt voor deze repo, biedt VS Code de mogelijkheid om de code opnieuw te openen in een container. Dit vereist een Docker-installatie en is ook wat complexer, dus we raden dit aan voor meer ervaren gebruikers.

## Uitvoeren in de cloud

Als je Python niet lokaal wilt installeren en toegang hebt tot cloudresources, is een goed alternatief om de code in de cloud uit te voeren. Er zijn verschillende manieren om dit te doen:

* Gebruik **[GitHub Codespaces](https://github.com/features/codespaces)**, een virtuele omgeving die voor jou is aangemaakt op GitHub en toegankelijk is via een VS Code-browserinterface. Als je toegang hebt tot Codespaces, kun je gewoon op de **Code**-knop in de repo klikken, een codespace starten en meteen aan de slag gaan.
* Gebruik **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) biedt gratis computerkracht in de cloud voor mensen zoals jij om code van GitHub te testen. Er is een knop op de startpagina om de repository in Binder te openen - dit brengt je snel naar de Binder-site waar een onderliggende container wordt opgebouwd en naadloos een Jupyter-webinterface voor je start.

> **Opmerking**: Om misbruik te voorkomen, heeft Binder de toegang tot sommige webresources geblokkeerd. Dit kan voorkomen dat een deel van de code werkt, vooral als deze modellen en/of datasets van het publieke internet ophaalt. Je moet mogelijk een workaround vinden. Ook zijn de computerresources die door Binder worden geleverd vrij basic, dus training zal traag zijn, vooral in latere, meer complexe lessen.

## Uitvoeren in de cloud met GPU

Sommige van de latere lessen in deze leergang profiteren sterk van GPU-ondersteuning. Bijvoorbeeld het trainen van modellen kan anders erg traag zijn. Er zijn een paar opties die je kunt volgen, vooral als je toegang hebt tot cloud via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), of via je onderwijsinstelling:

* Maak een [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) aan en maak verbinding via Jupyter. Je kunt dan de repo direct op de machine klonen en beginnen met leren. NC-series VM’s hebben GPU-ondersteuning.

> **Opmerking**: Sommige abonnementen, waaronder Azure for Students, bieden niet direct GPU-ondersteuning. Je moet mogelijk extra GPU-kernen aanvragen via een technische supportaanvraag.

* Maak een [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) aan en gebruik daar de Notebook-functie. [Deze video](https://azure-for-academics.github.io/quickstart/azureml-papers/) laat zien hoe je een repository naar een Azure ML-notebook kloont en er begint mee te werken.

Je kunt ook Google Colab gebruiken, dat met wat gratis GPU-ondersteuning komt, en daar Jupyter Notebooks uploaden om ze één voor één uit te voeren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->