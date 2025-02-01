import streamlit as st
from query_handler import QueryHandler

def main():
    st.title("QuranGPT")
    st.write("Ask any question about the Quran")
    
    # Initialize query handler
    handler = QueryHandler()
    
    # Create the search interface
    query = st.text_input("Enter your question:")
    num_results = st.slider("Number of verses to return:", 1, 10, 5)
    
    if st.button("Search"):
        if query:
            results = handler.search(query, top_k=num_results)
            
            for result in results:
                st.markdown(f"""
                [**Surah {result['surah_name']} ({result['surah']}), Verse {result['ayah']}**](https://quran.com/{result['surah']}?startingVerse={result['ayah']})  
                {result['text']}
                """)
        else:
            st.warning("Please enter a question")

if __name__ == "__main__":
    main()
