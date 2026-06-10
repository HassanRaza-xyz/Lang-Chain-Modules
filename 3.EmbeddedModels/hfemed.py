from langchain_huggingface import HuggingFaceEmbeddings
embed = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2",dimensions=20)
text = "My name is Hassan"
output = embed.embed_query(text)
print(len(output))
