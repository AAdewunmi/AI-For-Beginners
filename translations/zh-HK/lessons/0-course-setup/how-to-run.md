# 如何執行代碼

本課程包含許多可執行的範例和實驗室，您會想要運行它們。要做到這一點，您需要能夠在本課程附帶的 Jupyter 筆記本中執行 Python 代碼。您有幾種運行代碼的選項：

## 在您的電腦本地運行

為了在您的電腦本地運行代碼，需要安裝 Python。建議安裝 **[miniconda](https://conda.io/en/latest/miniconda.html)** —— 它是一個相當輕量的安裝包，支援使用 `conda` 套件管理器來管理不同的 Python <strong>虛擬環境</strong>。

安裝 miniconda 後，請克隆此倉庫並創建一個該課程使用的虛擬環境：

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### 使用 Visual Studio Code 搭配 Python 擴展

本課程最佳使用方式是打開 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) 並安裝 [Python 擴展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)。

> <strong>注意</strong>: 當您克隆並在 VS Code 打開目錄時，它會自動建議您安裝 Python 擴展。您還需要依照上述說明安裝 miniconda。

> <strong>注意</strong>: 如果 VS Code 提示您重新在容器中打開該倉庫，您應該拒絕此提議，以便使用本地的 Python 安裝。

### 在瀏覽器中使用 Jupyter

您也可以在自己電腦的瀏覽器中使用 Jupyter 環境。無論是經典 Jupyter 還是 JupyterHub，都提供了方便的開發環境，擁有自動完成功能、代碼高亮等。

若要在本地啟動 Jupyter，請進入課程目錄並執行：

```bash
jupyter notebook
```
或
```bash
jupyterhub
```
然後您可以導航至任何 `.ipynb` 文件，打開並開始使用。

### 容器中運行

不安裝 Python 的另一個方案是將代碼在容器中運行。由於本倉庫提供了一個特殊的 `.devcontainer` 資料夾，指示如何為此倉庫構建容器，VS Code 可提供重新在容器中打開代碼的機會。這需要安裝 Docker，且操作較複雜，我們建議較有經驗的使用者使用。

## 在雲端運行

如果您不想在本地安裝 Python，且能使用某些雲端資源，一個很好的替代方案是將代碼放到雲端運行。您可以用以下幾種方式：

* 使用 **[GitHub Codespaces](https://github.com/features/codespaces)**，這是一個在 GitHub 上為您創建的虛擬環境，通過 VS Code 的瀏覽器界面存取。只要您能使用 Codespaces，點擊倉庫中的 **Code** 按鈕，啟動一個 codespace，即可迅速開始工作。
* 使用 **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**。[Binder](https://mybinder.org) 為像您這樣的用戶免費提供雲端計算資源，可讓您測試 GitHub 上的部分代碼。首頁有按鈕可在 Binder 中打開此倉庫 —— 它會迅速帶您進入 Binder 網站，該網站會構建底層容器並無縫啟動 Jupyter 網頁介面。

> <strong>注意</strong>: 為防止濫用，Binder 對部分網路資源設有限制。這可能導致某些代碼無法正常執行（尤其是從公開網路下載模型和/或數據集時）。您可能需要尋找替代方案。此外，Binder 提供的計算資源較為基礎，因此訓練過程會較慢，特別是在後期較複雜的課程中。

## 在雲端使用 GPU 運行

本課程後期的部分課程將大大受惠於 GPU 支持。例如模型訓練，若無 GPU 輔助會非常緩慢。有幾種選項特別適合擁有雲端資源的用戶，例如通過 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) 或透過您的學術機構：

* 建立 [資料科學虛擬機器](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)，並透過 Jupyter 連線到該機器，然後您可以直接在該機器克隆倉庫開始學習。NC 系列虛擬機器支援 GPU。

> <strong>注意</strong>: 某些訂閱（包括 Azure for Students）預設不提供 GPU 支持。您可能需要透過技術支援申請額外的 GPU 核心。

* 建立 [Azure 機器學習工作區](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)，然後使用筆記本功能。此 [影片](https://azure-for-academics.github.io/quickstart/azureml-papers/) 示範如何在 Azure ML 筆記本中克隆倉庫並開始使用。

您也可以使用 Google Colab，它提供部分免費 GPU 支持，並上傳 Jupyter 筆記本逐個執行。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->