# 如何執行程式碼

本課程包含許多可執行的範例和實驗室，您會想要執行它們。為此，您需要能夠在此課程提供的 Jupyter 筆記本中執行 Python 程式碼。有幾種方式可以執行程式碼：

## 在您的電腦本地執行

若要在您的電腦本地執行程式碼，需要安裝 Python。建議安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)** — 這是一個輕量級安裝，支援使用 `conda` 套件管理器管理不同的 Python <strong>虛擬環境</strong>。

安裝 miniconda 後，複製本儲存庫並建立一個用於此課程的虛擬環境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用 Visual Studio Code 與 Python 擴充套件

此課程建議在 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 中搭配 [Python 擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) 來使用。

> <strong>注意</strong>：當您複製並打開目錄於 VS Code 時，它會自動建議您安裝 Python 擴充套件。您還需要依照上述說明安裝 miniconda。

> <strong>注意</strong>：若 VS Code 建議您在容器中重新打開儲存庫，您應拒絕這個選項以使用本地的 Python 安裝。

### 在瀏覽器中使用 Jupyter

您也可以在自己電腦的瀏覽器中使用 Jupyter 環境。無論是傳統 Jupyter 還是 JupyterHub，都提供方便的開發環境，具有自動完成、程式碼高亮等功能。

若要在本地啟動 Jupyter，請移至課程目錄並執行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
接著您即可瀏覽任何 `.ipynb` 檔案，打開並開始使用。

### 在容器中執行

另一種替代本地 Python 安裝的方法是使用容器執行程式碼。由於本儲存庫提供了一個特殊的 `.devcontainer` 資料夾，說明如何為此儲存庫建構容器，VS Code 提供了以容器重新打開程式碼的功能。這需要安裝 Docker，且操作較為複雜，因此我們建議具備經驗的使用者使用。

## 在雲端執行

如果您不想在本地安裝 Python，且有雲端資源可用，另一個很好的選擇是在雲端執行程式碼。您可以用以下幾種方法：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是在 GitHub 上為您建立的虛擬環境，可透過瀏覽器中的 VS Code 介面存取。如果您能使用 Codespaces，只需點擊儲存庫中的 **Code** 按鈕，啟動 codespace，即可立刻開始執行。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。 [Binder](https://mybinder.org) 提供免費的雲端運算資源，方便您測試 GitHub 上的程式碼。首頁有一個按鈕可直接在 Binder 中開啟儲存庫 — 它會快速帶您進入 Binder 網站，背後會建構容器並順利啟動 Jupyter 網頁介面。

> <strong>注意</strong>：因預防濫用，Binder 對某些網路資源設有限制，這可能導致部分需從公開網路下載模型或資料集的程式碼無法運作。您可能需要尋找替代方法。此外，Binder 提供的運算資源相當基本，訓練速度會很慢，尤其是後面較複雜的課程。

## 在有 GPU 的雲端執行

本課程後期的部分課程非常需要 GPU 支援。否則模型訓練可能非常緩慢。若您有雲端存取權限，特別是透過[Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)或您的機構，您可以參考以下幾種選項：

* 建立 [資料科學虛擬機器](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，並透過 Jupyter 連線。您可直接在該虛擬機器中複製儲存庫並開始學習。NC 系列虛擬機支援 GPU。

> <strong>注意</strong>：部分訂閱方案（包含 Azure for Students）預設不提供 GPU 支援。您可能需要提交技術支援請求以取得更多 GPU 核心。

* 建立 [Azure 機器學習工作區](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然後使用其內建的 Notebook 功能。[這段影片](https://azure-for-academics.github.io/quickstart/azureml-papers/)展示如何將儲存庫複製到 Azure ML Notebook 並開始使用。

您也可以使用 Google Colab，其提供部分免費的 GPU 支援，並在那裡上傳 Jupyter 筆記本逐一執行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->