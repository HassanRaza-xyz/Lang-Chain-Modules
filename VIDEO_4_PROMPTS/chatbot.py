from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
chat_history = []
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
while True:
    
    user_input = input("You")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result =  model.invoke(chat_history)
    print("Ai",result.content)
    
