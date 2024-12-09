import streamlit as st
import bcrypt
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate

# Création du dictionnaire d'identifiants
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

# Afficher le formulaire de connexion
authentication_status = authenticator.login()

if authentication_status is not None:
    name = lesDonneesDesComptes["usernames"].get("utilisateur", {}).get("name", "utilisateur")
    username = "utilisateur"


if authentication_status:
    authenticator.logout("Déconnexion", "sidebar")
    st.sidebar.write(f"Bienvenue {name}")

        # Création de la barre de navigation
menu = st.sidebar.radio("Navigation", ["Accueil", "Les photos de mon chat"])

if menu == "Accueil":
    st.title("Bienvenue sur ma page")
    st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS32SVmd_cMHBXsFvtRnww7hXkekTULnbg46g&s"
        )
elif menu == "Les photos de mon chat":
    st.title("Bienvenue dans l'album de mon chat")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYHzmTgYog6eZY5J3-PLu3At_v35k75q9n7Q&s")
    with col2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5xJj2eY0CRT5Wkf-XklUtNd2t2dtJVivThA&s")
    with col3:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKdFRNhrGxUwL5I2zpLgyNtF_pJBWjo0uy_A&s")

elif authentication_status is False:
    st.error("Le nom d'utilisateur ou mot de passe est incorrect")
elif authentication_status is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
