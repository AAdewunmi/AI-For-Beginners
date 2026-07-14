# Cómo Ejecutar el Código

Este currículo contiene muchos ejemplos ejecutables y laboratorios que querrás ejecutar. Para hacer esto, necesitas la capacidad de ejecutar código Python en Jupyter Notebooks que se proporcionan como parte de este currículo. Tienes varias opciones para ejecutar el código:

## Ejecutar localmente en tu computadora

Para ejecutar el código localmente en tu computadora, se necesita una instalación de Python. Una recomendación es instalar **[miniconda](https://conda.io/en/latest/miniconda.html)** - es una instalación bastante ligera que soporta el gestor de paquetes `conda` para diferentes **entornos virtuales** de Python.

Después de instalar miniconda, clona el repositorio y crea un entorno virtual que se usará para este curso:

```bash
git clone http://github.com/microsoft/ai-for-beginners
cd ai-for-beginners
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

### Usando Visual Studio Code con la Extensión de Python

Este currículo es mejor utilizarlo abriéndolo en [Visual Studio Code](http://code.visualstudio.com/?WT.mc_id=academic-77998-cacaste) con la [Extensión de Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-77998-cacaste).

> **Nota**: Una vez que clonas y abres el directorio en VS Code, te sugerirá automáticamente instalar extensiones de Python. También tendrás que instalar miniconda como se describió arriba.

> **Nota**: Si VS Code te sugiere reabrir el repositorio en un contenedor, deberías rechazar esto para usar la instalación local de Python.

### Usar Jupyter en el Navegador

También puedes usar un entorno Jupyter desde el navegador en tu propia computadora. Tanto Jupyter clásico como JupyterHub proporcionan un entorno de desarrollo conveniente con autocompletado, resaltado de código, etc.

Para iniciar Jupyter localmente, ve al directorio del curso y ejecuta:

```bash
jupyter notebook
```
o
```bash
jupyterhub
```
Luego puedes navegar a cualquiera de los archivos `.ipynb`, abrirlos y comenzar a trabajar.

### Ejecutar en contenedor

Una alternativa a la instalación de Python sería ejecutar el código en un contenedor. Dado que nuestro repositorio suministra una carpeta especial `.devcontainer` que indica cómo construir un contenedor para este repositorio, VS Code ofrece la posibilidad de reabrir el código en un contenedor. Esto requerirá la instalación de Docker, y también sería más complejo, por lo que recomendamos esto a usuarios más experimentados.

## Ejecutar en la Nube

Si no quieres instalar Python localmente y tienes acceso a algunos recursos en la nube, una buena alternativa sería ejecutar el código en la nube. Hay varias maneras en que puedes hacer esto:

* Usar **[GitHub Codespaces](https://github.com/features/codespaces)**, que es un entorno virtual creado para ti en GitHub, accesible a través de una interfaz de navegador de VS Code. Si tienes acceso a Codespaces, solo tienes que hacer clic en el botón **Code** en el repositorio, iniciar un codespace y empezar a trabajar en poco tiempo.
* Usar **[Binder](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)**. [Binder](https://mybinder.org) ofrece recursos computacionales gratuitos proporcionados en la nube para personas como tú para probar código en GitHub. Hay un botón en la página principal para abrir el repositorio en Binder - esto debería llevarte rápidamente al sitio de Binder, que construirá un contenedor subyacente y comenzará una interfaz web de Jupyter para ti sin problemas.

> **Nota**: Para prevenir usos indebidos, Binder tiene acceso a algunos recursos web bloqueados. Esto puede impedir que parte del código funcione, especialmente el que descarga modelos y/o conjuntos de datos desde Internet público. Puede que necesites encontrar algunas soluciones alternativas. Además, los recursos computacionales proporcionados por Binder son bastante básicos, por lo que el entrenamiento será lento, especialmente en lecciones posteriores y más complejas.

## Ejecutar en la Nube con GPU

Algunas de las lecciones posteriores de este currículo se beneficiarían mucho del soporte GPU. El entrenamiento de modelos, por ejemplo, puede ser dolorosamente lento de otra manera. Hay algunas opciones que puedes seguir, especialmente si tienes acceso a la nube ya sea a través de [Azure for Students](https://azure.microsoft.com/free/students/?WT.mc_id=academic-77998-cacaste), o mediante tu institución:

* Crear una [Máquina Virtual de Ciencia de Datos](https://docs.microsoft.com/learn/modules/intro-to-azure-data-science-virtual-machine/?WT.mc_id=academic-77998-cacaste) y conectarte a ella a través de Jupyter. Luego puedes clonar el repositorio directamente en la máquina y comenzar a aprender. Las máquinas virtuales de la serie NC tienen soporte GPU.

> **Nota**: Algunas suscripciones, incluyendo Azure for Students, no proporcionan soporte GPU por defecto. Puede que tengas que solicitar núcleos GPU adicionales con una solicitud de soporte técnico.

* Crear un [Espacio de Trabajo Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) y luego usar la función de Notebooks allí. [Este video](https://azure-for-academics.github.io/quickstart/azureml-papers/) muestra cómo clonar un repositorio en un notebook de Azure ML y empezar a usarlo.

También puedes usar Google Colab, que viene con algo de soporte GPU gratuito, y subir Jupyter Notebooks allí para ejecutarlos uno por uno.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->