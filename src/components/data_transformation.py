
from llama_index.core import SimpleDirectoryReader, StorageContext, Settings
from llama_index.vector_stores.lancedb import LanceDBVectorStore
from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from PIL import Image
from typing import List
import numpy as np

# Lớp CLIPEmbedding không kế thừa từ Pydantic


def load_index_from_storage(directory_path: str) -> MultiModalVectorStoreIndex:
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2",trust_remote_code=True)  # Sử dụng lớp CLIPEmbedding tùy chỉnh

    Settings.chunk_size = 512

    text_store = LanceDBVectorStore(uri="lancedb", table_name="text_collection")
    image_store = LanceDBVectorStore(uri="lancedb", table_name="image_collection")

    storage_context = StorageContext.from_defaults(vector_store=text_store, image_store=image_store)

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = MultiModalVectorStoreIndex.from_documents(documents=documents, storage_context=storage_context)

    return index 
