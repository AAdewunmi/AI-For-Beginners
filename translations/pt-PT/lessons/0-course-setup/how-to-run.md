# Como Executar o Código

Este currículo contém muitos exemplos e laboratórios executáveis que desejará correr. Para tal, precisa da capacidade de executar código Python em Jupyter Notebooks fornecidos como parte deste currículo. Tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, é necessário uma instalação de Python. Uma recomendação é instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação bastante leve que suporta o gestor de pacotes `conda` para diferentes **ambientes virtuais** Python.

Depois de instalar o miniconda, clone o repositório e crie um ambiente virtual a usar neste curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Utilizar o Visual Studio Code com a Extensão Python

Este currículo é melhor utilizado ao abri-lo no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Uma vez que clone e abra o diretório no VS Code, irá automaticamente sugerir-lhe a instalação das extensões Python. Também terá que instalar o miniconda conforme descrito acima.

> **Nota**: Se o VS Code lhe sugerir reabrir o repositório num contentor, deve recusar para usar a instalação local do Python.

### Utilizar o Jupyter no Navegador

Também pode usar um ambiente Jupyter a partir do navegador no seu próprio computador. Tanto o Jupyter clássico como o JupyterHub fornecem um ambiente de desenvolvimento conveniente com auto-completação, realce de código, etc.

Para iniciar o Jupyter localmente, vá para o diretório do curso e execute:

```bash
jupyter notebook
```
ou
```bash
jupyterhub
```
Pode então navegar a qualquer um dos ficheiros `.ipynb`, abri-los e começar a trabalhar.

### Executar num contentor

Uma alternativa à instalação do Python seria executar o código num contentor. Como o nosso repositório fornece uma pasta especial `.devcontainer` que indica como construir um contentor para este repositório, o VS Code oferece a oportunidade de reabrir o código num contentor. Isto requer a instalação do Docker e seria também mais complexo, por isso recomendamos isto para utilizadores mais experientes.

## Execução na Nuvem

Se não quiser instalar Python localmente e tiver acesso a alguns recursos na nuvem - uma boa alternativa seria executar o código na nuvem. Existem várias formas de o fazer:

* Utilizando **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para si no GitHub, acessível através de uma interface do VS Code no navegador. Se tiver acesso ao Codespaces, pode simplesmente clicar no botão **Code** no repositório, iniciar um codespace e ficar a correr em pouco tempo.
* Utilizando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. O [Binder](https://mybinder.org) oferece recursos computacionais gratuitos disponibilizados na nuvem para pessoas como você testarem algum código no GitHub. Existe um botão na página principal para abrir o repositório no Binder - isto deverá levá-lo rapidamente ao site do binder, que irá construir um contentor base e iniciar uma interface web do Jupyter para si sem interrupções.

> **Nota**: Para prevenir uso indevido, o Binder tem acesso bloqueado a alguns recursos web. Isto pode impedir que algum código funcione, especialmente aquele que obtém modelos e/ou conjuntos de dados da Internet pública. Pode ser necessário encontrar algumas soluções alternativas. Além disso, os recursos computacionais fornecidos pelo Binder são bastante básicos, por isso o treino será lento, especialmente nas lições posteriores mais complexas.

## Execução na Nuvem com GPU

Algumas das lições posteriores neste currículo beneficiariam muito do suporte a GPU. O treino de modelos, por exemplo, pode ser dolorosamente lento de outra forma. Existem algumas opções que pode seguir, especialmente se tiver acesso à nuvem seja através do [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), ou através da sua instituição:

* Crie uma [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e ligue-se a ela através do Jupyter. Pode então clonar o repositório diretamente na máquina e começar a aprender. As VMs da série NC têm suporte GPU.

> **Nota**: Algumas subscrições, incluindo o Azure for Students, não fornecem suporte a GPU imediatamente. Pode ser necessário solicitar núcleos GPU adicionais através de um pedido de suporte técnico.

* Crie um [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e utilize depois a funcionalidade de Notebook lá. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório num notebook Azure ML e começar a utilizá-lo.

Também pode usar o Google Colab, que vem com algum suporte GPU gratuito, e carregar aí os Jupyter Notebooks para os executar um por um.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->