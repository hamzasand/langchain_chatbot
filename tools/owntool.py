from langchain.tools import tool


@tool
def get_greetings(name : str) -> str:
    """This toll generate greetings for a user."""
    return f"Hello {name}, welcome to Ai world"

result = get_greetings.invoke({"name":"Hamza"})
print(result)

print(get_greetings.name)
print(get_greetings.description)
print(get_greetings.args)