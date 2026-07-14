# Hvordan man kører koden

Dette pensum indeholder mange eksekverbare eksempler og laboratorier, som du vil få brug for at køre. For at gøre dette, skal du kunne eksekvere Python-kode i Jupyter Notebooks, som er en del af dette pensum. Du har flere muligheder for at køre koden:

## Kør lokalt på din computer

For at køre koden lokalt på din computer, er en Python-installation nødvendig. En anbefaling er at installere **[miniconda](https://conda.io/en/latest/miniconda.html)** - det er en relativt let installation, der understøtter `conda` pakkehåndteringen til forskellige Python **virtuelle miljøer**.

Efter du har installeret miniconda, klon repositoriet og opret et virtuelt miljø til brug for dette kursus:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Brug af Visual Studio Code med Python-udvidelsen

Dette pensum bruges bedst ved at åbne det i [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) med [Python-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Når du har klonet og åbnet mappen i VS Code, vil den automatisk foreslå at installere Python-udvidelser. Du skal også installere miniconda som beskrevet ovenfor.

> **Note**: Hvis VS Code foreslår at genåbne repositoriet i en container, skal du afslå dette for at bruge den lokale Python-installation.

### Brug af Jupyter i browseren

Du kan også bruge et Jupyter-miljø fra browseren på din egen computer. Både klassisk Jupyter og JupyterHub giver et bekvemt udviklingsmiljø med autoudfyldning, kodehighlighting osv.

For at starte Jupyter lokalt, gå til kursusmappen, og kør:

```bash
jupyter notebook
```
eller
```bash
jupyterhub
```
Du kan herefter navigere til enhver `.ipynb` fil, åbne den og begynde at arbejde.

### Kørsel i container

Et alternativ til Python-installation ville være at køre koden i en container. Da vores repo leverer en speciel `.devcontainer` mappe, der vejleder, hvordan man bygger en container til dette repo, tilbyder VS Code muligheden for at genåbne koden inde i en container. Dette kræver Docker-installation og er også mere komplekst, så vi anbefaler dette til mere erfarne brugere.

## Kørsel i skyen

Hvis du ikke ønsker at installere Python lokalt, og har adgang til nogle skyressourcer - er et godt alternativ at køre koden i skyen. Der er flere måder du kan gøre det på:

* Brug af **[GitHub Codespaces](https://github.com/features/codespaces)**, som er et virtuelt miljø oprettet til dig på GitHub, tilgængeligt gennem et VS Code browserinterface. Hvis du har adgang til Codespaces, kan du bare klikke på **Code** knappen i repoet, starte en codespace, og være i gang på ingen tid.
* Brug af **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tilbyder gratis computerressourcer leveret i skyen til folk som dig, så man kan teste noget kode fra GitHub. Der er en knap på forside, som åbner repositoriet i Binder - dette fører dig hurtigt til bindersiden, som bygger en underliggende container og starter et Jupyter webinterface for dig problemfrit.

> **Note**: For at forhindre misbrug, har Binder blokeret adgang til nogle webressourcer. Dette kan forhindre, at noget kode virker, som henter modeller og/eller datasæt fra det offentlige internet. Du kan blive nødt til at finde nogle løsninger. Derudover er de computerressourcer, som Binder leverer, ret grundlæggende, så træning vil være langsom, især i de senere, mere komplekse lektioner.

## Kørsel i skyen med GPU

Nogle af de senere lektioner i dette pensum vil have stor fordel af GPU-understøttelse. Modeltræning kan for eksempel være smertefuldt langsom ellers. Der er nogle muligheder, som du kan følge, især hvis du har adgang til skyen gennem [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), eller via din institution:

* Opret en [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) og forbind til den gennem Jupyter. Du kan så klone repoet direkte på maskinen og begynde at lære. NC-seriens VM'er har GPU-understøttelse.

> **Note**: Nogle abonnementer, inklusive Azure for Students, tilbyder ikke GPU-understøttelse som standard. Du skal muligvis anmode om ekstra GPU-kerner via en teknisk supportanmodning.

* Opret et [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) og brug derefter Notebook-funktionen dér. [Denne video](https://azure-for-academics.github.io/quickstart/azureml-papers/) viser, hvordan man kloner et repository ind i Azure ML notebook og begynder at bruge det.

Du kan også bruge Google Colab, som har noget gratis GPU-understøttelse, og uploade Jupyter Notebooks der for at eksekvere dem én ad gangen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->