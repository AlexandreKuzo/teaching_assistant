# Un assistant conversationnel avec Streamlit & OpenAI

Cette petite app est un chatbot qui s'appuie sur l'API OpenAI et le modèle "text-davinci-003". On simule une conversation avec un automate qui répond à vos questions. 
[Streamlit](https://streamlit.io/) permet rapidement d'avoir une interface friendly et rapide à déployer en ligne.

## Contenu du dossier
- Le fichier app.py qui contient l'application en elle-même. 
- Le fichier de dépendances requirements.txt.

### "Packages" et matériel requis

- Pour utiliser l'app, le nécessaire est dans requirements.txt ; la commande ``pip install -r requirements.txt`` installera l'ensemble.

### Installation et démarrage (consignes adaptées pour utilisateurs/utilisatrices de Mac)

Etape 1: clonez le projet.

Etape 2: naviguez dans le dossier avec la commande ``cd teaching_assistant`` puis installez dans le répertoire un environnement virtuel (avec [pipenv](https://docs.python-guide.org/dev/virtualenvs/), ou avec [venv et pip](https://docs.python.org/fr/3/library/venv.html)).

Etape 3: activez l'environnement virtuel avec la commande appropriée : ``source env/bin/activate`` 

Etape 4 : installez au projet les packages requis ; ceux-ci sont fournis dans le fichier ``requirements.txt`` La commande suivante le fera : ``pip install -r requirements.txt``.

## Executer le projet en local

Dans le répertoire teaching_assistant, tapez depuis le Terminal ou votre éditeur de texte la commande ``streamlit run app.py``; si votre environnement virtuel est bien activé et que vous êtes au bon endroit, l'application se lance, et le tour est joué !

L'app s'ouvre dans votre navigateur à l'adresse http://localhost:8501

## Auteur
* **Alexandre Kuzo**  [@alexandrekuzo](https://github.com/AlexandreKuzo)