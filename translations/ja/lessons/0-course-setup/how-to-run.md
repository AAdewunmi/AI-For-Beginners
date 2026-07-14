# コードの実行方法

このカリキュラムには、多くの実行可能な例やラボが含まれており、それらを実行したくなるでしょう。これを行うには、このカリキュラムの一部として提供されるJupyterノートブック内でPythonコードを実行する能力が必要です。コードを実行するためのいくつかの選択肢があります：

## コンピューター上でローカルに実行する

コンピューター上でコードをローカルに実行するには、Pythonのインストールが必要です。おすすめの一つは **[miniconda](https://conda.io/en/latest/miniconda.html)** のインストールです。これは比較的軽量なインストールで、さまざまなPythonの<strong>仮想環境</strong>用に `conda` パッケージマネージャーをサポートします。

minicondaをインストールした後、リポジトリをクローンし、このコースで使用する仮想環境を作成します：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python拡張機能付きVisual Studio Codeの使用

このカリキュラムは、[Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) と [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) を使って開くと最も効果的に利用できます。

> <strong>注意</strong>: リポジトリをクローンしVS Codeでディレクトリを開くと、自動的にPython拡張機能のインストールを提案されます。また、上記のようにminicondaのインストールも必要です。

> <strong>注意</strong>: VS Codeがリポジトリをコンテナ内で再オープンすることを提案した場合は、ローカルのPythonインストールを使うためにこれを拒否してください。

### ブラウザでJupyterを使う

自分のコンピューター上のブラウザからJupyter環境を使うこともできます。古典的なJupyterもJupyterHubも、オートコンプリートやコードハイライトなど便利な開発環境を提供します。

ローカルでJupyterを開始するには、コースのディレクトリに移動し、以下を実行します：

```bash
jupyter notebook
```
または
```bash
jupyterhub
```
その後、任意の `.ipynb` ファイルに移動し、開いて作業を始めることができます。

### コンテナ内での実行

Pythonのインストールの代替として、コンテナ内でコードを実行する方法があります。当リポジトリはこのリポジトリ用のコンテナのビルド方法を指示する特別な `.devcontainer` フォルダーを提供しているため、VS Codeはコードをコンテナ内で再オープンする機能を提供しています。これにはDockerのインストールが必要で、より複雑になるため、より経験豊富なユーザーに推奨します。

## クラウドでの実行

ローカルにPythonをインストールしたくなく、クラウドリソースにアクセスできる場合は、クラウド上でコードを実行するのも良い選択肢です。いくつかの方法があります：

* **[GitHub Codespaces](https://github.com/features/codespaces)** を使用する。これはGitHub上に作成され、VS Codeのブラウザインターフェースからアクセス可能な仮想環境です。Codespacesにアクセスできる場合は、リポジトリの<strong>Code</strong>ボタンをクリックしてCodespaceを開始し、すぐに作業を始められます。
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** を使用する。[Binder](https://mybinder.org) は、GitHub上のコードをテストするために無料のクラウド計算資源を提供します。リポジトリのフロントページにあるボタンでBinder内にリポジトリを開けます。これにより基盤となるコンテナが構築され、Jupyterウェブインターフェースがシームレスに開始されます。

> <strong>注意</strong>: 悪用防止のため、Binderは一部のウェブリソースへのアクセスを制限しています。これにより、モデルやデータセットをパブリックインターネットから取得するコードの一部が動作しない可能性があります。回避策を見つける必要があるかもしれません。また、Binderの計算資源は非常に基本的なものなので、特に後半のより複雑なレッスンでのトレーニングは遅くなります。

## GPU付きクラウドでの実行

このカリキュラムの後半のいくつかのレッスンでは、GPUサポートがあると非常に有利です。例えば、モデルのトレーニングはそうでなければ非常に遅くなります。特に、[Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) や所属機関を通じてクラウドにアクセスできる場合には、以下の選択肢があります：

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) を作成し、Jupyter経由で接続します。リポジトリをそのままマシンにクローンし、学習を開始できます。NCシリーズのVMはGPUをサポートしています。

> <strong>注意</strong>: Azure for Studentsを含む一部のサブスクリプションでは、GPUサポートが標準で提供されていません。技術サポートリクエストで追加のGPUコアを申請する必要がある場合があります。

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) を作成し、そこでノートブック機能を使用します。[この動画](https://azure-for-academics.github.io/quickstart/azureml-papers/) は、Azure MLノートブックにリポジトリをクローンし、使用を開始する方法を示しています。

また、Google Colabを使うこともできます。これは無料のGPUサポートが含まれており、Jupyterノートブックを1つずつアップロードして実行できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->