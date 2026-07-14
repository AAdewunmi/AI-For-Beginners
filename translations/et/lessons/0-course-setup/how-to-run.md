# Kuidas koodi käivitada

See õppekava sisaldab palju käivitatavaid näiteid ja laboreid, mida soovite käivitada. Selleks peate suutma käivitada Python-koodi Jupyter Notebook'ides, mis on selle õppekava osana saadaval. Koodi käivitamiseks on teil mitu võimalust:

## Käivitage lokaalselt oma arvutis

Koodi käivitamiseks lokaalselt oma arvutis on vaja Python'i installatsiooni. Soovitame installida **[miniconda](https://conda.io/en/latest/miniconda.html)** – see on suhteliselt kerge installatsioon, mis toetab `conda` pakihaldurit erinevate Python'i **virtuaalsete keskkondade** jaoks.

Pärast miniconda installimist kloonige hoidla ja looge selle kursuse jaoks kasutatav virtuaalne keskkond:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code kasutamine Python'i laiendusega

Seda õppekava on kõige parem kasutada avades seda [Visual Studio Code'is](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) koos [Python'i laiendusega](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Märkus**: Kui olete hoidla klooninud ja avanud kataloogi VS Code'is, soovitatakse teil automaatselt Python'i laiendusi installida. Samuti peate installima miniconda vastavalt ülaltoodule.

> **Märkus**: Kui VS Code soovitab teil hoidla konteineris uuesti avada, peaksite selle pakkumise tagasi lükkama, et kasutada kohalikku Python'i installatsiooni.

### Jupyter'i kasutamine brauseris

Samuti saate kasutada Jupyter'i keskkonda oma arvuti brauseris. Nii klassikaline Jupyter kui ka JupyterHub pakuvad mugavat arendusvõimalust koos automaattäienduse, koodivärvimise jm-ga.

Jupyter'i kohalikuks käivitamiseks minge kursuse kataloogi ja käivitage:

```bash
jupyter notebook
```
või
```bash
jupyterhub
```
Seejärel saate navigeerida ükskõik millise `.ipynb` faili juurde, avada selle ja alustada tööd.

### Käivitamine konteineris

Üks alternatiiv Python'i installatsioonile on koodi käivitamine konteineris. Kuna meie hoidla sisaldab spetsiaalset `.devcontainer` kausta, mis juhendab konteineri ehitamist selle hoidla jaoks, pakub VS Code võimalust koodi konteineris uuesti avada. Selleks on vaja Docker'i installatsiooni ja see on keerukam, seega soovitame seda rohkem kogenud kasutajatele.

## Pilves käivitamine

Kui te ei soovi Python'i kohapeal installida ja teil on ligipääs mõnele pilveressursile, siis hea alternatiiv on koodi käivitamine pilves. Selleks on mitmeid võimalusi:

* Kasutades **[GitHub Codespaces](https://github.com/features/codespaces)**, mis on teie jaoks GitHubis loodud virtuaalne keskkond, mida pääseb ligi VS Code'i brauseriliidese kaudu. Kui teil on Codespaces'i ligipääs, saate lihtsalt vajutada hoidla **Code** nuppu, käivitada codespace'i ja hakata kohe kasutama.
* Kasutades **[Binderit](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) pakub pilves tasuta arvutusressursse, et saaksite GitHubis olevat koodi testida. Esilehel on nupp, mille abil saate hoidla Binderisse avada – see viib teid kiiresti Binder'i saidile, mis ehitab aluseks oleva konteineri ja käivitab probleemideta Jupyter'i veebiliidese.

> **Märkus**: Kuritarvituste vältimiseks on Bindril juurdepääs mõnedele veebivahenditele piiratud. See võib takistada mõnda koodi töötamist, mis laadib mudeleid ja/või andmekogumeid avalikust internetist. Võib tekkida vajadus otsida lahendusi. Samuti on Binderi pakutavad arvutusressursid üsna piiratud, seega võib treenimine olla aeglane, eriti hilisemates, keerukamates tundides.

## Pilves käivitamine GPU-ga

Mõned hilisemad selle õppekava tunnid võtaksid GPU toe suurepäraselt vastu. Mudelite treenimine võib muidu olla valusalt aeglane. On mitu võimalust, mida võite kasutada, eriti kui teil on juurdepääs pilvele kas [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) kaudu või oma asutuse kaudu:

* Looge [Data Science virtuaalmasin](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja ühenduge sellega Jupyteri kaudu. Siis saate kloonida hoidla otse masinale ja alustada õppimist. NC-seeria VM-id toetavad GPU-d.

> **Märkus**: Mõned tellimused, sh Azure for Students, ei paku GPU-tuge automaatselt. Võib vaja minna tehnilise toe taotlust täiendavate GPU südamike saamiseks.

* Looge [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja seejärel kasutage seal Notebook'i funktsiooni. [See video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näitab, kuidas kloonida hoidla Azure ML noteboodi ja hakata seda kasutama.

Võite kasutada ka Google Colabit, mis pakub teatud tasuta GPU tuge, ja laadida sinna üles Jupyter Notebook'e, et neid ükshaaval käivitada.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->