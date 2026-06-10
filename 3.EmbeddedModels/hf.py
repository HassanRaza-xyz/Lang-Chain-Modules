from langchain_huggingface import HuggingFaceEmbeddings
embed = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")
text = "I am  a student"
output = embed.embed_query(text)
print(len(output))
