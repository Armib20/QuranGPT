from data_loader import DataLoader
from embedder import Embedder
from vector_db import VectorDB
import os

def main():
    # Create embeddings directory if it doesn't exist
    os.makedirs('embeddings', exist_ok=True)
    
    # Load Quran verses
    print("Loading Quran verses...")
    loader = DataLoader('data/quran.json')
    verses = loader.load_data()
    print(f"Loaded {len(verses)} verses")

    # Generate embeddings
    embedder = Embedder()
    texts = [verse['text'] for verse in verses]
    print("Generating embeddings...")
    embeddings = embedder.embed_texts(texts)
    
    # Store in vector database
    print("Storing embeddings in vector database...")
    vector_db = VectorDB(embedding_dim=embeddings.shape[1])
    vector_db.add_embeddings(embeddings, verses)
    
    # Save the index and metadata
    print("Saving index and metadata...")
    vector_db.save(
        'embeddings/faiss_index.idx',
        'embeddings/metadata.pkl'
    )
    
    print("Done! Embeddings saved successfully.")

if __name__ == "__main__":
    main()