import faiss
from embedder import Embedder
import pickle

class VectorDB:
    def __init__(self, dim: int):
        self.index = faiss.IndexHNSWFlat(dim)
        self.embedder = Embedder()
