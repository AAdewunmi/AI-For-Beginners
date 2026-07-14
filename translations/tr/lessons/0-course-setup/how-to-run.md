# Kodu Nasıl Çalıştırılır

Bu müfredat, çalıştırmak isteyeceğiniz birçok yürütülebilir örnek ve laboratuvar içermektedir. Bunu yapabilmek için, bu müfredatın bir parçası olarak sağlanan Jupyter Notebooks içinde Python kodu çalıştırma yeteneğine sahip olmanız gerekir. Kodu çalıştırmak için birkaç seçeneğiniz vardır:

## Bilgisayarınızda Yerel Olarak Çalıştırma

Kodu bilgisayarınızda yerel olarak çalıştırmak için, bir Python kurulumu gereklidir. Bir öneri **[miniconda](https://conda.io/en/latest/miniconda.html)** kurmaktır - bu, farklı Python **sanal ortamları** için `conda` paket yöneticisini destekleyen oldukça hafif bir kurulumdur.

Miniconda'yı kurduktan sonra, depo klonlayın ve bu kurs için kullanılacak bir sanal ortam oluşturun:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Visual Studio Code ve Python Eklentisi ile Kullanma

Bu müfredat, [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) ve [Python Eklentisi](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste) ile açıldığında en iyi şekilde kullanılır.

> **Not**: Depoyu klonlayıp dizini VS Code'da açtığınızda, Python uzantılarını yüklemenizi otomatik olarak önerir. Ayrıca yukarıda açıklandığı gibi miniconda'yı da kurmanız gerekir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, yerel Python kurulumunu kullanmak için bunu reddetmelisiniz.

### Tarayıcıda Jupyter Kullanma

Kendi bilgisayarınızda tarayıcı üzerinden Jupyter ortamı da kullanabilirsiniz. Klasik Jupyter ve JupyterHub, otomatik tamamlama, kod vurgulama vb. özelliklerle kullanışlı bir geliştirme ortamı sunar.

Jupyter'ı yerel olarak başlatmak için, kurs dizinine gidin ve şunu çalıştırın:

```bash
jupyter notebook
```
 veya
```bash
jupyterhub
```
 Ardından `.ipynb` dosyalarından herhangi birine gidip açabilir ve çalışmaya başlayabilirsiniz.

### Konteyner İçinde Çalıştırma

Python kurulumu yerine kodu bir konteyner içinde çalıştırmak da bir alternatiftir. Depomuz, bu depo için bir konteyner nasıl oluşturulacağını belirten özel bir `.devcontainer` klasörü sağladığından, VS Code kodu bir konteyner içinde yeniden açma olanağı sunar. Bu Docker kurulumu gerektirir ve daha karmaşık olabilir, bu yüzden daha deneyimli kullanıcılar için tavsiye ederiz.

## Bulutta Çalıştırma

Python'ı yerel olarak kurmak istemiyorsanız ve bazı bulut kaynaklarına erişiminiz varsa, kodu bulutta çalıştırmak iyi bir alternatif olacaktır. Bunu yapabileceğiniz birkaç yol vardır:

* GitHub üzerinde sizin için oluşturulan ve VS Code tarayıcı arayüzüyle erişilen bir sanal ortam olan **[GitHub Codespaces](https://github.com/features/codespaces)** kullanmak. Eğer Codespaces erişiminiz varsa, depoda **Code** butonuna tıklayıp bir codespace başlatarak hemen çalışmaya başlayabilirsiniz.
* **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)** kullanmak. [Binder](https://mybinder.org), GitHub'daki bazı kodları test etmek isteyenler için bulut üzerinden ücretsiz hesaplama kaynakları sunar. Ana sayfada depoyu Binder'da açmak için bir buton vardır – bu sizi hızla binder sitesine götürür, arka planda bir konteyner oluşturur ve sorunsuz bir Jupyter web arayüzü başlatır.

> **Not**: Kötüye kullanımı engellemek için, Binder bazı web kaynaklarına erişimi engeller. Bu, modelleri ve/veya veri setlerini genel Internet'ten alan bazı kodların çalışmasını engelleyebilir. Bazı çözümler bulmanız gerekebilir. Ayrıca, Binder tarafından sağlanan hesaplama kaynakları oldukça basit olduğundan, özellikle sonraki daha karmaşık derslerde eğitim yavaş olacaktır.

## GPU ile Bulutta Çalıştırma

Bu müfredattaki bazı ileri dersler GPU desteğinden büyük ölçüde faydalanacaktır. Örneğin model eğitimi, aksi takdirde çok yavaş olabilir. Özellikle [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste) veya kurumunuz vasıtasıyla buluta erişiminiz varsa, takip edebileceğiniz birkaç seçenek vardır:

* [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) oluşturup Jupyter aracılığıyla bağlanmak. Ardından depoyu makineye klonlayıp öğrenmeye başlayabilirsiniz. NC-serisi VM'ler GPU desteğine sahiptir.

> **Not**: Azure for Students dahil bazı abonelikler kutudan çıkar çıkmaz GPU desteği sağlamaz. Ek GPU çekirdeği talebinde bulunmak için teknik destek isteğinde bulunmanız gerekebilir.

* [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) oluşturup oradaki Notebook özelliğini kullanmak. [Bu video](https://azure-for-academics.github.io/quickstart/azureml-papers/) Azure ML notebook içine depo klonlama ve kullanmaya başlama gösterir.

Ayrıca, biraz ücretsiz GPU desteği ile gelen Google Colab'i kullanabilir ve Jupyter Notebooks'ları oraya yükleyip tek tek çalıştırabilirsiniz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->