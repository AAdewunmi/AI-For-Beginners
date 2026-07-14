# Hogyan futtassuk a kódot

Ez a tanterv sok futtatható példát és laboratóriumi gyakorlatot tartalmaz, amelyeket szeretnél futtatni. Ehhez szükséged van arra, hogy képes legyél Python kódot futtatni a tananyag részeként biztosított Jupyter Notebook-okban. Több lehetőséged is van a kód futtatására:

## Lokális futtatás a számítógépeden

A kód futtatásához lokálisan Python telepítés szükséges. Egy ajánlott megoldás a **[miniconda](https://conda.io/en/latest/miniconda.html)** telepítése – ez egy viszonylag könnyű telepítés, ami támogatja a `conda` csomagkezelőt különböző Python **virtuális környezetek** kezeléséhez.

Miután telepítetted a minicondát, klónozd a tárolót és hozz létre egy virtuális környezetet, amit a kurzus során fogsz használni:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code használata Python bővítménnyel

A tananyagot legjobban úgy használhatod, ha [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)-ban nyitod meg a projekttárat, a [Python bővítmény](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) telepítésével.

> **Megjegyzés**: Amint klónozod és megnyitod a könyvtárat VS Code-ban, automatikusan javasolni fogja a Python bővítmények telepítését. Emellett telepítened kell a minicondát, ahogy azt fent leírtuk.

> **Megjegyzés**: Ha VS Code azt javasolja, hogy nyisd meg újra a tárolót egy konténerben, akkor ezt utasítsd el, hogy a lokális Python telepítést használd.

### Jupyter futtatása böngészőben

Használhatsz Jupytert is a böngészőben a saját számítógépeden. Mind az alap Jupyter, mind a JupyterHub kényelmes fejlesztői környezetet biztosít automatikus kiegészítéssel, kódkijelöléssel stb.

A helyi Jupyter indításához lépj a kurzus könyvtárába, és futtasd:

```bash
jupyter notebook
```
vagy
```bash
jupyterhub
```
Ezután bármely `.ipynb` fájlra navigálhatsz, megnyithatod és elkezdhetsz dolgozni.

### Konténerben való futtatás

Egy alternatíva a Python telepítés helyett, ha a kódot konténerben futtatod. Mivel a tárolónk tartalmaz egy speciális `.devcontainer` mappát, ami leírja, hogyan építhető fel a konténer, a VS Code kínál lehetőséget a kód konténerben való újranyitására. Ehhez Docker telepítés szükséges, és technikailag bonyolultabb, így ezt tapasztaltabb felhasználóknak ajánljuk.

## Futtatás a felhőben

Ha nem szeretnél helyileg Python-t telepíteni, és vannak felhő erőforrásaid, jó alternatíva a kód futtatása a felhőben. Több módja van ennek:

* Használhatod a **[GitHub Codespaces](https://github.com/features/codespaces)** szolgáltatást, amely egy virtuális környezet, amit a GitHub hoz létre számodra, és amit egy VS Code böngésző felületén keresztül érhetsz el. Ha hozzáférsz a Codespaces-hez, csak kattints a **Code** gombra a tárolóban, indíts el egy codespace-et, és máris futtathatod a kódot.
* Használhatod a **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** szolgáltatást is. A [Binder](https://mybinder.org) ingyenes felhő alapú számítási erőforrásokat biztosít, hogy GitHub kódokat kipróbálhass. Az oldal kezdőlapján van gomb a tároló megnyitására Binder-ben – ez gyorsan átvezet a binder oldalra, amely felépít egy mögöttes konténert és zökkenőmentesen elindít egy Jupyter webes felületet.

> **Megjegyzés**: A Binder biztonsági okokból bizonyos webes forrásokhoz nem enged hozzáférést. Ez megakadályozhatja, hogy néhány kód működjön, amely modelleket és/vagy adatállományokat tölt le a nyilvános internetről. Lehet, hogy kerülő megoldásokat kell találnod. Emellett a Binder által biztosított számítási erőforrások meglehetősen alap szintűek, így az edzések lassúak lesznek, különösen a későbbi, összetettebb leckékben.

## Futtatás a felhőben GPU-val

A tananyag későbbi leckéi nagyban profitálnak a GPU támogatásból. Például a modell edzés máskülönben nagyon lassú lehet. Több lehetőséged is van, különösen ha van hozzáférésed a felhőhöz a [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) vagy az intézményed révén:

* Hozz létre [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)-t, és csatlakozz hozzá Jupyteren keresztül. Ekkor közvetlenül a gépre klónozhatod a tárolót és elkezdheted a tanulást. Az NC-sorozatú VM-ek támogatják a GPU-t.

> **Megjegyzés**: Egyes előfizetések, így az Azure for Students sem biztosít alapból GPU támogatást. Elképzelhető, hogy technikai támogatási kéréssel kell további GPU magokat igényelned.

* Hozz létre egy [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)-et, és használd ott a Notebook funkciót. [Ez a videó](https://azure-for-academics.github.io/quickstart/azureml-papers/) bemutatja, hogyan lehet egy tárolót Azure ML notebook-ba klónozni és használni.

Használhatod a Google Colabot is, amely bizonyos ingyenes GPU támogatással rendelkezik, és egyesével töltheted fel és futtathatod benne a Jupyter Notebook-okat.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->