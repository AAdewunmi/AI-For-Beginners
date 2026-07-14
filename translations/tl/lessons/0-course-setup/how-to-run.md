# Paano Patakbuhin ang Kodigo

Ang kurikulum na ito ay naglalaman ng maraming maisasagawang halimbawa at mga laboratoryo na nais mong patakbuhin. Upang magawa ito, kailangan mong magkaroon ng kakayahang magpatakbo ng Python code sa Jupyter Notebooks na ibinigay bilang bahagi ng kurikulum na ito. Mayroon kang ilang mga opsyon para patakbuhin ang kodigo:

## Patakbuhin nang lokal sa iyong computer

Upang patakbuhin ang kodigo nang lokal sa iyong computer, kinakailangan ang isang pag-install ng Python. Isang rekomendasyon ay mag-install ng **[miniconda](https://conda.io/en/latest/miniconda.html)** - ito ay isang magaan na pag-install na sumusuporta sa `conda` package manager para sa iba't ibang mga Python **virtual environment**.

Pagkatapos mong mag-install ng miniconda, i-clone ang repositoryo at gumawa ng virtual environment na gagamitin para sa kursong ito:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Paggamit ng Visual Studio Code na may Python Extension

Ang kurikulum na ito ay pinakamainam gamitin kapag binuksan ito sa [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) na may [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Tandaan**: Kapag na-clone mo na at binuksan ang direktoryo sa VS Code, awtomatiko nitong mungkahiang mag-install ka ng mga Python extension. Kailangan mo ring mag-install ng miniconda gaya ng ipinaliwanag sa itaas.

> **Tandaan**: Kung iminumungkahi ng VS Code na muling buksan ang repositoryo sa isang container, dapat mong tanggihan ito upang magamit ang lokal na Python installation.

### Paggamit ng Jupyter sa Browser

Maaari mo ring gamitin ang isang Jupyter environment mula sa browser sa iyong sariling computer. Parehong ang klasikong Jupyter at JupyterHub ay nag-aalok ng maginhawang kapaligiran sa pag-develop na may auto-completion, pag-highlight ng code, atbp.

Upang simulan ang Jupyter nang lokal, pumunta sa direktoryo ng kurso, at patakbuhin ang:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Maaari ka nang mag-navigate sa kahit anong `.ipynb` na mga file, buksan ang mga ito at simulan ang pag-trabaho.

### Pagpapatakbo sa container

Isang alternatibo sa pag-install ng Python ay ang pagpapatakbo ng kodigo sa isang container. Dahil ang aming repositoryo ay nagbibigay ng isang espesyal na `.devcontainer` folder na nagtuturo kung paano bumuo ng isang container para sa repo na ito, inaalok ng VS Code ang pagkakataong muling buksan ang kodigo sa isang container. Kakailanganin nito ang pag-install ng Docker, at magiging mas kumplikado, kaya inirerekomenda namin ito para sa mga mas bihasang gumagamit.

## Pagpapatakbo sa Cloud

Kung ayaw mong mag-install ng Python nang lokal, at may access ka sa ilang mga cloud resources - isang magandang alternatibo ang pagpapatakbo ng kodigo sa cloud. May ilang paraan upang gawin ito:

* Paggamit ng **[GitHub Codespaces](https://github.com/features/codespaces)**, na isang virtual environment na nilikha para sa iyo sa GitHub, na ma-access sa pamamagitan ng interface ng browser ng VS Code. Kung may access ka sa Codespaces, maaari mo lang i-click ang **Code** button sa repo, magsimula ng codespace, at agad na magsimula.
* Paggamit ng **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. Nag-aalok ang [Binder](https://mybinder.org) ng mga libreng computing na resources na ibinibigay sa cloud para sa mga taong kagaya mo upang subukan ang ilang kodigo sa GitHub. May button sa front page para buksan ang repositoryo sa Binder - dadalhin ka nito agad sa binder site, na bubuo ng isang underlying container at magsisimula ng isang Jupyter web interface para sa iyo nang walang abala.

> **Tandaan**: Upang maiwasan ang maling paggamit, may akses ang Binder sa ilang mga web resource na naka-block. Maaaring hadlangan nito ang ilang bahagi ng kodigo na gumagana, lalo na yung humihingi ng mga modelo at/o datasets mula sa pampublikong Internet. Maaaring kailanganin mong humanap ng ibang paraan. Gayundin, ang computing resources na ibinibigay ng Binder ay medyo basic lang, kaya mabagal ang training, lalo na sa mga huling leksyon na mas kumplikado.

## Pagpapatakbo sa Cloud na may GPU

Ang ilan sa mga huling leksyon sa kurikulum na ito ay malaki ang mapapakinabangan mula sa suporta ng GPU. Halimbawa, ang pagte-train ng modelo ay maaaring maging napakabagal kung wala ito. May ilang mga opsyon na maaari mong sundan, lalo na kung may access ka sa cloud sa pamamagitan ng [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o mula sa iyong institusyon:

* Gumawa ng [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) at kumonekta dito gamit ang Jupyter. Maaari mong i-clone ang repo diretso sa makina, at simulan ang pag-aaral. Ang NC-series na mga VM ay may suporta sa GPU.

> **Tandaan**: Ang ilang mga subscription, kabilang ang Azure for Students, ay hindi agad nagbibigay ng suporta sa GPU. Maaaring kailanganin mong humiling ng karagdagang mga GPU core sa pamamagitan ng technical support request.

* Gumawa ng [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) at pagkatapos ay gamitin ang Notebook feature doon. [Ang video na ito](https://azure-for-academics.github.io/quickstart/azureml-papers/) ay nagpapakita kung paano i-clone ang repository sa Azure ML notebook at simulan itong gamitin.

Maaari mo ring gamitin ang Google Colab, na may kasamang libreng suporta sa GPU, at i-upload ang mga Jupyter Notebooks doon upang patakbuhin ang mga ito isa-isa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->