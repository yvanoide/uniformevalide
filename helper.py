from ultralytics import YOLO
import streamlit as st
import cv2
import settings

def charger_modele(chemin_modele):
    modele = YOLO(chemin_modele)
    return modele

def _afficher_frames_detectes_directives(conf, modele, st_frame, image, afficher_suivi=None):
    noms_classes = ["Casque", "Masque", "Pas de casque", "Pas de masque", "Pas de gilet de sécurité", "Personne", "Cône de sécurité", "Gilet de sécurité", "Machinerie", "Véhicule"]
    image = cv2.resize(image, (720, int(720*(3/4))))

    if afficher_suivi:
        resultat = modele.track(image, conf=conf, persist=True)
    else:
        resultat = modele.predict(image, conf=conf)

    # Vérifier la détection de 'Pas de casque' ou 'Pas de gilet de sécurité' et 'Personne'
    violation_securite_detectee = False
    personne_detectee = False
    for res in resultat:
        boites = res.boxes
        for boite in boites:
            classe = int(boite.cls[0])
            if noms_classes[classe] in ['Pas de casque', 'Pas de gilet de sécurité']:
                violation_securite_detectee = True
            if noms_classes[classe] == 'Personne':
                personne_detectee = True

    # Mettre du texte sur la caméra
    org = (50, 50)
    police = cv2.FONT_HERSHEY_SIMPLEX
    taille_police = 1
    if violation_securite_detectee and personne_detectee:
        couleur = (0, 0, 255)
        texte = 'Directives de sécurité non respectées'
    elif not violation_securite_detectee and not personne_detectee:
        couleur = (255, 255, 255)
        texte = 'Aucune personne détectée'
    else:
        couleur = (0, 255, 0)
        texte = 'Directives de sécurité respectées'
    epaisseur = 2
    image = cv2.flip(image, 1)
    cv2.putText(image, texte, org, police, taille_police, couleur, epaisseur)
    
    st_frame.image(image,
                   caption='Vidéo détectée',
                   channels="BGR",
                   use_column_width=True
                   )

def _afficher_frames_detectes_etiquettes(conf, modele, st_frame, image, afficher_suivi=None):

    image = cv2.resize(image, (720, int(720*(3/4))))
    image = cv2.flip(image, 1)

    if afficher_suivi:
        resultat = modele.track(image, conf=conf, persist=True)
    else:
        resultat = modele.predict(image, conf=conf)

    resultat_trace = resultat[0].plot()
    st_frame.image(resultat_trace,
                   caption='Vidéo détectée',
                   channels="BGR",
                   use_column_width=True
                   )


def jouer_webcam(conf, modele, type):
    source_webcam = settings.WEBCAM_PATH
    if st.sidebar.button('Démarrer la détection'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam, cv2.CAP_DSHOW)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success and type == 1:
                    _afficher_frames_detectes_directives(conf,
                                             modele,
                                             st_frame,
                                             image)
                elif success and type == 2:
                    _afficher_frames_detectes_etiquettes(conf,
                                             modele,
                                             st_frame,
                                             image)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Erreur de chargement de la webcam: " + str(e))
