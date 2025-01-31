from embedder import Embedder
from vector_db import VectorDB

class QueryHandler:
    def __init__(self, index_path='embeddings/faiss_index.idx', metadata_path='embeddings/metadata.pkl'):
        self.embedder = Embedder()
        self.vector_db = VectorDB(embedding_dim=384)  # dimension from MiniLM-L6-v2
        self.vector_db.load(index_path, metadata_path)
    
    def search(self, query, top_k=5):
        # Convert query to embedding
        query_embedding = self.embedder.embed_texts([query])[0]
        
        # Search for similar verses
        results = self.vector_db.search(query_embedding, top_k=top_k)
        
        # Format results
        formatted_results = []
        for verse in results:
            formatted_results.append({
                'surah_name': verse['surah_name'],
                'surah': verse['surah'],
                'ayah': verse['ayah'],
                'text': verse['text']
            })
        
        return formatted_results
