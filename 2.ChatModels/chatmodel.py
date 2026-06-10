from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash") #you can add like temperature and max_compeletion_tokens 
output = model.invoke("Suggest me 5 business names")
print(output.content)