# 코드 실행 방법

이 교과 과정에는 실행 가능한 예제와 실습이 많이 포함되어 있어 직접 실행해보고 싶을 것입니다. 이를 위해서는 이 교과 과정의 일부로 제공되는 Jupyter 노트북에서 Python 코드를 실행할 수 있어야 합니다. 코드를 실행하는 데에는 여러 가지 옵션이 있습니다:

## 컴퓨터에서 로컬 실행하기

컴퓨터에서 코드를 로컬로 실행하려면 Python 설치가 필요합니다. 추천하는 방법 중 하나는 **[miniconda](https://conda.io/en/latest/miniconda.html)** 를 설치하는 것입니다. miniconda는 가벼운 설치 방식으로, 다양한 Python <strong>가상 환경</strong>을 지원하는 `conda` 패키지 관리자를 제공합니다.

miniconda를 설치한 후 리포지토리를 클론하고 이 과정에 사용할 가상 환경을 생성합니다:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Python 확장과 함께 Visual Studio Code 사용하기

이 교과 과정은 [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste)에서 [Python 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste)을 통해 열어 사용하는 것이 가장 좋습니다.

> <strong>참고</strong>: 리포지토리를 클론하고 VS Code에서 디렉터리를 열면 자동으로 Python 확장 설치를 제안합니다. 또한 위에 설명된 대로 miniconda를 설치해야 합니다.

> <strong>참고</strong>: VS Code가 리포지토리를 컨테이너에서 다시 열라고 제안하면, 로컬 Python 설치를 사용하려면 이를 거절해야 합니다. 

### 브라우저에서 Jupyter 사용하기

자신의 컴퓨터 브라우저에서 Jupyter 환경을 사용할 수도 있습니다. 전통적인 Jupyter와 JupyterHub 모두 자동 완성, 코드 하이라이트 등의 편리한 개발 환경을 제공합니다.

로컬에서 Jupyter를 시작하려면, 과정 디렉터리로 이동하여 다음을 실행하세요:

```bash
jupyter notebook
```
또는
```bash
jupyterhub
```
그런 다음 `.ipynb` 파일 중 원하는 것을 찾아 열고 작업을 시작할 수 있습니다.

### 컨테이너에서 실행하기

Python 설치 대신 컨테이너에서 코드를 실행하는 방법도 있습니다. 이 리포지토리는 컨테이너를 빌드하는 방법을 안내하는 특별한 `.devcontainer` 폴더를 제공하므로 VS Code가 코드를 컨테이너에서 다시 열 수 있는 기능을 제공합니다. 이 방법은 Docker 설치가 필요하고 다소 복잡하므로, 경험이 있는 사용자에게 권장합니다.

## 클라우드에서 실행하기

로컬에 Python을 설치하지 않고 클라우드 자원에 접근할 수 있다면, 클라우드에서 코드를 실행하는 것도 좋은 대안입니다. 이를 할 수 있는 여러 방법이 있습니다:

* **[GitHub Codespaces](https://github.com/features/codespaces)** 이용하기: 이는 GitHub 상에서 가상 환경을 생성하고 VS Code 브라우저 인터페이스를 통해 접근할 수 있습니다. Codespaces에 접근 권한이 있으면 리포지토리의 **Code** 버튼을 클릭하고 Codespace를 시작하면 바로 실행할 수 있습니다.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** 이용하기: [Binder](https://mybinder.org)는 GitHub의 코드를 테스트할 수 있도록 클라우드에서 무료 컴퓨팅 자원을 제공합니다. 리포지토리 메인 페이지에 있는 버튼을 누르면 Binder 사이트로 빠르게 이동해 해당 컨테이너를 빌드하고 Jupyter 웹 인터페이스를 원활하게 시작할 수 있습니다.

> <strong>참고</strong>: Binder는 남용 방지를 위해 일부 웹 자원 접근을 차단합니다. 이로 인해 공개 인터넷에서 모델이나 데이터셋을 불러오는 코드가 제대로 작동하지 않을 수 있습니다. 우회 방법을 찾아야 할 수도 있습니다. 또한, Binder가 제공하는 컴퓨팅 자원은 기본적인 수준이므로 이후의 복잡한 수업에서는 학습 속도가 느릴 수 있습니다.

## GPU가 탑재된 클라우드에서 실행하기

이 교과 과정의 후반부 수업들은 GPU 지원이 크게 도움이 됩니다. 예를 들어 모델 학습이 그렇지 않으면 매우 느릴 수 있습니다. 특히 [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste)나 학교를 통한 클라우드 접근 권한이 있다면 다음과 같은 옵션이 있습니다:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste)을 생성하고 Jupyter로 연결하기. 머신에 리포지토리를 클론해서 바로 학습할 수 있습니다. NC 시리즈 VM은 GPU를 지원합니다.

> <strong>참고</strong>: Azure for Students 등 일부 구독은 기본적으로 GPU를 제공하지 않습니다. 추가 GPU 코어가 필요한 경우 기술 지원 요청을 해야 할 수 있습니다.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)를 생성한 후 그곳의 노트북 기능을 사용하기. [이 영상](https://azure-for-academics.github.io/quickstart/azureml-papers/)에서는 Azure ML 노트북에 리포지토리를 클론해서 사용하는 방법을 보여줍니다.

또한 Google Colab을 이용하면 무료 GPU 지원과 함께 Jupyter 노트북을 하나씩 업로드해 실행할 수 있습니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->