Band Names Generator – Projet Docker

Génération aléatoire de noms de groupes de musique – Projet MyDigitalSchool

📚 Table des matières

Présentation

Architecture du projet

Prérequis

Installation

Lancer le projet en développement

Construire l’image pour la production

Structure du projet

Gestion des environnements

Liens utiles

Remarques

🎸 Présentation

Ce projet permet de générer aléatoirement 10 noms de groupes de musique au format :

The {adjective} {noun}


L’application :

Vérifie la connexion à une base MySQL

Génère les noms via des données stockées en base

Est entièrement conteneurisée (web + DB + admin DB)

Projet développé pour l’évaluation “Conteneurisation”.

🏗️ Architecture du projet
Service	Technologie	Rôle
web	Python / Flask	Logique métier + rendu HTML
db	MySQL	Stockage des adjectifs et noms
admin	Adminer	Interface pour consulter la base

Le tout orchestré avec Docker Compose.

🚀 Prérequis

Docker & Docker Compose

Git

Un terminal (WSL conseillé sous Windows)

⚙️ Installation

Cloner le projet :

git clone https://github.com/<ton-user>/docker-projet-l-raphael.git
cd docker-projet-l-raphael


Créer ton fichier .env :

cp .env.dist .env


Modifier les valeurs du .env si nécessaire :

MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=bandnames
MYSQL_USER=user
MYSQL_PASSWORD=password

▶️ Lancer le projet en développement
docker compose up --build


Le site est disponible ici :

👉 http://localhost:8085

Adminer ici :
👉 http://localhost:8086

📦 Construire l’image pour la production

Image nommée :

bandnamesgenerator:1.0.0


Commande :

docker build -t bandnamesgenerator:1.0.0 -f Dockerfile.web .

🗂️ Structure du projet
.
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   └── database.py
├── db/
│   └── init.sql
├── compose.yaml
├── Dockerfile.web
├── requirements.txt
├── .env.dist
├── .gitignore
└── README.md

🔄 Gestion des environnements
Environnement développement

Fichier .env local

Watch mode pour recharger le code

Ports exposés

Adminer activé

Environnement production

Pas d’Adminer

Variables d’environnement différentes

Image buildée (bandnamesgenerator:1.0.0)

Pas de watch mode

Base de données externe ou service cloud

🔗 Liens utiles

Docker Compose docs : https://docs.docker.com/compose/

Image MySQL officielle : https://hub.docker.com/_/mysql

Flask documentation : https://flask.palletsprojects.com/

💬 Remarques

Projet réalisé dans le cadre de l’évaluation de Conteneurisation.
N’hésitez pas à ouvrir une issue si vous souhaitez proposer des améliorations.

✅ 2. Comment mettre ton projet sur GitHub ? (Tutoriel simple)
1️⃣ Crée un dépôt GitHub

Va sur : https://github.com/new

Nom du dépôt : docker-projet-l-raphael

Public

Ne mets pas README → ton projet en contient déjà un

Create Repository
