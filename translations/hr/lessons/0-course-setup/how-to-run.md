# Kako pokrenuti kod

Ovaj kurikulum sadrži mnogo izvršnih primjera i laboratorijskih zadataka koje biste željeli pokrenuti. Da biste to učinili, trebate mogućnost izvršavanja Python koda u Jupyter Notebookovima koje su uključene kao dio ovog kurikuluma. Imate nekoliko opcija za pokretanje koda:

## Pokretanje lokalno na vašem računalu

Za pokretanje koda lokalno na vašem računalu potrebna je instalacija Pythona. Jedan od prijedloga je instalirati **[miniconda](https://conda.io/en/latest/miniconda.html)** - to je prilično lagana instalacija koja podržava `conda` upravitelj paketa za različita Python **virtualna okruženja**.

Nakon što instalirate miniconda, klonirajte repozitorij i napravite virtualno okruženje koje ćete koristiti za ovaj tečaj:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Korištenje Visual Studio Code s Python proširenjem

Ovaj kurikulum je najbolje koristiti pritom da ga otvorite u [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) s [Python proširenjem](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Napomena**: Nakon što klonirate i otvorite direktorij u VS Code, on će vam automatski ponuditi instalaciju Python proširenja. Također ćete trebati instalirati miniconda kako je opisano gore.

> **Napomena**: Ako vam VS Code ponudi da ponovo otvorite repozitorij u kontejneru, trebali biste to odbiti da biste koristili lokalnu Python instalaciju.

### Korištenje Jupyter u pregledniku

Također možete koristiti Jupyter okruženje putem preglednika na vlastitom računalu. I klasični Jupyter i JupyterHub nude prikladno razvojno okruženje s automatskim dovršavanjem, isticanjem koda i slično.

Za pokretanje Jupyter-a lokalno, idite u direktorij s tečajem i pokrenite:

```bash
jupyter notebook
```
ili
```bash
jupyterhub
```
Nakon toga možete navigirati do bilo koje `.ipynb` datoteke, otvoriti je i početi raditi.

### Pokretanje u kontejneru

Jedna alternativa lokalnoj instalaciji Pythona je pokretanje koda u kontejneru. Budući da naš repozitorij isporučuje posebnu `.devcontainer` mapu koja opisuje kako izgraditi kontejner za ovaj repozitorij, VS Code nudi mogućnost ponovnog otvaranja koda u kontejneru. Ovo zahtijeva instalaciju Dockera i može biti složenije, pa to preporučujemo iskusnijim korisnicima.

## Pokretanje u oblaku

Ako ne želite instalirati Python lokalno i imate pristup nekim oblačnim resursima - dobra alternativa je pokrenuti kod u oblaku. Postoji nekoliko načina kako to možete učiniti:

* Korištenje **[GitHub Codespaces](https://github.com/features/codespaces)**, što je virtualno okruženje stvoreno za vas na GitHubu, dostupno kroz VS Code sučelje u pregledniku. Ako imate pristup Codespaces, jednostavno kliknite na gumb **Code** u repozitoriju, pokrenite codespace i brzo započnite.
* Korištenje **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) nudi besplatne računalne resurse u oblaku kako biste mogli isprobati neki kod s GitHuba. Na početnoj stranici postoji gumb za otvaranje repozitorija u Binderu - to bi vas brzo trebalo odvesti na stranicu bindera, koja će izgraditi osnovni kontejner i besprijekorno pokrenuti Jupyter web sučelje za vas.

> **Napomena**: Kako bi spriječio zloupotrebu, Binder ima blokiran pristup nekim web resursima. To može spriječiti rad nekog koda koji dohvaća modele i/ili skupove podataka s javnog Interneta. Možda ćete morati pronaći neka zaobilazna rješenja. Također, računarski resursi koje pruža Binder su prilično osnovni, pa će treniranje biti sporo, osobito u kasnijim, složenijim lekcijama.

## Pokretanje u oblaku s GPU-om

Neke od kasnijih lekcija u ovom kurikulumu puno bi profitirale od podrške GPU-a. Na primjer, treniranje modela može biti izrazito sporo bez toga. Postoji nekoliko opcija koje možete slijediti, posebno ako imate pristup oblaku putem [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) ili preko svoje institucije:

* Kreirajte [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i povežite se na nju putem Jupytera. Možete zatim klonirati repozitorij direktno na stroj i početi učiti. NC-serija VM-ova podržava GPU.

> **Napomena**: Neke pretplate, uključujući Azure for Students, ne pružaju GPU podršku odmah. Možda ćete trebati zatražiti dodatne GPU jezgre putem tehničke podrške.

* Kreirajte [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) i zatim koristite Notebook značajku tamo. [Ovaj video](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje kako klonirati repozitorij u Azure ML notebook i početi ga koristiti.

Također možete koristiti Google Colab, koji nudi određenu besplatnu podršku za GPU, te tamo učitavati Jupyter Notebooks i izvršavati ih jedan po jedan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->