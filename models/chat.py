from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI( 
    model = "mistral-large-latest",
    temperature = 0.2)

human = input("Entern your message")
response = model.invoke(human)
print(response.content)