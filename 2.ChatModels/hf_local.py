from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

my_llm = HuggingFacePipeline.from_model_id(
    model_id= "meta-llama/Llama-3.2-1B-Instruct",
    task= "text-generation",
    pipeline_kwargs= {
        "temperature" : 0.5,
        "max_new_tokens" : 10
    },
)
model = ChatHuggingFace(llm = my_llm)
output = model.invoke("What is the Capital of Pakistan")
print(output.content)