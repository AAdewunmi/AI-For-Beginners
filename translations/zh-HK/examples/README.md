# 適合初學者的 AI 範例

歡迎！此目錄包含簡單的獨立範例，幫助你入門 AI 和機器學習。每個範例均設計為適合初學者，並附有詳細的註解和逐步說明。

## 📚 範例總覽

| 範例 | 說明 | 難度 | 預備知識 |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | 你的第一個 AI 程式 - 簡單的模式識別 | ⭐ 初學者 | Python 基礎 |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | 從零建立神經網絡 | ⭐⭐ 初學者+ | Python、基礎數學 |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | 利用預訓練模型分類影像 | ⭐⭐ 初學者+ | Python、numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | 分析文本情緒（正面／負面） | ⭐⭐ 初學者+ | Python |

## 🚀 開始使用

### 預備條件

請確保已安裝 Python（建議 3.8 以上）。安裝所需套件：

```bash
# 適用於 Python 腳本
pip install numpy

# 適用於 Jupyter 筆記本（圖像分類器）
pip install jupyter numpy pillow tensorflow
```

或使用主要課程中的 conda 環境：

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 執行範例

**對於 Python 腳本（.py 檔案）：**
```bash
python 01-hello-ai-world.py
```

**對於 Jupyter 筆記本（.ipynb 檔案）：**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 學習路線

建議依序完成以下範例：

1. **從「Hello AI World」開始** - 學習模式識別基礎
2. <strong>建立簡單神經網絡</strong> - 了解神經網絡運作方式
3. <strong>嘗試影像分類器</strong> - 見識 AI 實際應用於真實影像
4. <strong>分析文本情緒</strong> - 探索自然語言處理

## 💡 初學者小提示

- <strong>仔細閱讀程式註解</strong> - 這些會說明每行程式碼的作用
- **多做實驗！** - 嘗試更改數值，觀察結果變化
- <strong>不用擔心一下子全部都懂</strong> - 學習需要時間
- <strong>勇於提問</strong> - 使用 [討論區](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 後續步驟

完成這些範例後，可探索完整課程：
- [AI 簡介](../lessons/1-Intro/README.md)
- [神經網絡](../lessons/3-NeuralNetworks/README.md)
- [電腦視覺](../lessons/4-ComputerVision/README.md)
- [自然語言處理](../lessons/5-NLP/README.md)

## 🤝 貢獻

覺得這些範例有幫助嗎？歡迎幫助我們改進：
- 回報問題或建議改進
- 新增更多適合初學者的範例
- 改善文件與註解

---

*記住：每位專家都曾是初學者。祝你學習愉快！🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->