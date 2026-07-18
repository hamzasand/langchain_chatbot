from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.3)

print("Select your mode:")
print("Press 1 for Angry mode")
print("Press 2 for Happy mode")
print("Press 1 for Funny mode")
choice = int(input("Please enter you mode:"))

if choice == 1:
    mode = "You act as angry bot and repy each answer in angry mode"
elif choice == 2:
    mode ="You act as happy bot and reply in happy way."
elif choice ==3:
    mode ="You act as funny bot and reply in funny way"

messages =[
    SystemMessage(content=mode)
]

print("_____If you want exit enter exit_____")
while True:
    prompt = input("You:")
    messages.append(HumanMessage(content=prompt))
    if prompt =="exist":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:",response.content)

print(messages)