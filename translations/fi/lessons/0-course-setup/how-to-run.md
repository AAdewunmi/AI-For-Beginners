# Kuinka ajaa koodi

Tämä opetussuunnitelma sisältää paljon suoritettavia esimerkkejä ja labroja, joita haluat varmasti ajaa. Tätä varten sinun täytyy pystyä suorittamaan Python-koodia Jupyter-muistikirjoissa, joita tarjotaan osana tätä opetussuunnitelmaa. Sinulla on useita vaihtoehtoja koodin ajamiseen:

## Aja paikallisesti tietokoneellasi

Jotta voit ajaa koodin paikallisesti tietokoneellasi, tarvitset Python-asennuksen. Suosittelemme asentamaan **[minicondan](https://conda.io/en/latest/miniconda.html)** – se on melko kevyt asennus, joka tukee `conda`-paketinhallintaa eri Python **virtuaaliympäristöille**.

Kun olet asentanut minicondan, kloonaa repositorio ja luo virtuaaliympäristö tätä kurssia varten:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Coden käyttäminen Python-laajennuksella

Tämä opetussuunnitelma on parhaiten käytettävissä avaamalla se [Visual Studio Codessa](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) yhdessä [Python-laajennuksen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) kanssa.

> **Huom:** Kun kloonaat ja avaat kansion VS Codessa, se ehdottaa automaattisesti Python-laajennusten asentamista. Sinun täytyy myös asentaa miniconda yllä kuvatulla tavalla.

> **Huom:** Jos VS Code ehdottaa kansion uudelleenavaamista kontissa, sinun kannattaa kieltäytyä tästä käyttääksesi paikallista Python-asennusta.

### Jupyteriä selaimessa käyttäen

Voit myös käyttää Jupyter-ympäristöä selaimessa omalla tietokoneellasi. Sekä klassinen Jupyter että JupyterHub tarjoavat kätevän kehitysympäristön automaattisen täydennyksen, koodin korostuksen yms. kanssa.

Aloittaaksesi Jupyteriä paikallisesti, siirry kurssin kansioon ja suorita:

```bash
jupyter notebook
```
tai
```bash
jupyterhub
```
Sitten voit siirtyä mihin tahansa `.ipynb`-tiedostoista, avata ne ja aloittaa työn.

### Ajaminen kontissa

Vaihtoehtona Python-asennukselle voit ajaa koodin kontissa. Koska meidän repositoriomme sisältää erityisen `.devcontainer`-kansion, joka ohjeistaa konttien rakentamista tälle repositoriolle, VS Code tarjoaa mahdollisuuden avata koodin uudelleen kontissa. Tämä vaatii Dockeriin asennuksen ja on myös monimutkaisempi, joten suosittelemme tätä kokeneemmille käyttäjille.

## Ajaminen pilvessä

Jos et halua asentaa Pythonia paikallisesti ja sinulla on pääsy joihinkin pilviresursseihin, hyvä vaihtoehto on ajaa koodi pilvessä. Tätä voit tehdä monella tavalla:

* Käyttämällä **[GitHub Codespaces](https://github.com/features/codespaces)**, joka on sinulle GitHubissa luotu virtuaaliympäristö, jota pääset käyttämään VS Coden selainkäyttöliittymän kautta. Jos sinulla on pääsy Codespacesiin, voit vain klikata **Code**-painiketta repositoriossa, käynnistää codespacen ja päästä nopeasti töihin.
* Käyttämällä **[Binderia](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) tarjoaa ilmaisia pilvessä toimivia laskentaresursseja, jotta voit testata koodia GitHubissa. Alkusivulla on painike, jolla voit avata repositorion Binderissä – tämä vie sinut nopeasti binder-sivustolle, joka rakentaa taustalle konttialustan ja käynnistää sinulle sujuvasti Jupyter-verkkokäyttöliittymän.

> **Huom:** väärinkäytösten estämiseksi Binderillä on estetty pääsy joihinkin verkkoresursseihin. Tämä saattaa estää joidenkin koodien toiminnan, jos ne hakevat malleja ja/tai aineistoja julkisesta internetistä. Sinun täytyy ehkä keksiä kiertotapoja. Lisäksi Binderin tarjoamat laskentaresurssit ovat varsin rajalliset, joten mallien koulutus on hidasta, varsinkin myöhemmissä ja monimutkaisemmissa tehtävissä.

## Ajaminen pilvessä GPU:lla

Jotkin tämän opetussuunnitelman myöhemmistä tehtävistä hyötyvät suuresti GPU-tuesta. Esimerkiksi mallin koulutus voi olla muuten tuskallisen hidasta. Sinulla on muutama vaihtoehto, etenkin jos sinulla on pääsy pilveen joko [Azure for Studentsin](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) kautta tai oppilaitoksesi kautta:

* Luo [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) ja yhdistä siihen Jupyteriä käyttäen. Voit kloonata repositorion suorilta koneelle ja aloittaa opiskelun. NC-sarjan VM:issä on GPU-tuki.

> **Huom:** Jotkin tilaukset, mukaan lukien Azure for Students, eivät tarjoa GPU-tukea oletuksena. Saatat joutua pyytämään lisä-GPU-ytimiä teknisen tuen kautta.

* Luo [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ja käytä siellä Notebook-ominaisuutta. [Tämä video](https://azure-for-academics.github.io/quickstart/azureml-papers/) näyttää, miten kloonataan repositorio Azure ML Notebooksiin ja aletaan sitä käyttää.

Voit myös käyttää Google Colabia, joka tarjoaa jonkin verran ilmaista GPU-tukea, ja ladata sinne Jupyter-muistikirjat suoritettavaksi yksitellen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->