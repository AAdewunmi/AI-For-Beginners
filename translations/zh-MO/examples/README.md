# 初學者友好的 AI 範例

歡迎！本目錄包含簡單、獨立的範例，幫助您入門 AI 和機器學習。每個範例都設計得適合初學者，附有詳細註解和逐步解釋。

## 📚 範例總覽

| 範例 | 說明 | 難度 | 前置條件 |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | 您的第一個 AI 程式 - 簡單的模式識別 | ⭐ 初學者 | Python 基礎 |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | 從零開始建立神經網絡 | ⭐⭐ 初階初學者+ | Python、基礎數學 |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | 用預先訓練模型分類圖像 | ⭐⭐ 初階初學者+ | Python、numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | 分析文字情緒（正面/負面） | ⭐⭐ 初階初學者+ | Python |

## 🚀 開始使用

### 前置條件

確保您已安裝 Python（建議 3.8 或以上版本）。安裝所需套件：

```bash
# 適用於 Python 腳本
pip install numpy

# 適用於 Jupyter 筆記本（圖像分類器）
pip install jupyter numpy pillow tensorflow
```

或使用主課程的 conda 環境：

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

## 📖 學習路徑

建議按順序跟進範例：

1. **從「Hello AI World」開始** - 學習模式識別基礎
2. <strong>建立簡單神經網絡</strong> - 理解神經網絡運作方式
3. <strong>嘗試圖像分類器</strong> - 見識 AI 的真實應用
4. <strong>分析文字情緒</strong> - 探索自然語言處理

## 💡 初學者小貼士

- <strong>仔細閱讀程式註解</strong> - 它們說明每行程式碼的作用
- **多做實驗！** - 嘗試改變數值，看看結果如何
- <strong>不用擔心一次就懂</strong> - 學習需要時間
- <strong>提出問題</strong> - 使用 [討論板](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 後續步驟

完成這些範例後，探索完整課程：
- [AI 入門](../lessons/1-Intro/README.md)
- [神經網絡](../lessons/3-NeuralNetworks/README.md)
- [電腦視覺](../lessons/4-ComputerVision/README.md)
- [自然語言處理](../lessons/5-NLP/README.md)

## 🤝 貢獻

覺得這些範例有幫助嗎？幫助我們改進它們：
- 回報問題或提出改進建議
- 增加更多適合初學者的範例
- 改進文件與註解

---

*記住：每位專家都曾是初學者。祝學習愉快！🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->