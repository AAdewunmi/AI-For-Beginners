# 适合初学者的 AI 示例

欢迎！该目录包含简单的独立示例，帮助您入门 AI 和机器学习。每个示例都设计得适合初学者，配有详细注释和逐步解释。

## 📚 示例概览

| 示例 | 描述 | 难度 | 先决条件 |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | 你的第一个 AI 程序 - 简单的模式识别 | ⭐ 初学者 | Python 基础 |
| [简单神经网络](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | 从零搭建神经网络 | ⭐⭐ 初学者+ | Python，基础数学 |
| [图像分类器](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | 使用预训练模型分类图像 | ⭐⭐ 初学者+ | Python，numpy |
| [文本情感分析](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | 分析文本情感（正面/负面） | ⭐⭐ 初学者+ | Python |

## 🚀 快速开始

### 先决条件

请确保安装了 Python（推荐版本 3.8 及以上）。安装所需的包：

```bash
# 用于Python脚本
pip install numpy

# 用于Jupyter笔记本（图像分类器）
pip install jupyter numpy pillow tensorflow
```

或者使用主课程中的 conda 环境：

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 运行示例

**对于 Python 脚本（.py 文件）：**
```bash
python 01-hello-ai-world.py
```

**对于 Jupyter 笔记本（.ipynb 文件）：**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 学习路径

我们建议按顺序完成以下示例：

1. **从 “Hello AI World” 开始** - 学习模式识别基础
2. <strong>构建一个简单神经网络</strong> - 理解神经网络的工作原理
3. <strong>尝试图像分类器</strong> - 体验 AI 在真实图像中的应用
4. <strong>分析文本情感</strong> - 探索自然语言处理

## 💡 初学者提示

- <strong>仔细阅读代码注释</strong> - 它们解释了每行代码的作用
- **多多实验！** - 尝试修改数值，观察结果
- <strong>不用担心一开始理解全部内容</strong> - 学习需要时间
- <strong>有问题就问</strong> - 使用[讨论区](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 后续步骤

完成这些示例后，继续探索完整课程：
- [AI 入门介绍](../lessons/1-Intro/README.md)
- [神经网络](../lessons/3-NeuralNetworks/README.md)
- [计算机视觉](../lessons/4-ComputerVision/README.md)
- [自然语言处理](../lessons/5-NLP/README.md)

## 🤝 贡献指南

觉得这些示例有帮助吗？帮助我们改进它们：
- 报告问题或提出改进建议
- 添加更多适合初学者的示例
- 改进文档和注释

---

*记住：每个专家都曾是初学者。祝学习愉快！🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->