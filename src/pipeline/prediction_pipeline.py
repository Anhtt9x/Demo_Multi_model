from llama_index.multi_modal_llms.gemini import GeminiMultiModal
import os
from dotenv import load_dotenv
from src.components.model_trainer import retriever
from src.components.data_transformation import load_index_from_storage
from llama_index.core.readers import SimpleDirectoryReader
from src.components.data_ingestion import metadata
import json

load_dotenv()

query_str="can you tell me what is linear regression and equation of linear regression?"
retriever_engine = load_index_from_storage("mixed_data").as_retriever(similarity_top_k=1,image_similariry_top_k=3)
imgs, text = retriever(retriever_engine=retriever_engine,query_str=query_str)

qa_tmpl_str=(
    "Based on the provided information, including relevant images and retrieved context from the video, \
    accurately and precisely answer the query without any additional prior knowledge.\n"

    "---------------------\n"
    "Context: {context_str}\n"
    "Metadata for video: {metadata_str} \n"

    "---------------------\n"
    "Query: {query_str}\n"
    "Answer: "
)

metadata_str = json.dumps(metadata)
context_str = "".join(text)
image_documents = SimpleDirectoryReader(input_files=imgs).load_data()

google_api_key = os.getenv('GOOGLE_API_KEY')
llm = GeminiMultiModal(api_key=google_api_key,model_name="models/gemini-1.5-pro",max_tokens=1500)

response = llm.complete(
    prompt=qa_tmpl_str.format(context_str=context_str,query_str=query_str,metadata_str=metadata_str),
    image_documents=image_documents
)

print(response.text)