# Comment exécuter le code

Ce programme contient de nombreux exemples exécutables et laboratoires que vous voudrez exécuter. Pour ce faire, vous devez pouvoir exécuter du code Python dans les notebooks Jupyter fournis dans le cadre de ce programme. Plusieurs options s'offrent à vous pour exécuter le code :

## Exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, une installation de Python est nécessaire. Une recommandation est d’installer **[miniconda](https://conda.io/en/latest/miniconda.html)** - il s'agit d'une installation assez légère qui supporte le gestionnaire de paquets `conda` pour différents **environnements virtuels** Python.

Après avoir installé miniconda, clonez le dépôt et créez un environnement virtuel à utiliser pour ce cours :

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilisation de Visual Studio Code avec l’extension Python

Ce programme s’utilise le mieux en l’ouvrant dans [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) avec l’[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note** : Une fois que vous avez cloné et ouvert le dossier dans VS Code, il vous proposera automatiquement d’installer les extensions Python. Vous devrez aussi installer miniconda comme décrit ci-dessus.

> **Note** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, vous devriez refuser ceci pour utiliser l’installation Python locale.

### Utilisation de Jupyter dans le navigateur

Vous pouvez aussi utiliser un environnement Jupyter depuis le navigateur sur votre propre ordinateur. Tant Jupyter classique que JupyterHub offrent un environnement de développement pratique avec auto-complétion, coloration syntaxique, etc.

Pour démarrer Jupyter localement, allez dans le dossier du cours, et exécutez :

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Vous pouvez alors naviguer vers n’importe quel fichier `.ipynb`, l’ouvrir et commencer à travailler.

### Exécuter dans un conteneur

Une alternative à l’installation de Python serait d’exécuter le code dans un conteneur. Étant donné que notre dépôt fournit un dossier spécial `.devcontainer` qui explique comment construire un conteneur pour ce repo, VS Code offre la possibilité de rouvrir le code dans un conteneur. Cela nécessite l’installation de Docker, et est aussi plus complexe, donc nous recommandons cette option aux utilisateurs plus expérimentés.

## Exécuter dans le cloud

Si vous ne souhaitez pas installer Python localement, et disposez d’accès à des ressources cloud, une bonne alternative serait d’exécuter le code dans le cloud. Plusieurs méthodes sont possibles :

* Utiliser **[GitHub Codespaces](https://github.com/features/codespaces)**, qui est un environnement virtuel créé pour vous sur GitHub, accessible via une interface navigateur de VS Code. Si vous avez accès à Codespaces, vous pouvez simplement cliquer sur le bouton **Code** dans le dépôt, démarrer un codespace, et commencer très rapidement.
* Utiliser **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) offre des ressources informatiques gratuites fournies dans le cloud pour permettre à des personnes comme vous d’essayer du code sur GitHub. Il y a un bouton sur la page d’accueil pour ouvrir le dépôt dans Binder - cela vous amènera rapidement au site Binder, qui construira un conteneur sous-jacent et lancera une interface web Jupyter pour vous de façon transparente.

> **Note** : Pour prévenir les abus, Binder bloque l’accès à certaines ressources web. Ceci peut empêcher une partie du code de fonctionner, notamment lorsque le code va chercher des modèles et/ou des jeux de données sur Internet. Vous pourriez devoir trouver des solutions alternatives. De plus, les ressources de calcul fournies par Binder sont assez basiques, donc l’entraînement sera lent, surtout dans les leçons plus avancées et complexes.

## Exécuter dans le cloud avec GPU

Certaines des leçons avancées de ce programme bénéficieraient grandement du support GPU. Par exemple, l’entraînement des modèles peut être très lent autrement. Vous avez plusieurs options, en particulier si vous avez accès au cloud via [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), ou via votre institution :

* Créer une [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) et s’y connecter via Jupyter. Vous pouvez alors cloner le dépôt directement sur la machine, et commencer à apprendre. Les machines virtuelles de la série NC ont un support GPU.

> **Note** : Certaines souscriptions, y compris Azure for Students, ne fournissent pas de support GPU nativement. Vous pourriez devoir demander des cœurs GPU supplémentaires via une demande de support technique.

* Créer un [Espace de travail Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) puis utiliser la fonctionnalité Notebook là-bas. [Cette vidéo](https://azure-for-academics.github.io/quickstart/azureml-papers/) montre comment cloner un dépôt dans un notebook Azure ML et commencer à l’utiliser.

Vous pouvez aussi utiliser Google Colab, qui offre un support GPU gratuit limité, et y uploader les notebooks Jupyter pour les exécuter un à un.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->