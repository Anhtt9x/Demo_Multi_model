from llama_index.core.response.notebook_utils import display_source_node
from llama_index.core.schema import ImageNode
from src.components.data_transformation import load_index_from_storage

def retriever(retriever_engine,query_str):
    retrival_result = retriever_engine.retrieve(query_str)

    retrieved_text = []
    retrieved_image = []

    for res_node in retrival_result:
        if  isinstance(res_node.node, ImageNode):
            retrieved_image.append(res_node.node.metadata['file_path'])

        else:
            display_source_node(res_node,source_length=200)
            retrieved_text.append(res_node.text)

    return retrieved_image,retrieved_text



if __name__ == "__main__":

    query="can you tell me what is linear regression? explain equation of the multiple linear regression?"
    retriever_engine = load_index_from_storage("mixed_data").as_retriever(similarity_top_k=1,image_similariry_top_k=3)
    print(retriever(retriever_engine=retriever_engine,query_str=query)) 