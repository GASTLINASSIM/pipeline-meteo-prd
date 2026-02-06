# Pipeline Machine Learning – Prédiction météorologique à court terme

## Présentation du projet
Ce projet consiste en la conception et l’implémentation d’un pipeline de Machine Learning complet en Python, appliqué à la prédiction de la température à court terme à partir de données météorologiques horaires. Il met l’accent sur la structuration du pipeline, la reproductibilité et les bonnes pratiques en Data Science.

---

## Objectifs
- Construire un pipeline de données clair et reproductible
- Transformer une série temporelle en un problème de régression supervisée
- Réaliser une analyse exploratoire pour comprendre les relations entre variables
- Préparer des jeux de données exploitables pour l’apprentissage automatique

---

## Données
Les données utilisées sont des données météorologiques horaires (température, pression, date/heure).  
Les fichiers de données ne sont pas versionnés directement dans le dépôt afin de respecter les bonnes pratiques liées au volume et à la gestion des données.

---

## Méthodologie
Le pipeline est structuré selon les étapes suivantes :

1. Ingestion et nettoyage des données  
2. Feature engineering avec création de variables temporelles retardées  
3. Analyse exploratoire des données  
4. Construction des jeux de données d’entrée (X) et de sortie (y)  
5. Archivage et traçabilité des données  

La variable cible correspond à la température à l’instant t+1.

---

## Résultats
L’analyse exploratoire met en évidence une forte corrélation entre la température passée et la température future, confirmant la pertinence de l’approche basée sur des variables temporelles. Ces résultats constituent une base solide pour l’intégration ultérieure de modèles de régression plus avancés.

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
Le projet est organisé de manière à séparer clairement le code, les données et les étapes de traitement, dans une logique proche d’un environnement professionnel et collaborative.

---

## Auteur
06/02/2026
Nassim Gastli  
Bilel Sahnoun
Master of Science 2 – Data Management & Artificial Intelligence, ECE Paris, France
