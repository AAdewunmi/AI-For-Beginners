# Come Eseguire il Codice

Questo curriculum contiene molti esempi eseguibili e laboratori che vorrai eseguire. Per farlo, hai bisogno della possibilità di eseguire codice Python nei Jupyter Notebook forniti come parte di questo curriculum. Hai diverse opzioni per eseguire il codice:

## Esegui localmente sul tuo computer

Per eseguire il codice localmente sul tuo computer, è necessaria un'installazione di Python. Una raccomandazione è quella di installare **[miniconda](https://conda.io/en/latest/miniconda.html)** - è un'installazione piuttosto leggera che supporta il gestore di pacchetti `conda` per diversi **ambienti virtuali** Python.

Dopo aver installato miniconda, clona il repository e crea un ambiente virtuale da usare per questo corso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usare Visual Studio Code con l'Estensione Python

Questo curriculum è meglio utilizzato aprendolo in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con l'[Estensione Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una volta che cloni e apri la cartella in VS Code, ti suggerirà automaticamente di installare le estensioni Python. Dovrai anche installare miniconda come descritto sopra.

> **Nota**: Se VS Code ti suggerisce di riaprire il repository in un contenitore, dovresti rifiutare per usare l'installazione Python locale.

### Usare Jupyter nel Browser

Puoi anche usare un ambiente Jupyter dal browser sul tuo computer. Sia Jupyter classico che JupyterHub forniscono un ambiente di sviluppo comodo con completamento automatico, evidenziazione del codice, ecc.

Per avviare Jupyter localmente, vai nella cartella del corso ed esegui:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Poi puoi navigare su qualsiasi file `.ipynb`, aprirlo e iniziare a lavorare.

### Esecuzione in contenitore

Un'alternativa all'installazione di Python sarebbe eseguire il codice in un contenitore. Poiché il nostro repository fornisce una cartella speciale `.devcontainer` che indica come costruire un contenitore per questo repo, VS Code offre la possibilità di riaprire il codice in un contenitore. Questo richiederà l'installazione di Docker e sarebbe più complesso, quindi raccomandiamo questo a utenti più esperti.

## Esecuzione nel Cloud

Se non vuoi installare Python localmente e hai accesso a risorse cloud, un'ottima alternativa è eseguire il codice nel cloud. Ci sono diversi modi per farlo:

* Usare **[GitHub Codespaces](https://github.com/features/codespaces)**, che è un ambiente virtuale creato per te su GitHub, accessibile tramite un'interfaccia browser di VS Code. Se hai accesso a Codespaces, puoi semplicemente cliccare il pulsante **Code** nel repo, avviare un codespace e iniziare subito.
* Usare **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre risorse di calcolo gratuite nel cloud per persone come te per testare codice su GitHub. C'è un pulsante nella pagina principale per aprire il repository in Binder - questo ti porterà rapidamente al sito di Binder, che costruirà un contenitore sottostante e avvierà un'interfaccia web Jupyter per te senza soluzione di continuità.

> **Nota**: Per prevenire abusi, Binder ha accesso bloccato ad alcune risorse web. Questo può impedire ad alcune parti del codice di funzionare, che recuperano modelli e/o dataset da Internet pubblico. Potresti dover trovare qualche soluzione alternativa. Inoltre, le risorse di calcolo fornite da Binder sono piuttosto basiche, quindi l'addestramento sarà lento, specialmente nelle lezioni più avanzate e complesse.

## Esecuzione nel Cloud con GPU

Alcune delle lezioni avanzate in questo curriculum trarrebbero gran beneficio dal supporto GPU. L'addestramento di modelli, per esempio, può essere dolorosamente lento senza. Ci sono alcune opzioni che puoi seguire, specialmente se hai accesso al cloud tramite [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o tramite la tua istituzione:

* Creare una [Virtual Machine per Data Science](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e connettersi ad essa tramite Jupyter. Puoi poi clonare il repo direttamente sulla macchina e iniziare a studiare. Le VM serie NC hanno supporto GPU.

> **Nota**: Alcuni abbonamenti, incluso Azure for Students, non forniscono supporto GPU predefinito. Potresti dover richiedere core GPU aggiuntivi tramite una richiesta di supporto tecnico.

* Creare uno [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e poi usare la funzione Notebook lì. [Questo video](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra come clonare un repository in un notebook Azure ML e iniziare a usarlo.

Puoi anche usare Google Colab, che include un certo supporto GPU gratuito, e caricare i Jupyter Notebook lì per eseguirli uno per uno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->