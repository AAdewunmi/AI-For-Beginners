# Cara Menjalankan Kode

Kurikulum ini berisi banyak contoh dan lab yang dapat dijalankan yang mungkin ingin Anda jalankan. Untuk melakukan ini, Anda memerlukan kemampuan menjalankan kode Python di Jupyter Notebooks yang disediakan sebagai bagian dari kurikulum ini. Anda memiliki beberapa opsi untuk menjalankan kode:

## Menjalankan secara lokal di komputer Anda

Untuk menjalankan kode secara lokal di komputer Anda, diperlukan instalasi Python. Salah satu rekomendasinya adalah menginstal **[miniconda](https://conda.io/en/latest/miniconda.html)** - ini adalah instalasi yang cukup ringan yang mendukung pengelola paket `conda` untuk berbagai **lingkungan virtual** Python.

Setelah Anda menginstal miniconda, kloning repositori dan buat lingkungan virtual yang akan digunakan untuk kursus ini:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Menggunakan Visual Studio Code dengan Ekstensi Python

Kurikulum ini paling baik digunakan saat membukanya di [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) dengan [Ekstensi Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Catatan**: Setelah Anda mengkloning dan membuka direktori di VS Code, secara otomatis akan menyarankan Anda untuk menginstal ekstensi Python. Anda juga perlu menginstal miniconda seperti yang dijelaskan di atas.

> **Catatan**: Jika VS Code menyarankan untuk membuka kembali repositori dalam sebuah kontainer, Anda harus menolak ini untuk menggunakan instalasi Python lokal.

### Menggunakan Jupyter di Browser

Anda juga dapat menggunakan lingkungan Jupyter dari browser di komputer Anda sendiri. Baik Jupyter klasik maupun JupyterHub menyediakan lingkungan pengembangan yang nyaman dengan auto-completion, penyorotan kode, dll.

Untuk memulai Jupyter secara lokal, pergi ke direktori kursus, dan jalankan:

```bash
jupyter notebook
```
atau
```bash
jupyterhub
```
Kemudian Anda dapat menavigasi ke salah satu file `.ipynb`, membukanya, dan mulai bekerja.

### Menjalankan di dalam kontainer

Alternatif lain untuk instalasi Python adalah menjalankan kode dalam kontainer. Karena repositori kami menyediakan folder khusus `.devcontainer` yang mengarahkan bagaimana membangun kontainer untuk repo ini, VS Code menawarkan kesempatan untuk membuka ulang kode di dalam kontainer. Ini memerlukan instalasi Docker, dan juga akan lebih kompleks, jadi kami merekomendasikan hal ini untuk pengguna yang lebih berpengalaman.

## Menjalankan di Cloud

Jika Anda tidak ingin menginstal Python secara lokal, dan memiliki akses ke beberapa sumber daya cloud - alternatif yang baik adalah menjalankan kode di cloud. Ada beberapa cara yang dapat Anda lakukan ini:

* Menggunakan **[GitHub Codespaces](https://github.com/features/codespaces)**, yang merupakan lingkungan virtual yang dibuat untuk Anda di GitHub, dapat diakses melalui antarmuka browser VS Code. Jika Anda memiliki akses ke Codespaces, Anda hanya perlu klik tombol **Code** di repo, mulai codespace, dan segera berjalan.
* Menggunakan **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) menyediakan sumber daya komputasi gratis di cloud untuk orang-orang seperti Anda agar dapat mencoba beberapa kode di GitHub. Ada tombol di halaman depan untuk membuka repositori di Binder - ini akan membawa Anda cepat ke situs binder, yang akan membangun kontainer dasar dan memulai antarmuka web Jupyter untuk Anda secara mulus.

> **Catatan**: Untuk mencegah penyalahgunaan, Binder memblokir akses ke beberapa sumber daya web. Ini mungkin akan menghalangi sebagian kode untuk berjalan, terutama yang mengambil model dan/atau dataset dari Internet publik. Anda mungkin perlu mencari solusi alternatif. Selain itu, sumber daya komputasi yang disediakan oleh Binder cukup dasar, jadi pelatihan akan lambat, terutama pada pelajaran yang lebih kompleks di kemudian hari.

## Menjalankan di Cloud dengan GPU

Beberapa pelajaran terakhir dalam kurikulum ini akan sangat diuntungkan dengan dukungan GPU. Pelatihan model, misalnya, bisa sangat lambat jika tanpa GPU. Ada beberapa opsi yang dapat Anda ikuti, terutama jika Anda memiliki akses ke cloud baik melalui [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), atau melalui institusi Anda:

* Buat [Data Science Virtual Machine](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) dan sambungkan ke mesin tersebut melalui Jupyter. Anda kemudian dapat mengkloning repo langsung ke mesin ini, dan mulai belajar. VM seri NC memiliki dukungan GPU.

> **Catatan**: Beberapa langganan, termasuk Azure for Students, tidak menyediakan dukungan GPU secara langsung. Anda mungkin perlu meminta tambahan inti GPU dengan permintaan dukungan teknis.

* Buat [Azure Machine Learning Workspace](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) dan kemudian gunakan fitur Notebook di sana. [Video ini](https://azure-for-academics.github.io/quickstart/azureml-papers/) menunjukkan cara mengkloning repositori ke dalam notebook Azure ML dan mulai menggunakannya.

Anda juga dapat menggunakan Google Colab, yang menyertakan beberapa dukungan GPU gratis, dan mengunggah Jupyter Notebooks di sana untuk menjalankannya satu per satu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->