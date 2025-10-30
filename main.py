import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Nouvel import pour LangChain >= 0.1.0



load_dotenv ()  # Charger les variables d'environnement (comme OPENAI_API_KEY)

def namePet():
	LLM = ChatOpenAI(temperature=0.9)  # Utilisation de ChatOpenAI pour LangChain >= 0.1.0
	# la température controle la créativité des réponses généréés par le modèle
	# Une température plus élevée (proche de 1) rend les réponses plus créatives, 
	# tandis qu'une température plus basse (proche de 0) les rend plus conservatrices. 


# invoke est la méthode correcte pour appeler le modèle que j'ai 
	names = LLM.invoke("quels sont les meilleurs noms au maroc pour un chat ?") 
	return names
if __name__ == "__main__":
	print(namePet())