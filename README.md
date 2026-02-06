# pipeline-meteo-prd
Pipeline Machine Learning – Prédiction météorologique à court terme
Description du projet

Ce projet présente la conception et l’implémentation d’un pipeline de Machine Learning complet en Python, appliqué à la prédiction de la température à court terme à partir de données météorologiques horaires. L’objectif est de démontrer une approche structurée et reproductible, allant de l’ingestion des données à leur préparation pour l’apprentissage automatique.

Le projet met l’accent sur la qualité du pipeline et la logique de traitement des données plutôt que sur l’optimisation d’un modèle spécifique. Il s’inscrit dans une démarche proche de celle rencontrée en environnement professionnel, notamment en data analysis et en machine learning appliqué.

Objectifs

Mettre en place un pipeline de traitement de données structuré et reproductible

Transformer une série temporelle en un problème de régression supervisée

Réaliser une analyse exploratoire afin de comprendre les relations entre variables

Préparer des jeux de données exploitables pour l’entraînement de modèles de Machine Learning

Données

Les données utilisées sont des données météorologiques horaires (température, pression, date/heure).
Pour des raisons de volume et de bonnes pratiques, les fichiers de données ne sont pas versionnés directement dans le dépôt. Le pipeline permet toutefois de charger et de traiter les données à partir de sources externes ou de fichiers fournis localement.

Méthodologie

Le pipeline est organisé selon les étapes suivantes :

Ingestion et nettoyage des données

Feature engineering avec création de variables retardées (lag features)

Analyse exploratoire des données (EDA) à l’aide de visualisations

Construction des jeux de données d’entrée (X) et de sortie (y)

Archivage et stockage intermédiaire pour assurer la traçabilité

La température à l’instant t+1 est utilisée comme variable cible, tandis que la température passée et d’autres variables météorologiques servent de variables explicatives.

Résultats principaux

L’analyse exploratoire met en évidence une forte corrélation entre la température à t-1 et la température à t+1, ce qui confirme la pertinence de l’approche basée sur des variables temporelles retardées. Les résultats obtenus constituent une base solide pour l’intégration ultérieure de modèles de régression et d’étapes d’évaluation plus avancées.

Technologies utilisées

Python

Pandas, NumPy

Matplotlib / Seaborn

Scikit-learn

SQLite

Jupyter Notebook

Git / GitHub

Organisation du projet

Notebook principal pour l’exploration et le pipeline

Séparation des données brutes, des données transformées et du code

Archivage des données pour assurer la reproductibilité

Utilisation de Git pour le versionnement et le travail collaboratif

Perspectives d’amélioration

Intégration de modèles de régression plus avancés

Ajout de métriques d’évaluation quantitatives

Automatisation complète du pipeline (scripts ou orchestration)

Extension à d’autres variables météorologiques ou horizons de prédiction

Auteur

Projet réalisé par Nassim Gastlin
Master of Science – Data Management & Artificial Intelligence
