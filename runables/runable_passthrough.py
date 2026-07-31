from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

code_prompt = ChatPromptTemplate.from_messages([
    ("system","You are a code generator in python"),
    ("human","{topic}")
])

explain_code= ChatPromptTemplate.from_messages([
    ("system","You are helpful assistnt who explain code in simple terms"),
    ("human","Explain this code in simple words:\n{code}")
])

seq = code_prompt | model | parser
seq2 = RunnableParallel(
    {"code": RunnablePassthrough(),
     "explanation": explain_code | model | parser}
)

chain = seq | seq2
result = chain.invoke({"topic": "Please write a code of palindrome in python"})
print(result['code'])
print(result['explanation'])