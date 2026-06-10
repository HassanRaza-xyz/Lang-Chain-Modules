# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from dotenv import load_dotenv
# load_dotenv()
# my_llm = HuggingFaceEndpoint(
#   repo_id = "meta-llama/Llama-3.2-1B-Instruct",
#   task= "text-generation"
#  )
# model = ChatHuggingFace(llm=my_llm)
# oytput = model.invoke("What is the capital of Pakistan")
# print(oytput.content)

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
my_llm = HuggingFaceEndpoint (
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct",
    task = "text-generation"
)
model = ChatHuggingFace(llm=my_llm)
output = model.invoke("What is Punjab")
print(output.content)