# Kako zagnati kodo

Ta učni načrt vsebuje veliko izvedljivih primerov in laboratorijskih vaj, ki jih boste želeli zagnati. Za to potrebujete možnost izvajanja Pythona v Jupyter zvezkih, ki so del tega učnega načrta. Na voljo imate več možnosti za zagon kode:

## Zagon lokalno na vašem računalniku

Za zagon kode lokalno na vašem računalniku je potrebna Python namestitev. Priporočamo namestitev **[miniconda](https://conda.io/en/latest/miniconda.html)** – gre za razmeroma lahko namestitev, ki podpira upravljanje paketov `conda` za različna Python **virtualna okolja**.

Po namestitvi miniconde klonirajte repozitorij in ustvarite virtualno okolje, ki bo uporabljeno za ta tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Uporaba Visual Studio Code z razširitvijo Python

Ta učni načrt je najbolje uporabljati, če ga odprete v [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [razširitvijo Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Opomba**: Ko klonirate in odprete mapo v VS Code, vam bo samodejno predlagal namestitev Python razširitev. Prav tako boste morali namestiti minicondo, kot je opisano zgoraj.

> **Opomba**: Če vam VS Code predlaga, da repozitorij ponovno odprete v vsebniku, tega zavrnite, da boste uporabljali lokalno Python namestitev.

### Uporaba Jupyter v brskalniku

Jupyter okolje lahko uporabljate tudi iz brskalnika na svojem računalniku. Tako klasični Jupyter kot JupyterHub nudita priročno razvojno okolje z avto-dokončevanjem, poudarjanjem kode itd.

Za zagon Jupyterja lokalno pojdite v mapo s tečajem in zaženite:

```bash
jupyter notebook
```
ali
```bash
jupyterhub
```
Nato lahko odprete katere koli `.ipynb` datoteke in začnete z delom.

### Zagon v vsebniku

Ena alternativa Python namestitvi je zagon kode v vsebniku. Ker naš repozitorij vsebuje posebno mapo `.devcontainer`, ki določa, kako zgraditi vsebnik za ta repozitorij, VS Code ponuja možnost ponovnega odpiranja kode v vsebniku. To zahteva namestitev Dockerja in je nekoliko bolj zapleteno, zato priporočamo to izkušenejšim uporabnikom.

## Zagon v oblaku

Če ne želite namestiti Pythona lokalno in imate dostop do oblakov, je dobra alternativa zagon kode v oblaku. Obstaja več načinov za to:

* Uporaba **[GitHub Codespaces](https://github.com/features/codespaces)**, ki je virtualno okolje, ustvarjeno za vas na GitHubu, dostopno preko VS Code v brskalniku. Če imate dostop do Codespaces, lahko kliknete gumb **Code** v repozitoriju, zaženete codespace in začnete v hipu.
* Uporaba **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nudi brezplačne računske vire v oblaku za ljudi, ki želijo preizkusiti kodo na GitHubu. Na vstupni strani je gumb za odprtje repozitorija v Binderju – to vas bo hitro odpeljalo na Binder spletno stran, ki bo zgradila osnovni vsebnik in brez težav zagnala Jupyter spletni vmesnik.

> **Opomba**: Da prepreči zlorabe, ima Binder blokiran dostop do nekatere spletne vsebine. To lahko prepreči delovanje kode, ki prenese modele in/ali podatkovne nize iz javnega interneta. Morda boste morali najti načine za zaobid. Računski viri, ki jih nudi Binder, so precej osnovni, zato bo učenje, zlasti v poznejših, bolj zapletenih lekcijah, počasno.

## Zagon v oblaku z GPU

Nekatere poznejše lekcije v tem učnem načrtu bi močno koristi podpora GPU. Na primer, trening modela je sicer lahko zelo počasen. Obstaja nekaj možnosti, ki jih lahko uporabite, še posebej, če imate dostop do oblaka preko [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ali prek svoje institucije:

* Ustvarite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) in se povežite nanjo preko Jupyterja. Nato lahko replicirate repozitorij neposredno v stroj in začnete z učenjem. NC-serija VM-jev ima podporo za GPU.

> **Opomba**: Nekateri naročniški paketi, vključno z Azure for Students, ne nudijo podpore za GPU takoj. Morda boste morali zaprositi za dodatne GPU jedra s tehnično podporo.

* Ustvarite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) in nato uporabite funkcijo Notebook tam. [Ta video](https://azure-for-academics.github.io/quickstart/azureml-papers/) prikazuje, kako replicirati repozitorij v Azure ML notebook in ga začeti uporabljati.

Prav tako lahko uporabite Google Colab, ki nudi nekaj brezplačne podpore za GPU, in naložite Jupyter zvezke tam za izvajanje posamezno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->