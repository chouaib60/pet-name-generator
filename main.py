import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Force le rechargement du .env
load_dotenv(override=True)

# Vérifie que la clé est bien chargée
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ ERREUR : OPENAI_API_KEY n'est pas définie dans .env")
    sys.exit(1)
elif api_key.startswith("sk-proj-"):
    print("✅ Clé API trouvée et valide")
else:
    print("⚠️ Attention : La clé API ne semble pas valide")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def namePet(animal_type):
    llm = ChatOpenAI(temperature=0.9)
    
    prompt_template = PromptTemplate(
        input_variables=["animal_type"],
        template="I have a {animal_type} pet, give me some good names"
    )
    
    chain = prompt_template | llm | StrOutputParser()
    
    response = chain.invoke({"animal_type": animal_type})
    return response

if __name__ == "__main__":
    print(namePet("cat"))