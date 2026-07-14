# How to Run di Code

Dis curriculum get plenti executable example dem and lab dem wey you go like run. To fit do dis, you need di ability to run Python code for Jupyter Notebooks wey dem provide as part of dis curriculum. You get plenty options to run di code:

## Run am for your computer

To run di code for your own computer, you need to install Python first. One wey we recommend na to install **[miniconda](https://conda.io/en/latest/miniconda.html)** - e light well well and e get support for `conda` package manager for different Python **virtual environments**.

After you don install miniconda, clone di repository and create virtual environment wey you go use for dis course:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### How to Take Use Visual Studio Code with Python Extension

Dis curriculum beta pass if you open am for [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) with [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Note**: Once you clone am and open di folder for VS Code, e go automatically want make you install Python extensions. You still go need install miniconda as we talk for up.

> **Note**: If VS Code tell you make you open repository again for container, no accept am if you wan use local Python installation.

### How to Use Jupyter for Browser

You fit also run Jupyter environment from your browser for your computer. Both classical Jupyter and JupyterHub dey give you beta development environment with auto-completion, code highlighting, and others.

To start Jupyter for your computer, waka go the course directory, and run:

```bash
jupyter notebook
```
or
```bash
jupyterhub
```
After dat you fit open any `.ipynb` files, open dem and start to work.

### How to Run Inside Container

One other way to run Python na to run am inside container. Because our repo get special `.devcontainer` folder wey dey show how to build container for this repo, VS Code dey give chance to open code for container. You go need Docker install, and e go get some yawa, so we recommend am for people wey sabi small.

## How to Run am for Cloud

If you no wan install Python for your machine, and you get access to cloud resources - one beta option na to run code for cloud. You get different ways to do am:

* Use **[GitHub Codespaces](https://github.com/features/codespaces)**, na virtual environment wey dem create for you for GitHub, wey fit enter through VS Code browser interface. If you get Codespaces access, you fit just click **Code** button for repo, start codespace and run quick quick.
* Use **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) dey give free computing resources for cloud make people like you fit test some code wey dey GitHub. For front page, you go see button to open repo for Binder - e go carry you go binder site quick, wey go build container under and start Jupyter web interface for you without palava.

> **Note**: To make sure say people no misuse am, Binder block some web resources. This fit make some code no work if dem dey fetch models or datasets from public Internet. You fit need find workaround. Compute resources wey Binder provide na basic level, so training go slow, especially for later, more complex lessons dem.

## How to Run am for Cloud with GPU

Some of di later lessons for dis curriculum go beta well if dem get GPU support. Model training fit be very slow if no get am. You fit follow some options, especially if you get cloud access from [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), or from your school:

* Create [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) and connect am through Jupyter. You fit clone di repo directly for the machine, and start to learn. NC-series VMs get GPU support.

> **Note**: Some subscriptions, including Azure for Students, no dey provide GPU support straight. You fit need request extra GPU cores with technical support.

* Create [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) and use Notebook feature for there. [Dis video](https://azure-for-academics.github.io/quickstart/azureml-papers/) show how to clone repo into Azure ML notebook and start to use am.

You fit also use Google Colab wey get some free GPU support, and upload Jupyter Notebooks make you run dem one by one.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->