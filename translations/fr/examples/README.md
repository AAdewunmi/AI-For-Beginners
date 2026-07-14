# Exemples d'IA adaptés aux débutants

Bienvenue ! Ce répertoire contient des exemples simples et autonomes pour vous aider à démarrer avec l'IA et l'apprentissage automatique. Chaque exemple est conçu pour être accessible aux débutants avec des commentaires détaillés et des explications étape par étape.

## 📚 Aperçu des exemples

| Exemple | Description | Difficulté | Prérequis |
|---------|-------------|------------|---------------|
| [Hello AI World](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/01-hello-ai-world.py) | Votre premier programme d'IA - reconnaissance de motifs simple | ⭐ Débutant | Bases de Python |
| [Simple Neural Network](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/02-simple-neural-network.py) | Construisez un réseau de neurones à partir de zéro | ⭐⭐ Débutant+ | Python, mathématiques de base |
| [Image Classifier](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/03-image-classifier.ipynb) | Classifiez des images avec un modèle pré-entraîné | ⭐⭐ Débutant+ | Python, numpy |
| [Text Sentiment](https://github.com/microsoft/AI-For-Beginners/blob/main/examples/04-text-sentiment.py) | Analysez le sentiment d'un texte (positif/négatif) | ⭐⭐ Débutant+ | Python |

## 🚀 Pour commencer

### Prérequis

Assurez-vous d'avoir Python installé (3.8 ou plus recommandé). Installez les packages nécessaires :

```bash
# Pour les scripts Python
pip install numpy

# Pour les notebooks Jupyter (classificateur d’images)
pip install jupyter numpy pillow tensorflow
```

Ou utilisez l'environnement conda du cursus principal :

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Exécution des exemples

**Pour les scripts Python (.py) :**
```bash
python 01-hello-ai-world.py
```

**Pour les notebooks Jupyter (.ipynb) :**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Parcours d'apprentissage

Nous recommandons de suivre les exemples dans l'ordre :

1. **Commencez par "Hello AI World"** - Apprenez les bases de la reconnaissance de motifs
2. **Construisez un réseau de neurones simple** - Comprenez le fonctionnement des réseaux de neurones
3. **Essayez le classificateur d'images** - Découvrez l'IA en action avec des images réelles
4. **Analysez le sentiment du texte** - Explorez le traitement du langage naturel

## 💡 Conseils pour les débutants

- **Lisez attentivement les commentaires dans le code** - Ils expliquent ce que fait chaque ligne
- **Expérimentez !** - Essayez de modifier les valeurs et voyez ce qui se passe
- **Ne vous inquiétez pas de tout comprendre** - L'apprentissage prend du temps
- **Posez des questions** - Utilisez le [forum de discussion](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Prochaines étapes

Après avoir terminé ces exemples, explorez le cursus complet :
- [Introduction à l'IA](../lessons/1-Intro/README.md)
- [Réseaux de neurones](../lessons/3-NeuralNetworks/README.md)
- [Vision par ordinateur](../lessons/4-ComputerVision/README.md)
- [Traitement du langage naturel](../lessons/5-NLP/README.md)

## 🤝 Contribution

Ces exemples vous ont été utiles ? Aidez-nous à les améliorer :
- Signalez les problèmes ou suggérez des améliorations
- Ajoutez plus d'exemples pour débutants
- Améliorez la documentation et les commentaires

---

*N'oubliez pas : Tout expert a un jour été débutant. Bon apprentissage ! 🎓*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->