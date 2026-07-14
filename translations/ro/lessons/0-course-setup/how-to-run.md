# Cum să Rulați Codul

Acest curriculum conține multe exemple și laboratoare executabile pe care le veți dori să le rulați. Pentru a face acest lucru, aveți nevoie de capacitatea de a executa cod Python în Jupyter Notebooks furnizate ca parte a acestui curriculum. Aveți mai multe opțiuni pentru rularea codului:

## Rulare locală pe computerul dvs.

Pentru a rula codul local pe computerul dvs., este necesară o instalare Python. O recomandare este să instalați **[miniconda](https://conda.io/en/latest/miniconda.html)** - este o instalare destul de ușoară care suportă managerul de pachete `conda` pentru diferite **medii virtuale** Python.

După ce instalați miniconda, clonați depozitul și creați un mediu virtual care va fi folosit pentru acest curs:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Folosind Visual Studio Code cu Extensia Python

Acest curriculum este cel mai bine folosit deschizându-l în [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) cu [Extensia Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Notă**: Odată ce clonați și deschideți directorul în VS Code, acesta vă va sugera automat să instalați extensiile Python. De asemenea, trebuie să instalați miniconda așa cum este descris mai sus.

> **Notă**: Dacă VS Code vă sugerează să redeschideți depozitul într-un container, ar trebui să refuzați această opțiune pentru a folosi instalarea Python locală.

### Folosind Jupyter în Browser

Puteți de asemenea să folosiți un mediu Jupyter din browser pe propriul computer. Atât Jupyter clasic, cât și JupyterHub oferă un mediu de dezvoltare convenabil cu auto-completare, evidențierea codului etc.

Pentru a porni Jupyter local, mergeți în directorul cursului și executați:

```bash
jupyter notebook
```
sau
```bash
jupyterhub
```
Puteți apoi naviga la oricare dintre fișierele `.ipynb`, să le deschideți și să începeți lucrul.

### Rulare în container

O alternativă la instalarea Python ar fi să rulați codul într-un container. Deoarece depozitul nostru oferă un folder special `.devcontainer` care indică cum să construiți un container pentru acest repo, VS Code oferă posibilitatea de a redeschide codul într-un container. Acest lucru va necesita instalarea Docker și ar fi mai complex, așa că recomandăm această metodă utilizatorilor mai experimentați.

## Rulare în Cloud

Dacă nu doriți să instalați Python local și aveți acces la unele resurse cloud - o alternativă bună ar fi să rulați codul în cloud. Sunt mai multe moduri prin care puteți face acest lucru:

* Folosind **[GitHub Codespaces](https://github.com/features/codespaces)**, care este un mediu virtual creat pentru dvs. pe GitHub, accesibil printr-o interfață VS Code în browser. Dacă aveți acces la Codespaces, puteți pur și simplu să faceți clic pe butonul **Code** din repo, să porniți un codespace și să începeți rapid.
* Folosind **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferă resurse de calcul gratuite furnizate în cloud pentru oameni ca dvs. să testeze cod de pe GitHub. Există un buton pe pagina principală pentru a deschide depozitul în Binder - aceasta vă va duce rapid la site-ul Binder, care va construi un container de bază și va porni o interfață web Jupyter pentru dvs.

> **Notă**: Pentru a preveni utilizarea necorespunzătoare, Binder are accesul la unele resurse web blocat. Acest lucru poate împiedica funcționarea unor coduri care descarcă modele și/sau seturi de date de pe Internet public. Este posibil să fie nevoie să găsiți câteva soluții alternative. De asemenea, resursele de calcul oferite de Binder sunt destul de limitate, astfel antrenarea va fi lentă, în special în lecțiile ulterioare, mai complexe.

## Rulare în Cloud cu GPU

Unele dintre lecțiile ulterioare din acest curriculum ar beneficia foarte mult de suport GPU. Antrenarea modelelor, de exemplu, poate fi altfel dureros de lentă. Există câteva opțiuni pe care le puteți urma, mai ales dacă aveți acces la cloud prin [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) sau prin instituția dvs.:

* Creați [Mașina Virtuală pentru Știința Datelor](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) și conectați-vă la ea prin Jupyter. Puteți apoi să clonați repo-ul direct pe mașină și să începeți să învățați. Mașinile virtuale din seria NC au suport GPU.

> **Notă**: Unele abonamente, inclusiv Azure for Students, nu oferă suport GPU implicit. Este posibil să trebuiască să solicitați nuclee GPU suplimentare printr-un ticket de suport tehnic.

* Creați [Workspace Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) și apoi folosiți funcția Notebook acolo. [Acest video](https://azure-for-academics.github.io/quickstart/azureml-papers/) arată cum să clonați un depozit în notebook-ul Azure ML și să începeți să îl folosiți.

Puteți de asemenea să folosiți Google Colab, care oferă suport GPU gratuit și să încărcați Jupyter Notebooks acolo pentru a le executa unul câte unul.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->