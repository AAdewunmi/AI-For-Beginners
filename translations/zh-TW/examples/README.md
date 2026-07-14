# 初學者友善的 AI 範例

歡迎！此目錄包含簡單且獨立的範例，幫助你開始 AI 與機器學習之旅。每個範例都設計為適合初學者，附有詳細註解與逐步說明。

## 📚 範例總覽

| 範例 | 說明 | 難度 | 先備知識 |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | 你的第一個 AI 程式 - 簡單模式識別 | ⭐ 初學者 | Python 基礎 |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | 從零開始建立神經網路 | ⭐⭐ 初學者+ | Python，基礎數學 |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | 使用預訓練模型分類影像 | ⭐⭐ 初學者+ | Python，numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | 分析文字情緒（正面/負面） | ⭐⭐ 初學者+ | Python |

## 🚀 開始使用

### 先決條件

確認你已安裝 Python（建議版本 3.8 以上）。安裝必要套件：

```bash
# 適用於 Python 腳本
pip install numpy

# 適用於 Jupyter 筆記本（影像分類器）
pip install jupyter numpy pillow tensorflow
```

或使用主課程中的 conda 環境：

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

建議依序循序進行範例：

1. **從「Hello AI World」開始** - 學習模式識別基礎
2. <strong>建立簡單神經網路</strong> - 了解神經網路如何運作
3. <strong>嘗試影像分類器</strong> - 觀察 AI 如何處理真實影像
4. <strong>分析文字情緒</strong> - 探索自然語言處理

## 💡 初學者技巧

- <strong>仔細閱讀程式碼註解</strong> - 解釋每行程式的作用
- **多多嘗試！** - 改變數值，看看會發生什麼
- <strong>不必急著全部懂</strong> - 學習需要時間
- <strong>勇於提問</strong> - 利用 [討論區](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 下一步

完成這些範例後，探索完整課程：
- [AI 入門](../lessons/1-Intro/README.md)
- [神經網路](../lessons/3-NeuralNetworks/README.md)
- [電腦視覺](../lessons/4-ComputerVision/README.md)
- [自然語言處理](../lessons/5-NLP/README.md)

## 🤝 貢獻

覺得這些範例有幫助嗎？來幫助我們改進吧：
- 回報問題或提出改進建議
- 新增更多初學者範例
- 改善文件與註解

---

*記得：每位專家都曾是初學者。祝學習愉快！🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->