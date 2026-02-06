# Pipeline Machine Learning – Prédiction météorologique à court terme

## Présentation du projet
Ce projet présente la conception et l’implémentation d’un pipeline de Machine Learning complet en Python, appliqué à la prédiction de la température à court terme à partir de données météorologiques horaires.

L’objectif est de démontrer une approche structurée et reproductible, depuis l’ingestion des données jusqu’à leur préparation pour l’apprentissage automatique, dans une logique proche d’un environnement professionnel.

---

## Objectifs du projet
- Mettre en place un pipeline de données clair et reproductible
- Transformer une série temporelle en problème de régression supervisée
- Réaliser une analyse exploratoire approfondie
- Préparer des données exploitables pour le Machine Learning

---

## Données
Les données utilisées sont des données météorologiques horaires (température, pression, date et heure).

Pour des raisons de bonnes pratiques et de volume, les données brutes ne sont pas versionnées directement dans le dépôt. Le pipeline permet toutefois de charger et traiter les données localement.

---

## Méthodologie

1. Ingestion et nettoyage des données
2. Feature engineering (création de variables retardées)
3. Analyse exploratoire des données (EDA)
4. Construction des jeux de données X et y
5. Archivage et traçabilité des données

La variable cible correspond à la température à l’instant t+1.

---

## Analyse exploratoire des données

### Évolution temporelle de la température
Cette visualisation met en évidence les variations et tendances de la température au cours du temps.

![Évolution temporelle de la température](images/temperature_t1.png)

---

### Distribution de la température cible
La distribution de la température à t+1 montre une répartition continue, sans valeurs aberrantes majeures.

![Distribution de la température](images/distribution_temp.png)

---

### Relation température t-1 / température t+1
Le graphique ci-dessous met en évidence une forte corrélation entre la température passée et la température future.

![Relation température t-1 et t+1](images/scatter_temp.png)

---

## Résultats et interprétation
L’analyse exploratoire montre que la température à l’instant t-1 est fortement corrélée à la température à t+1, ce qui confirme la pertinence de l’approche basée sur des variables temporelles retardées.

La pression atmosphérique apporte une information complémentaire mais moins déterminante.

---

## Technologies utilisées
- Python
- Pandas, NumPy
- Matplotlib
- Scikit-learn
- SQLite
- Jupyter Notebook
- Git / GitHub

---

## Organisation du projet
- Notebook principal pour le pipeline et l’analyse
- Séparation claire entre données, features et code
- Archivage des données pour assurer la reproductibilité
- Versionnement avec Git

---

## Perspectives d’amélioration
- Intégration de modèles de régression avancés
- Ajout de métriques d’évaluation quantitatives
- Automatisation complète du pipeline
- Extension à d’autres horizons de prédiction

---

## Auteur
Nassim Gastlin  
Master of Science – Data Management & Artificial Intelligence
