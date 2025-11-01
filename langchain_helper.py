import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable

# Charger les variables d'environnement (comme GOOGLE_API_KEY)
load_dotenv()

def namePet(animal_type, couleur):
    """Génère un nom de pet en fonction du type d'animal et de la couleur"""
    
    # Initialiser le modèle Google Generative AI
    LLM = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9)
    
    # Appliquer les prompt templates
    prompt_template = PromptTemplate(
        input_variables=["animal_type", "couleur"],
        template="J'ai un {animal_type} de couleur {couleur}, donne-moi un bon nom mignon pour mon pet. Donne uniquement le nom, sans explication."
    )
    
    # Appliquer la chaîne pour combiner le prompt template et le modèle IA
    # LLM est une instance du modèle ChatGoogleGenerativeAI
    # prompt_template est une instance de PromptTemplate
    name_chain = prompt_template | LLM
    
    # Générer la réponse
    response = name_chain.invoke({"animal_type": animal_type, "couleur": couleur})
    
    return response.content

# Exemple d'utilisation
if __name__ == "__main__":
    print("🐾 Générateur de noms de pets avec Google Generative AI\n")
    
    # Exemple 1
    animal_type = "chat"
    couleur = "orange"
    print(f"Génération d'un nom pour: {animal_type} {couleur}")
    print("-" * 40)
    result = namePet(animal_type, couleur)
    print(f"✅ Nom généré: {result}\n")
    
    