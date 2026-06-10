# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()
# embeddig = GoogleGenerativeAIEmbeddings(model ="models/gemini-embedding-001" ,dimensions= 32)
# output = embeddig.embed_query("Islamabad is the capital of Pakistan")
# print(str(output))
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# print("Checking available embedding models...")
# for m in genai.list_models():
#     if 'embedContent' in m.supported_generation_methods:
#         print(f"Model Name: {m.name}")
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
      dimensions=32)
document=[
    "i am hassan",
    "my bro is ali",
    "i am in kfueit"
]
output = embedding.embed_documents(document)
print(str(output))