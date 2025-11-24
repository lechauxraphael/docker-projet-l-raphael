# Band Names Generator – Projet Docker

Génération aléatoire de noms de groupes de musique – Projet MyDigitalSchool.

---

## Présentation
Cette application permet de générer 10 noms de groupes de musique aléatoires au format :

{adjective}{noun}

Fonctionnalités :
- Vérifie la connexion à une base MySQL.
- Génère les noms à partir des données stockées en base.
- Conteneurisée avec Docker Compose (web + base de données + interface admin).

---

## Architecture
| Service | Technologie | Rôle |
|---------|------------|-----|
| web     | Python/Flask | Logique métier + rendu HTML |
| db      | MySQL       | Stockage des adjectifs et noms |
| admin   | Adminer     | Interface pour consulter la base |

---

## Prérequis
- Docker & Docker Compose
- Git
- Terminal (WSL conseillé sous Windows)

---

## Installation
1. Cloner le projet :
---bash
   
git clone https://github.com/lechauxraphael/docker-projet-l-raphael.git
cd docker-projet-l-raphael

3. Créer le fichier .env à partir du fichier .env.dist :
   cp .env.dist .env

4. Modifier les valeurs si nécéssaire:
  Modifier les valeurs si nécessaire :
    DB_ROOT_PASSWORD=root
    DB_NAME=bandnames
    DB_USER=banduser
    DB_PASSWORD=bandpass

Lancer le projet
  docker compose up --build


Site web : http://localhost:8085

Adminer : http://localhost:8086

Construire l’image pour la production

Image nommée bandnamesgenerator:1.0.0 :

docker build -t bandnamesgenerator:1.0.0 -f Dockerfile.web .

Structure du projet

├── app/

│   ├── templates/index.html

│   ├── app.py

│   └── database.py

├── db/init.sql

├── compose.yaml

├── Dockerfile.web

├── requirements.txt

├── .env.dist

├── .gitignore

└── README.md  
