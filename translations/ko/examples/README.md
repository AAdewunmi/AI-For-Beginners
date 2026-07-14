# 초보자 친화적 AI 예제

환영합니다! 이 디렉터리에는 AI와 머신러닝을 시작하는 데 도움이 되는 간단하고 독립적인 예제가 포함되어 있습니다. 각 예제는 자세한 주석과 단계별 설명으로 초보자도 쉽게 따라할 수 있도록 설계되었습니다.

## 📚 예제 개요

| 예제 | 설명 | 난이도 | 필요 조건 |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | 첫 번째 AI 프로그램 - 간단한 패턴 인식 | ⭐ 초보자 | Python 기초 |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | 신경망을 처음부터 구축하기 | ⭐⭐ 초보자+ | Python, 기초 수학 |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | 사전 학습된 모델로 이미지 분류하기 | ⭐⭐ 초보자+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | 텍스트 감정 분석 (긍정/부정) | ⭐⭐ 초보자+ | Python |

## 🚀 시작하기

### 필요 조건

Python이 설치되어 있는지 확인하세요 (3.8 이상 권장). 필요 패키지 설치:

```bash
# 파이썬 스크립트용
pip install numpy

# 주피터 노트북용 (이미지 분류기)
pip install jupyter numpy pillow tensorflow
```

또는 메인 커리큘럼의 conda 환경을 사용하세요:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 예제 실행하기

**Python 스크립트 (.py 파일)의 경우:**
```bash
python 01-hello-ai-world.py
```

**Jupyter 노트북 (.ipynb 파일)의 경우:**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 학습 경로

다음 순서로 예제를 학습하는 것을 권장합니다:

1. **"Hello AI World"부터 시작하기** - 패턴 인식의 기초 배우기
2. **간단한 신경망 구축** - 신경망 작동 원리 이해하기
3. **이미지 분류기 시도해보기** - 실제 이미지로 AI 적용해 보기
4. **텍스트 감정 분석** - 자연어 처리 탐험하기

## 💡 초보자 팁

- **코드 주석을 꼼꼼히 읽으세요** - 각 줄이 무엇을 하는지 설명함
- **실험해보세요!** - 값을 바꿔보고 어떤 변화가 있는지 확인하세요
- **모든 것을 완벽히 이해하지 않아도 괜찮아요** - 학습은 시간이 걸립니다
- <strong>질문하세요</strong> - [토론 게시판](https://github.com/microsoft/AI-For-Beginners/discussions)을 활용하세요

## 🔗 다음 단계

이 예제를 완료한 후, 전체 커리큘럼을 탐색하세요:
- [AI 소개](../lessons/1-Intro/README.md)
- [신경망](../lessons/3-NeuralNetworks/README.md)
- [컴퓨터 비전](../lessons/4-ComputerVision/README.md)
- [자연어 처리](../lessons/5-NLP/README.md)

## 🤝 기여하기

이 예제가 도움이 되었나요? 개선에 참여해주세요:
- 문제점 보고 또는 개선 제안
- 초보자를 위한 더 많은 예제 추가
- 문서와 주석 개선

---

*기억하세요: 모든 전문가도 한때는 초보자였습니다. 즐거운 학습 되세요! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->