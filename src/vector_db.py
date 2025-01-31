import faiss
import numpy as np
import pickle

class VectorDB:
    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []
    
    def add_embeddings(self, embeddings, metadata):
        self.index.add(embeddings)
        self.metadata.extend(metadata)
    
    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(
            np.array([query_embedding]).astype('float32'), 
            top_k
        )
        return [self.metadata[idx] for idx in indices[0]]
    
    def save(self, index_path, metadata_path):
        faiss.write_index(self.index, index_path)
        with open(metadata_path, 'wb') as f:
            pickle.dump(self.metadata, f)
    
    def load(self, index_path, metadata_path):
        self.index = faiss.read_index(index_path)
        with open(metadata_path, 'rb') as f:
            self.metadata = pickle.load(f)
