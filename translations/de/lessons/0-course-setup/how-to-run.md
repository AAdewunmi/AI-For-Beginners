# So führen Sie den Code aus

Dieser Lehrplan enthält viele ausführbare Beispiele und Labs, die Sie ausführen möchten. Um dies zu tun, benötigen Sie die Möglichkeit, Python-Code in Jupyter Notebooks auszuführen, die als Teil dieses Lehrplans bereitgestellt werden. Sie haben mehrere Möglichkeiten, den Code auszuführen:

## Lokal auf Ihrem Computer ausführen

Um den Code lokal auf Ihrem Computer auszuführen, ist eine Python-Installation erforderlich. Eine Empfehlung ist die Installation von **[miniconda](https://conda.io/en/latest/miniconda.html)** – es handelt sich um eine eher leichte Installation, die den Paketmanager `conda` für verschiedene Python-**virtuelle Umgebungen** unterstützt.

Nachdem Sie miniconda installiert haben, klonen Sie das Repository und erstellen eine virtuelle Umgebung, die für diesen Kurs verwendet wird:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code mit Python-Erweiterung verwenden

Dieser Lehrplan wird am besten verwendet, wenn Sie ihn in [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) öffnen.

> **Hinweis**: Sobald Sie das Verzeichnis klonen und in VS Code öffnen, wird automatisch vorgeschlagen, Python-Erweiterungen zu installieren. Sie müssen auch miniconda wie oben beschrieben installieren.

> **Hinweis**: Wenn VS Code Ihnen vorschlägt, das Repository in einem Container neu zu öffnen, sollten Sie dies ablehnen, um die lokale Python-Installation zu verwenden.

### Jupyter im Browser verwenden

Sie können auch eine Jupyter-Umgebung über den Browser auf Ihrem eigenen Computer nutzen. Sowohl klassisches Jupyter als auch JupyterHub bieten eine bequeme Entwicklungsumgebung mit Autovervollständigung, Codehervorhebung usw.

Um Jupyter lokal zu starten, wechseln Sie in das Verzeichnis des Kurses und führen aus:

```bash
jupyter notebook
```
oder
```bash
jupyterhub
```
Sie können dann zu einer der `.ipynb`-Dateien navigieren, sie öffnen und mit der Arbeit beginnen.

### Ausführen in einem Container

Eine Alternative zur Python-Installation wäre, den Code in einem Container auszuführen. Da unser Repository einen speziellen `.devcontainer`-Ordner bereitstellt, der beschreibt, wie ein Container für dieses Repo gebaut wird, bietet VS Code die Möglichkeit, den Code neu in einem Container zu öffnen. Dies erfordert eine Docker-Installation und ist auch komplexer, daher empfehlen wir dies eher erfahrenen Nutzern.

## Ausführen in der Cloud

Wenn Sie Python nicht lokal installieren möchten und Zugriff auf einige Cloud-Ressourcen haben – wäre eine gute Alternative, den Code in der Cloud auszuführen. Es gibt mehrere Möglichkeiten, dies zu tun:

* Verwendung von **[GitHub Codespaces](https://github.com/features/codespaces)**, einer virtuellen Umgebung, die für Sie auf GitHub erstellt wird, zugänglich über eine VS Code-Browseroberfläche. Wenn Sie Zugriff auf Codespaces haben, können Sie einfach auf die **Code**-Schaltfläche im Repo klicken, einen Codespace starten und sofort loslegen.
* Verwendung von **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) bietet kostenlose Rechenressourcen in der Cloud für Personen wie Sie, um Code auf GitHub auszuprobieren. Auf der Startseite gibt es eine Schaltfläche, um das Repository in Binder zu öffnen – dies führt Sie schnell zur Binder-Seite, die einen zugrundeliegenden Container erstellt und nahtlos eine Jupyter-Weboberfläche startet.

> **Hinweis**: Um Missbrauch zu verhindern, hat Binder den Zugriff auf einige Web-Ressourcen blockiert. Dies kann verhindern, dass einige Codeabschnitte funktionieren, die Modelle und/oder Datensätze aus dem öffentlichen Internet laden. Sie müssen möglicherweise einige Umgehungsmöglichkeiten finden. Außerdem sind die von Binder bereitgestellten Rechenressourcen recht einfach, daher ist das Training besonders in späteren, komplexeren Lektionen langsam.

## Ausführen in der Cloud mit GPU

Einige der späteren Lektionen in diesem Lehrplan würden sehr von GPU-Unterstützung profitieren. Model-Training kann zum Beispiel ohne diese schmerzhaft langsam sein. Es gibt einige Optionen, denen Sie folgen können, besonders wenn Sie über [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) oder Ihre Institution Zugang zur Cloud haben:

* Erstellen Sie eine [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) und verbinden Sie sich über Jupyter damit. Sie können dann das Repo direkt auf die Maschine klonen und mit dem Lernen beginnen. NC-Serie VMs verfügen über GPU-Unterstützung.

> **Hinweis**: Einige Abonnements, einschließlich Azure for Students, bieten nicht standardmäßig GPU-Unterstützung. Sie müssen möglicherweise zusätzliche GPU-Kerne über eine technische Supportanfrage anfordern.

* Erstellen Sie einen [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) und nutzen Sie dann dort die Notebook-Funktion. [Dieses Video](https://azure-for-academics.github.io/quickstart/azureml-papers/) zeigt, wie Sie ein Repository in ein Azure ML Notebook klonen und verwenden.

Sie können auch Google Colab verwenden, das einige kostenlose GPU-Unterstützung bietet, und Jupyter Notebooks dort hochladen, um sie nacheinander auszuführen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->