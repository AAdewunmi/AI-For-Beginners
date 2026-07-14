# Kaip paleisti kodą

Šioje mokymo programoje yra daug vykdomų pavyzdžių ir laboratorinių darbų, kuriuos norėsite paleisti. Tam reikia galimybės vykdyti Python kodą Jupyter užrašuose, kurie pateikti kaip šios mokymo programos dalis. Turite keletą galimybių, kaip paleisti kodą:

## Vykdyti vietoje savo kompiuteryje

Norint paleisti kodą vietoje savo kompiuteryje, reikia turėti įdiegtą Python. Viena iš rekomendacijų – įdiegti **[miniconda](https://conda.io/en/latest/miniconda.html)** – tai pakankamai lengvas diegimas, kuris palaiko `conda` paketų tvarkyklę skirtingoms Python **virtualioms aplinkoms**.

Įdiegus miniconda, nuklonuokite saugyklą ir sukurkite virtualią aplinką, kuri bus naudojama šiame kurse:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Naudojant Visual Studio Code su Python papildiniu

Šią mokymo programą geriausia naudoti atidarant ją [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) su [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Pastaba**: Kai tik nuklonuosite ir atidarysite katalogą VS Code, jis automatiškai pasiūlys įdiegti Python papildinius. Taip pat turėsite įdiegti miniconda, kaip aprašyta aukščiau.

> **Pastaba**: Jei VS Code siūlo atidaryti saugyklą konteineryje, turėtumėte atsisakyti šio pasiūlymo, kad naudotumėte vietoje įdiegtą Python.

### Naudojant Jupyter naršyklėje

Taip pat galite naudoti Jupyter aplinką naršyklėje savo kompiuteryje. Tiek klasikinis Jupyter, tiek JupyterHub suteikia patogią vystymo aplinką su automatinio pildymo, kodo paryškinimo ir kitomis funkcijomis.

Norėdami paleisti Jupyter vietoje, eikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```
arba
```bash
jupyterhub
```
Tuomet galite naršyti bet kurį iš `.ipynb` failų, atidaryti juos ir pradėti darbą.

### Vykdymas konteineryje

Vienas iš Python diegimo alternatyvų yra paleisti kodą konteineryje. Kadangi mūsų saugykla turi specialų `.devcontainer` katalogą, kuris nurodo, kaip sukurti konteinerį šiai saugyklai, VS Code siūlo galimybę iš naujo atidaryti kodą konteineryje. Tam reikės įdiegti Docker, ir tai bus sudėtingiau, todėl rekomenduojame šį būdą labiau patyrusiems vartotojams.

## Vykdymas debesyje

Jei nenorite diegti Python vietoje ir turite prieigą prie kokių nors debesies išteklių – geras pasirinkimas būtų vykdyti kodą debesyje. Tai galite padaryti keliais būdais:

* Naudojant **[GitHub Codespaces](https://github.com/features/codespaces)**, tai yra virtuali aplinka, sukurta jums GitHub platformoje, pasiekiama per VS Code naršyklės sąsają. Jei turite prieigą prie Codespaces, tiesiog spauskite **Code** mygtuką saugykloje, pradėkite codespace ir pradėkite dirbti labai greitai.
* Naudojant **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) suteikia nemokamus skaičiavimo išteklius debesyje žmonėms, norintiems išbandyti kodą GitHub platformoje. Pagrindiniame puslapyje yra mygtukas atidaryti saugyklą Binder – tai greitai nukels jus į Binder svetainę, kuri sukuria konteinerį ir sklandžiai paleidžia Jupyter interneto sąsają.

> **Pastaba**: Norint išvengti piktnaudžiavimo, Binder blokuoja prieigą prie kai kurių internetinių šaltinių. Tai gali neleisti veikti kai kuriems kodo fragmentams, kurie naudoja modelius ir (arba) duomenų rinkinius iš interneto. Gali prireikti rasti sprendimų. Taip pat Binder skirti skaičiavimo ištekliai yra gana pagrindiniai, todėl treniruotės bus lėtos, ypač vėlesnėse, sudėtingesnėse pamokose.

## Vykdymas debesyje su GPU

Kai kurios vėlesnės šios mokymo programos pamokos labai naudotųsi GPU palaikymu. Modelių mokymas, pavyzdžiui, kitu atveju gali būti labai lėtas. Yra keletas variantų, kuriuos galite pasirinkti, ypač jei turite prieigą prie debesies per [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) arba per savo instituciją:

* Sukurkite [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ir prisijunkite prie jos per Jupyter. Galite tiesiog nuklonuoti saugyklą tiesiai į šį kompiuterį ir pradėti mokytis. NC serijos VM turi GPU palaikymą.

> **Pastaba**: Kai kurios prenumeratos, įskaitant Azure for Students, pagal nutylėjimą neteikia GPU palaikymo. Gali prireikti pateikti užklausą techninės pagalbos skyriui dėl papildomų GPU branduolių.

* Sukurkite [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), o tada naudokite ten esančią Notebook funkciją. [Šis video](https://azure-for-academics.github.io/quickstart/azureml-papers/) parodo, kaip nuklonuoti saugyklą į Azure ML užrašinį ir pradėti jį naudoti.

Taip pat galite naudoti Google Colab, kuris suteikia nemokamą GPU palaikymą, ir įkelti Jupyter užrašus ten, kad paleistumėte juos po vieną.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->