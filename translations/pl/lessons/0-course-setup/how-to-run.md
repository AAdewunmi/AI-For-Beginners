# Jak uruchomić kod

Ten program nauczania zawiera wiele wykonalnych przykładów i laboratoriów, które zechcesz uruchomić. Aby to zrobić, potrzebujesz możliwości wykonywania kodu Python w Jupyter Notebooks udostępnionych w ramach tego kursu. Masz kilka opcji uruchamiania kodu:

## Uruchamianie lokalnie na komputerze

Aby uruchomić kod lokalnie na komputerze, potrzebna jest instalacja Pythona. Jedną z rekomendacji jest zainstalowanie **[miniconda](https://conda.io/en/latest/miniconda.html)** – to dość lekka instalacja, która obsługuje menedżera pakietów `conda` dla różnych **wirtualnych środowisk** Pythona.

Po zainstalowaniu miniconda, sklonuj repozytorium i utwórz wirtualne środowisko do wykorzystania w tym kursie:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Korzystanie z Visual Studio Code z rozszerzeniem Python

Ten kurs najlepiej używać, otwierając go w [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) z [rozszerzeniem Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Uwaga**: Po sklonowaniu i otwarciu katalogu w VS Code, program automatycznie zasugeruje instalację rozszerzeń Pythona. Musisz też zainstalować miniconda według wyżej opisanych kroków.

> **Uwaga**: Jeśli VS Code zasugeruje ponowne otwarcie repozytorium w kontenerze, powinieneś odmówić, by korzystać z lokalnej instalacji Pythona.

### Korzystanie z Jupyter w przeglądarce

Możesz też używać środowiska Jupyter w przeglądarce na własnym komputerze. Zarówno klasyczny Jupyter, jak i JupyterHub oferują wygodne środowisko programistyczne z autouzupełnianiem, podświetlaniem kodu itp.

Aby uruchomić Jupyter lokalnie, przejdź do katalogu kursu i wykonaj:

```bash
jupyter notebook
```
lub
```bash
jupyterhub
```
Następnie możesz przejść do dowolnego pliku `.ipynb`, otworzyć go i zacząć pracę.

### Uruchamianie w kontenerze

Alternatywą dla instalacji Pythona może być uruchomienie kodu w kontenerze. Ponieważ nasze repozytorium zawiera specjalny folder `.devcontainer`, który instruuje, jak zbudować kontener dla tego repozytorium, VS Code oferuje możliwość ponownego otwarcia kodu w kontenerze. Wymaga to zainstalowania Dockera i jest to bardziej skomplikowane, więc zalecamy tę opcję bardziej doświadczonym użytkownikom.

## Uruchamianie w chmurze

Jeśli nie chcesz instalować Pythona lokalnie i masz dostęp do zasobów chmurowych – dobrą alternatywą jest uruchamianie kodu w chmurze. Możesz to zrobić na kilka sposobów:

* Korzystając z **[GitHub Codespaces](https://github.com/features/codespaces)**, czyli wirtualnego środowiska utworzonego dla Ciebie na GitHub i dostępnego przez interfejs VS Code w przeglądarce. Jeśli masz dostęp do Codespaces, wystarczy kliknąć przycisk **Code** w repozytorium, uruchomić codespace i szybko zacząć pracę.
* Korzystając z **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) oferuje bezpłatne zasoby obliczeniowe w chmurze dla osób takich jak Ty do testowania kodu z GitHub. Na stronie głównej jest przycisk do otwarcia repozytorium w Binder – szybko przeniesie Cię on do serwisu binder, który zbuduje kontener i bezproblemowo uruchomi interfejs Jupyter w przeglądarce.

> **Uwaga**: Aby zapobiec nadużyciom, Binder ma zablokowany dostęp do niektórych zasobów internetowych. Może to uniemożliwić działanie niektórych fragmentów kodu, które pobierają modele i/lub zestawy danych z internetu. Możesz potrzebować obejść te ograniczenia. Poza tym zasoby obliczeniowe udostępniane przez Binder są dość podstawowe, więc trenowanie będzie powolne, zwłaszcza w późniejszych, bardziej skomplikowanych lekcjach.

## Uruchamianie w chmurze z GPU

Niektóre z późniejszych lekcji w tym kursie bardzo skorzystałyby na wsparciu GPU. Trenowanie modeli może być w przeciwnym razie bardzo powolne. Masz kilka opcji, zwłaszcza jeśli masz dostęp do chmury przez [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) lub przez swoją instytucję:

* Utwórz [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) i połącz się z nią przez Jupyter. Możesz wtedy sklonować repozytorium bezpośrednio na maszynę i zacząć naukę. Maszyny NC-series mają wsparcie GPU.

> **Uwaga**: Niektóre subskrypcje, w tym Azure for Students, nie oferują domyślnie wsparcia GPU. Może być konieczne zgłoszenie prośby o dodatkowe rdzenie GPU do pomocy technicznej.

* Utwórz [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), a następnie używaj tam funkcji Notatnika. [Ten film](https://azure-for-academics.github.io/quickstart/azureml-papers/) pokazuje, jak sklonować repozytorium do notatnika Azure ML i zacząć je wykorzystywać.

Możesz także użyć Google Colab, który oferuje bezpłatną obsługę GPU i przesłać tam Jupyter Notebooks, aby wykonywać je pojedynczo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->