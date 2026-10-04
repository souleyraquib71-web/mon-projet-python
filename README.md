# RodiumAI SDK Python – Exercice 3

Ce projet est un script Python interactif utilisant le SDK `rodiumai` pour générer du texte, des images et des vidéos avec l'API RodiumAI.
Il permet de naviguer entre les trois étapes et de rester, revenir en arrière, passer à l'étape suivante ou quitter le programme.

## Installation

Le projet utilise **Python 3.13.0**.

Installer les dépendances avec :

```bash
pip install -r requirements.txt
```


## Configuration du `.env`

Copier le fichier `.env.example` vers `.env` :

```bash
cp .env.example .env
```

Puis ajouter votre clé API RodiumAI dans le fichier `.env` :

```env
RODIUMAI_API_KEY=votre_cle_api
```

Ne partagez jamais votre fichier `.env` et ne publiez pas votre clé API sur GitHub.

## Lancer le script

Exécuter la commande suivante :

```bash
python main.py
```

Le script propose trois étapes :

1. Chat conversationnel
2. Génération d'image
3. Génération de vidéo

Les commandes disponibles sont :

* `r` : rester sur l'étape actuelle
* `s` : passer à l'étape suivante
* `b` : revenir à l'étape précédente
* `q` : quitter le programme
