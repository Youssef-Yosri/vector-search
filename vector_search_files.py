def search():
    from transformers import BertModel, BertTokenizer
    import torch
    from pymongo import MongoClient
    import numpy as np
    import faiss

    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
    model = BertModel.from_pretrained('bert-large-uncased')

    def get_embedding(query):
        inputs = tokenizer(query, return_tensors='pt', truncation=True, padding=True)

        with torch.no_grad():
            outputs = model(**inputs)

        last_hidden_state = outputs.last_hidden_state

        pooled_output = last_hidden_state.mean(dim=1)
        
        return pooled_output

    query = input("Enter your search query: ")
    query_vector = get_embedding(query)
    
    print("Embedding vector:", query_vector)

    client = MongoClient('mongodb://localhost:27017/')
    db = client['VectorDBPython']
    collection = db['CVs']

    vectors = []
    metadata = []
    for doc in collection.find():
        vectors.append(doc['embedding'])
        metadata.append(doc['metadata'])
    
    vectors = np.array(vectors, dtype='float32')
    
    index = faiss.read_index('faiss_index.index')

    norm_query_vector = np.linalg.norm(query_vector)
    print(f"Initial norm of the query vector: {norm_query_vector}")
    query_vector /= np.linalg.norm(query_vector)
    
    norm_query_vector_after = np.linalg.norm(query_vector)
    print(f"Norm of the query vector after normalization: {norm_query_vector_after}")
    
    distances, indices = index.search(query_vector, k=1)
    
    print("Indices:", indices)
    print("Distances (inner product):", distances)
    
    for idx in indices[0]:
        print("-------------------------------------------------------------------------")
        metadata_item = metadata[idx]
        for key, value in metadata_item.items():
            print(f"{key}: {value}")
        print("-------------------------------------------------------------------------")

if __name__ == "__main__":
    search()
