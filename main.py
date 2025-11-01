import langchain_helper as lh  # Importer le module langchain_helper
import streamlit as st  # importer streamlit pour créer l'interface utilisateur web

st.set_page_config(page_title="Pet Name Generator", page_icon="🐾")

st.title("🐾 Générateur de noms de pets")

# Entrées utilisateur dans la sidebar
animal_type = st.sidebar.selectbox(
    "C'est quoi votre animal ?", 
    ("chat", "chien", "vache", "hamster")
)

couleur = st.sidebar.text_input("Couleur de l'animal ?", placeholder="ex: orange, noir, blanc...")

# Bouton pour générer le nom
if st.sidebar.button("Générer un nom mignon pour mon pet 🎉"):
    if couleur.strip() == "":
        st.warning("⚠️ Veuillez entrer la couleur de l'animal")
    else:
        # Afficher un spinner pendant la génération
        with st.spinner("⏳ Génération en cours..."):
            try:
                # Appeler la fonction namePet du module langchain_helper
                name = lh.namePet(animal_type, couleur)
                
                # Afficher le résultat
                st.success(f"✅ Nom généré avec succès !")
                st.markdown(f"## 🎁 Voici un super nom pour votre {animal_type} {couleur} :")
                st.markdown(f"### **{name}**")
                
                # Ajouter un ballon et des emojis pour célébrer
                st.balloons()
                
            except Exception as e:
                st.error(f"❌ Erreur lors de la génération : {e}")

# Ajouter des informations dans la sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📝 Comment ça marche ?
1. Sélectionnez le type d'animal
2. Entrez la couleur
3. Cliquez sur le bouton
4. Obtenez un nom mignon ! 🎉
""")