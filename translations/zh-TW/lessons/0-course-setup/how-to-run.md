# 如何執行程式碼

本課程包含許多可執行的範例和實驗，您可能想要執行它們。要做到這一點，您需要能夠在本課程提供的 Jupyter 筆記本中執行 Python 程式碼。您有幾種選擇來運行程式碼：

## 在您的電腦上本地執行

若要在您的電腦上本地執行程式碼，您需要安裝 Python。其中一個建議是安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)** ——這是一個相當輕量的安裝，它支援使用 `conda` 套件管理器來管理不同的 Python <strong>虛擬環境</strong>。

安裝 miniconda 後，克隆本儲存庫並建立一個用於本課程的虛擬環境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用帶有 Python 擴充功能的 Visual Studio Code

本課程在使用 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 與 [Python 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 開啟時效果最佳。

> <strong>注意</strong>：當您克隆並在 VS Code 中開啟此目錄後，它會自動建議您安裝 Python 擴充功能。您也必須依上述方式安裝 miniconda。

> <strong>注意</strong>：若 VS Code 建議您在容器中重新開啟儲存庫，您應該拒絕此建議以使用本地 Python 安裝。

### 在瀏覽器中使用 Jupyter

您也可以在自己電腦的瀏覽器中使用 Jupyter 環境。傳統 Jupyter 以及 JupyterHub 都提供了方便的開發環境，包含自動補全、程式碼高亮等功能。

若要在本地啟動 Jupyter，請前往課程目錄並執行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
您即可導航至任一 `.ipynb` 檔案，打開並開始使用。

### 在容器中運行

另一種替代 Python 安裝的方法是使用容器。由於我們的儲存庫包含一個特殊的 `.devcontainer` 資料夾，用來指示如何為此儲存庫建立容器，VS Code 提供了重新在容器中開啟程式碼的功能。這需要安裝 Docker，並且較為複雜，因此建議較有經驗的使用者使用此方法。

## 在雲端運行

如果您不想在本地安裝 Python，且可以使用一些雲端資源，一個不錯的替代方案是將程式碼運行在雲端。有幾種方法：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是一個由 GitHub 為您建立的虛擬環境，可以透過 VS Code 瀏覽器介面存取。如果您可以使用 Codespaces，只需在儲存庫中點擊 **Code** 按鈕，啟動 Codespace，即可快速開始。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。 [Binder](https://mybinder.org) 提供免費的雲端運算資源，讓您能在 GitHub 上測試程式碼。首頁有個按鈕可以在 Binder 中開啟此儲存庫——它將快速帶您到 binder 網站，該網站會建立基礎容器並無縫啟動 Jupyter 網頁介面。

> <strong>注意</strong>：為避免誤用，Binder 阻擋了部分網路資源的存取。這會導致部分從公共網路下載模型和/或資料集的程式碼無法正常運作。您可能需要找一些變通方法。此外，Binder 提供的運算資源相當基礎，因此訓練會很慢，尤其在較複雜的後期課程中更是如此。

## 使用 GPU 在雲端運行

本課程後期的部分課程非常需要 GPU 支援。例如模型訓練，否則將非常緩慢。您可以採用以下幾種方案，尤其是若您透過 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或您就讀的機構有雲端權限：

* 建立 [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，並透過 Jupyter 連線。您可以在該機器上直接克隆儲存庫，並開始學習。NC 系列虛擬機器支援 GPU。

> <strong>注意</strong>：某些訂閱，包括 Azure for Students，預設不提供 GPU 支援。您可能需要透過技術支援請求額外申請 GPU 核心。

* 建立 [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然後使用其中的 Notebook 功能。[這段影片](https://azure-for-academics.github.io/quickstart/azureml-papers/) 示範如何將儲存庫克隆到 Azure ML notebook 並開始使用。

您也可以使用 Google Colab，它提供一些免費的 GPU 支援，且能逐一上傳與執行 Jupyter 筆記本。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->