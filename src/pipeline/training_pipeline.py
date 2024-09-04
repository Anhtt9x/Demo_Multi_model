from src.components.data_transformation import load_index_from_storage
from src.components.model_trainer import retriever
from src.components.model_evaluation import plot_images

retriever_engine=load_index_from_storage("mixed_data").as_retriever(similariry_top_k=1, image_similarity_top_k=3)


query="can you tell me what is linear regression? explain equation of the multiple linear regression?"
imgs, text = retriever(retriever_engine=retriever_engine,query_str=query)

plot_images(images_path=imgs)