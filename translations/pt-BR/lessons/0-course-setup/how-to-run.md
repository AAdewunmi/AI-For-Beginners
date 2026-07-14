# Como Executar o Código

Este currículo contém muitos exemplos executáveis e laboratórios que você vai querer executar. Para isso, é necessário ter a capacidade de executar código Python em Jupyter Notebooks fornecidos como parte deste currículo. Você tem várias opções para executar o código:

## Executar localmente no seu computador

Para executar o código localmente no seu computador, é necessária a instalação do Python. Uma recomendação é instalar o **[miniconda](https://conda.io/en/latest/miniconda.html)** - é uma instalação bastante leve que suporta o gerenciador de pacotes `conda` para diferentes **ambientes virtuais** de Python.

Após instalar o miniconda, clone o repositório e crie um ambiente virtual para ser usado neste curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando Visual Studio Code com Extensão Python

Este currículo é melhor utilizado quando aberto no [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) com a [Extensão Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Uma vez que você clona e abre o diretório no VS Code, ele automaticamente sugerirá a instalação das extensões Python. Você também deverá instalar o miniconda conforme descrito acima.

> **Nota**: Se o VS Code sugerir que você reabra o repositório em um container, você deve recusar para usar a instalação local do Python.

### Usando Jupyter no Navegador

Você também pode usar um ambiente Jupyter a partir do navegador no seu próprio computador. Tanto o Jupyter clássico quanto o JupyterHub oferecem um ambiente de desenvolvimento conveniente com autocompletar, realce de código, etc.

Para iniciar o Jupyter localmente, vá ao diretório do curso e execute:

```bash
jupyter notebook
```
 ou
```bash
jupyterhub
```
 Você então pode navegar até qualquer um dos arquivos `.ipynb`, abri-los e começar a trabalhar.

### Executando em container

Uma alternativa à instalação do Python é executar o código em um container. Como nosso repositório fornece uma pasta especial `.devcontainer` que indica como construir um container para este repositório, o VS Code oferece a oportunidade de reabrir o código em um container. Isso exigirá a instalação do Docker e será mais complexo, por isso recomendamos para usuários mais experientes.

## Executando na Nuvem

Se você não quiser instalar o Python localmente e tiver acesso a alguns recursos na nuvem, uma boa alternativa é executar o código na nuvem. Há várias maneiras de fazer isso:

* Usando **[GitHub Codespaces](https://github.com/features/codespaces)**, que é um ambiente virtual criado para você no GitHub, acessível através da interface do VS Code no navegador. Se você tiver acesso ao Codespaces, basta clicar no botão **Code** no repositório, iniciar um codespace e começar rapidamente.
* Usando **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. O [Binder](https://mybinder.org) oferece recursos computacionais gratuitos fornecidos na nuvem para pessoas como você testarem algum código no GitHub. Há um botão na página inicial para abrir o repositório no Binder - isso deve levá-lo rapidamente ao site do binder, que construirá um container subjacente e iniciará uma interface web Jupyter para você sem dificuldades.

> **Nota**: Para evitar uso indevido, o Binder bloqueia o acesso a alguns recursos da web. Isso pode impedir que parte do código funcione, especialmente aqueles que buscam modelos e/ou conjuntos de dados da Internet pública. Você pode precisar encontrar algumas soluções alternativas. Além disso, os recursos de computação fornecidos pelo Binder são bastante básicos, então o treinamento será lento, especialmente em aulas mais avançadas e complexas.

## Executando na Nuvem com GPU

Algumas das aulas mais avançadas deste currículo se beneficiariam muito do suporte a GPU. O treinamento de modelos, por exemplo, pode ser extremamente lento sem isso. Há algumas opções que você pode seguir, especialmente se você tiver acesso à nuvem por meio do [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ou através da sua instituição:

* Criar uma [Máquina Virtual de Ciência de Dados](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) e conectar a ela através do Jupyter. Você pode então clonar o repositório diretamente na máquina e começar a aprender. Máquinas virtuais da série NC têm suporte a GPU.

> **Nota**: Algumas assinaturas, incluindo o Azure for Students, não fornecem suporte a GPU por padrão. Você pode precisar solicitar núcleos adicionais de GPU através de um pedido de suporte técnico.

* Criar um [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) e depois usar o recurso de Notebooks lá. [Este vídeo](https://azure-for-academics.github.io/quickstart/azureml-papers/) mostra como clonar um repositório em um notebook do Azure ML e começar a usá-lo.

Você também pode usar o Google Colab, que oferece algum suporte gratuito a GPU, e fazer upload dos Jupyter Notebooks para executar um por um.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->