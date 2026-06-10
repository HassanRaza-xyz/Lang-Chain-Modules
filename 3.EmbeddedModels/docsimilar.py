# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# load_dotenv()
# embeding = GoogleGenerativeAIEmbeddings (model = "models/gemini-embedding-001", dimensions = 32)
# docuemnt = [
#     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",

# "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",

# "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",

# "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",

# "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",

# ]
# quest = "Tell me About Rohit Sharma "

# output = embeding.embed_documents(docuemnt)
# u_input = embeding.embed_query(quest)   
# similar =cosine_similarity([u_input],output)[0]

# sorted_list =sorted(list(enumerate(similar)),key = lambda x:x [1])
# index , score = sorted_list[-1]
# print(quest)
# print(docuemnt[index])
# print("Similarity score is ", score)


# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# load_dotenv()
# model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", dimensions=200)
# docuemnt = [
# "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",

# "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",

# "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",

# "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",

# "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",

# ]
# query = "tell me about sachin"


# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from dotenv import load_dotenv
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# load_dotenv()
# Embded = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001", dimensions = 32)

# docs = [
#     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",

#  "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",

#  "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",

#  "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",

# "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",

# ]

# question = "Who is Rohit sharma"

# user_input = Embded.embed_query(question)
# Document = Embded.embed_documents(docs)
# similarity = cosine_similarity([user_input],Document)[0]
# output =sorted(list(enumerate(similarity)),key = lambda x:x[1] )
# index, score = output[-1]
# print(question)
# print(docs[index])
# print (score)


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
model = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001",dimensions=200)
docuemnt = [
"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",

"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",

"Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",

"Rohit Sharma is known for his elegant batting and record-breaking double centuries.",

"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",

]
query = "tell me about sachin"
doc_embedding = model.embed_documents(docuemnt)
query_embed = model.embed_query(query)
score = cosine_similarity([query_embed] , doc_embedding)[0]
print("score",score)
sorted_score = sorted(list(enumerate(score)),key = lambda x:x[1])
print("sorted score", sorted_score)
best_match = sorted_score[-1]
index = best_match[0]
similar = best_match[1]
print(query)
print(docuemnt[index])
print(similar)