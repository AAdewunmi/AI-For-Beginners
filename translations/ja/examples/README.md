# 初心者向けAI例

ようこそ！このディレクトリには、AIや機械学習を始めるためのシンプルで独立した例が含まれています。各例は詳細なコメントと段階的な説明があり、初心者に優しい設計です。

## 📚 例の概要

| 例 | 説明 | 難易度 | 前提条件 |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | はじめてのAIプログラム - シンプルなパターン認識 | ⭐ 初心者 | Pythonの基本 |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | ニューラルネットワークをゼロから作成 | ⭐⭐ 初心者+ | Python、基礎数学 |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | 事前学習済みモデルで画像分類 | ⭐⭐ 初心者+ | Python、numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | テキストの感情分析（ポジティブ/ネガティブ） | ⭐⭐ 初心者+ | Python |

## 🚀 はじめに

### 前提条件

Pythonがインストールされていることを確認してください（3.8以上を推奨）。必要なパッケージをインストールします：

```bash
# Pythonスクリプト用
pip install numpy

# Jupyterノートブック用（画像分類器）
pip install jupyter numpy pillow tensorflow
```

またはメインカリキュラムのconda環境を使用してください：

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 実行方法

**Pythonスクリプト（.pyファイル）の場合：**
```bash
python 01-hello-ai-world.py
```

**Jupyterノートブック（.ipynbファイル）の場合：**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 学習の流れ

以下の順番で例を進めることをおすすめします：

1. **「Hello AI World」から始める** - パターン認識の基礎を学ぶ
2. <strong>シンプルなニューラルネットワークを作る</strong> - ニューラルネットワークの仕組みを理解する
3. **Image Classifierに挑戦** - 実際の画像でAIを体験する
4. <strong>テキストの感情分析を行う</strong> - 自然言語処理を探求する

## 💡 初心者向けのヒント

- <strong>コードのコメントをよく読む</strong> - 各行の意味を説明しています
- **実験してみる！** - 値を変えて何が起きるか試しましょう
- <strong>すべてを理解しようと焦らないで</strong> - 学習は時間がかかります
- <strong>質問をする</strong> - [ディスカッションボード](https://github.com/microsoft/AI-For-Beginners/discussions)を利用しましょう

## 🔗 次のステップ

これらの例を終えたら、完全なカリキュラムを探求してください：
- [AI入門](../lessons/1-Intro/README.md)
- [ニューラルネットワーク](../lessons/3-NeuralNetworks/README.md)
- [コンピュータビジョン](../lessons/4-ComputerVision/README.md)
- [自然言語処理](../lessons/5-NLP/README.md)

## 🤝 貢献

これらの例が役立ったと思ったら、改善にご協力ください：
- 問題の報告や改善提案
- 初心者向けの例をもっと追加
- ドキュメントやコメントの改善

---

*覚えておいてください：すべての専門家もかつては初心者でした。楽しい学習を！ 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->