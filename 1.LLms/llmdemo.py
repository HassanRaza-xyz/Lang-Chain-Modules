from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model= "gemini-2.5-flash", temperature=0)

output = llm.invoke("Suggest me 5 best business ideas")
print(output.content)