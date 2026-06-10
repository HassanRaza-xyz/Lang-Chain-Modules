# from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

# my_llm = HuggingFacePipeline.from_model_id(
#     model_id= "meta-llama/Meta-Llama-3-8B-Instruct",
#     task= "text-generation",
#     pipeline_kwargs= {
#         "temperature" : 0.5,
#         "max_new_tokens" : 10
#     },
# )
# model = ChatHuggingFace(llm = my_llm)
# output = model.invoke("What is the Capital of Pakistan")
# print(output.content)

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os 
os.environ['HF_HOME'] = 'D:/huggingface_cache'
my_llm = HuggingFacePipeline.from_model_id(
    #locally downlaod krna pary ga isko 
    model_id= "meta-llama/Meta-Llama-3-8B-Instruct",
    task = "text_generation",
    pipeline_kwargs=dict(
        temperature=0.4,
        max_new_tokens= 40
    )

)
model = ChatHuggingFace(llm=my_llm)
output = model.invoke("What is Punjab")
print(output.content)