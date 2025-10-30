import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

# Charger les variables d'environnement
load_dotenv()

def namePet(animal_type):
    # Vérification de la clé API
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"🔑 Clé API chargée: {'Oui' if api_key else 'Non'}")
    
    if not api_key:
        return "❌ ERREUR: OPENAI_API_KEY non trouvée dans .env"
    
    try:
        # Initialisation du modèle
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.9,
            api_key=api_key
        )
        
        # Prompt template
        prompt_template = PromptTemplate(
            input_variables=["animal_type"],
            template="I have a {animal_type} pet. Suggest 5 good names for it."
        )
        
        # Création de la chaîne
        name_chain = LLMChain(llm=llm, prompt=prompt_template)
        
        # Exécution
        response = name_chain.run({"animal_type": animal_type})
        return response
        
    except Exception as e:
        return f"❌ Erreur: {str(e)}"

if __name__ == "__main__":
    print("🚀 Test de l'application...")
    result = namePet("cat")
    print("🐾 Résultat:")
    print(result)