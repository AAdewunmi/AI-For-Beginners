# Jinsi ya Kuendesha Msimbo

Mtaala huu una mifano mingi inayoweza kutekelezwa na maabara ambazo ungependa kuendesha. Ili kufanya hivyo, unahitaji uwezo wa kutekeleza msimbo wa Python katika Jupyter Notebooks zinazotolewa kama sehemu ya mtaala huu. Una chaguzi kadhaa za kuendesha msimbo:

## Endesha kwa ndani kwenye kompyuta yako

Ili kuendesha msimbo kwa ndani kwenye kompyuta yako, unahitaji kuwa na usakinishaji wa Python. Moja ya mapendekezo ni kusakinisha **[miniconda](https://conda.io/en/latest/miniconda.html)** - ni usakinishaji mwepesi unaounga mkono meneja wa vifurushi `conda` kwa mazingira mbalimbali ya Python **virtual environments**.

Baada ya kusakinisha miniconda, nakili (clone) hifadhidata na unda mazingira ya virtual yatakayotumika kwa kozi hii:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Kutumia Visual Studio Code na Virutubisho vya Python

Mtaala huu unatumika vizuri zaidi unapoufungua katika [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ukiwa na [Virutubisho vya Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Kumbuka**: Mara baada ya kunakili na kufungua saraka katika VS Code, itapendekeza moja kwa moja kusakinisha virutubisho vya Python. Pia utahitaji kusakinisha miniconda kama ilivyoelezwa hapo juu.

> **Kumbuka**: Ikiwa VS Code itakupendekeza kufungua hifadhidata upya ndani ya kontena, unapaswa kukataa hii ili kutumia usakinishaji wa Python kwa ndani. 

### Kutumia Jupyter katika Kivinjari

Unaweza pia kutumia mazingira ya Jupyter kutoka kivinjari kwenye kompyuta yako mwenyewe. Jupyter wa kawaida na JupyterHub zote zinatoa mazingira mazuri ya maendeleo yenye utimilifu wa nira (auto-completion), muonekano wa msimbo, n.k.

Ili kuanza Jupyter kwa ndani, nenda kwenye saraka ya kozi, na tekeleza:

```bash
jupyter notebook
```
au
```bash
jupyterhub
```
Kisha unaweza kuvinjari faili yoyote ya `.ipynb`, ufungue na kuanza kufanya kazi.

### Kuendesha katika kontena

Njia mbadala ya usakinishaji wa Python ni kuendesha msimbo katika kontena. Kwa kuwa hifadhidata yetu ina jalada maalum `.devcontainer` linaloelekeza jinsi ya kujenga kontena kwa ajili ya repository hii, VS Code inatoa fursa ya kufungua upya msimbo ndani ya kontena. Hii itahitaji usakinishaji wa Docker, na pia itakuwa ngumu zaidi, kwa hiyo tunapendekeza hii kwa watumiaji wenye uzoefu zaidi.

## Kuendesha kwenye Wingu

Ikiwa hutaki kusakinisha Python kwa ndani, na una upatikanaji wa rasilimali za wingu - njia nzuri ni kuendesha msimbo kwenye wingu. Kuna njia kadhaa unazoweza kutumia kufanya hivi:

* Kutumia **[GitHub Codespaces](https://github.com/features/codespaces)**, ambayo ni mazingira halisi yaliyoundwa kwa ajili yako kwenye GitHub, yanayopatikana kupitia kiolesura cha kivinjari cha VS Code. Ikiwa una upatikanaji wa Codespaces, unaweza kubofya tu kitufe cha **Code** katika repo, anza codespace, na uanze kuendesha mara moja.
* Kutumia **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) hutoa rasilimali za kompyuta bure zinazotolewa kwenye wingu kwa watu kama wewe kujaribu msimbo wa GitHub. Kuna kitufe kwenye ukurasa wa mwanzo cha kufungua repository kwenye Binder - hii itakupeleka haraka kwenye tovuti ya binder, ambayo itajenga kontena la msingi na kuanzisha kiolesura cha wavuti cha Jupyter kwako kwa urahisi.

> **Kumbuka**: Ili kuzuia matumizi mabaya, Binder ina upatikanaji wa baadhi ya rasilimali za wavuti zilizozuiwa. Hii inaweza kuzuia baadhi ya misimbo kufanya kazi, ambayo hupakua mifano na/au seti za data kutoka kwenye mtandao wa umma. Huenda utahitaji kutafuta mbinu mbadala. Pia, rasilimali za kompyuta zinazotolewa na Binder ni za kawaida tu, kwa hiyo mafunzo yatakuwa polepole, hasa katika mafunzo ya baadaye, magumu zaidi.

## Kuendesha kwenye Wingu kwa GPU

Baadhi ya masomo ya baadaye katika mtaala huu yangefaidika sana na msaada wa GPU. Mafunzo ya mifano, kwa mfano, yanaweza kuwa polepole sana vinginevyo. Kuna chaguzi kadhaa unazoweza kufuata, hasa ikiwa una upatikanaji wa wingu kupitia [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), au kupitia taasisi yako:

* Unda [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) na uunganishe kupitia Jupyter. Kisha unaweza kunakili repo moja kwa moja kwenye mashine, na kuanza kujifunza. VMs za NC-series zina msaada wa GPU.

> **Kumbuka**: Baadhi ya usajili, ikiwemo Azure for Students, haipati msaada wa GPU moja kwa moja. Huenda utahitaji kuomba cores za ziada za GPU kupitia ombi la msaada wa kiufundi.

* Unda [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) na kisha tumia kipengele cha Notebook hapo. [Video hii](https://azure-for-academics.github.io/quickstart/azureml-papers/) inaonyesha jinsi ya kunakili repository ndani ya Azure ML notebook na kuanza kuitumia.

Unaweza pia kutumia Google Colab, ambayo huja na msaada wa GPU bure, na kupakia Jupyter Notebooks huko ili kuzitekeleza mmoja mmoja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->