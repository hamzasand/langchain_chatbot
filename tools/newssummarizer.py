from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults
load_dotenv()

search_tools = TavilySearchResults(max_results=5)
llm = ChatMistralAI(model = "mistral-small-2506")

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assitant who summarize the following 
    new into clear bullet points {new}
    """
)

chain = prompt | llm | StrOutputParser()
news_result = search_tools.run("Latest Pakistan news of 2026")
result = chain.invoke({"news": news_result})

print(result)