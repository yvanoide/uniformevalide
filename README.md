# Application de Détection de Casque/Gilet de Chantier

## Contexte du Projet

Les caméras de surveillance et de sécurité sont devenues un outil essentiel pour garantir la sécurité dans diverses applications. Notre entreprise se spécialise dans le développement de solutions technologiques pour les caméras de surveillance et de sécurité. Dans le cadre de ce projet, nous visons à développer une application web basée sur l'intelligence artificielle (IA) capable de détecter et de localiser la présence de casques et de gilets de chantier dans une vidéo.

L'application que nous développons doit être en mesure d'activer la caméra de l'ordinateur et d'afficher les résultats de la détection en temps réel sur la vidéo. De plus, l'application doit être capable de générer un message d'alerte en dehors de la vidéo si une personne ne porte pas son casque ou son gilet de chantier.

## Objectif

L'objectif principal de ce projet est de créer une application web robuste capable de détecter et de localiser la présence de casques et de gilets de chantier dans une vidéo en temps réel. Les points clés de notre mission sont les suivants :

1. **Détection d'Équipements de Sécurité** : Développer un algorithme d'IA capable de détecter la présence ou l'absence de casques et de gilets de chantier dans une vidéo.

2. **Interface Web Conviviale** : Créer une interface web conviviale qui affiche la vidéo en temps réel et les résultats de la détection.

3. **Gestion des Alertes** : Générer un message d'alerte sur la page web si une personne ne porte pas son casque ou son gilet de chantier.

4. **Vérification de l'Uniforme** : Afficher un message "Uniforme vérifié" si toutes les détections sont conformes, sinon afficher "Uniforme non vérifié".

## Fonctionnalités

- Détection en temps réel de la présence de casques et de gilets de chantier dans une vidéo.
- Affichage de la vidéo en temps réel avec les résultats de la détection.
- Génération d'un message d'alerte en cas de non-port d'un casque ou d'un gilet de chantier.
- Message "Uniforme vérifié" si toutes les détections sont conformes, sinon "Uniforme non vérifié".

## Prérequis

Avant de commencer à travailler sur ce projet, assurez-vous de disposer des éléments suivants :

- **Environnement de Développement** : Un environnement de développement Python 3.x configuré sur votre ordinateur.

- **Bibliothèques Python** : Installez les bibliothèques Python nécessaires, que vous pouvez trouver dans le fichier `requirements.txt`.

- **Caméra PC** : Votre ordinateur doit être équipé d'une caméra pour la détection en temps réel.

## Arborescence du Projet

Organisez le projet sur votre machine selon la structure suivante :

```
Yolo/
│ 
├─── assets/
│   └─── pic1.png
│
├─── images/
│   ├─── worker.png
│   └─── worker_detected.png
│
├─── weights/
│   ├─── best.pt
│   ├─── yolo8n.pt
│   ├─── yolov8n-cls.pt
│   └─── yolov8n-seg.pt
│
├─── .gitignore
├─── README.md
├─── app.py
├─── helper.py
├─── settings.py
└───  requirements.txt

```

## Installation et Utilisation

Pour mettre en place et utiliser l'application de détection de casque/gilet de chantier, suivez ces étapes :

1. Clonez ce référentiel sur votre ordinateur.

2. Installez les dépendances requises en exécutant la commande suivante :
   ```bash
   pip install -r app/requirements.txt
   ```

3. Lancez l'application web en exécutant :
   ```bash
   streamlit run app.py
   ```

4. Ouvrez un navigateur web et accédez à l'URL suivante : `http://localhost:5001` (ou l'adresse qui sera affichée au moment du lancement de l'application) pour utiliser l'application.

## Contributions

Merci au contributeurs de ce projet ! 