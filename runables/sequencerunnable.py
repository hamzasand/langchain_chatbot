from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1.set prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {Topic} in language in simple and under 20 words"
)

# 2.set model
model = ChatMistralAI(model ="mistral-small-2506")

# 3.outputparser
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke("Machine Learning")
print(result)