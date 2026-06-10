from langchain_huggingface import HuggingFaceEmbeddings
embed = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")
text = "My name is Hassan"
output = embed.embed_query(text)
print(str(output))
