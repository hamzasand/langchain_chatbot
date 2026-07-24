from langchain_community.retrievers import ArxivRetriever

retriver = ArxivRetriever(
    load_max_docs=2,
    load_all_available_meta=True
)

docs = retriver.invoke("large language models")

# print results
for i, doc in enumerate(docs):
    print(f"\nResult {i+1}")
    print("Title:", doc.metadata.get("Title"))
    print("Authors:", doc.metadata.get("Authors"))
    print("Summary:", doc.page_content)  # print first 500 characters