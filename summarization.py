import streamlit as st
from spacy import displacy
from gensim.summarization import summarize

#from multilang_summarizer.summarizer import summarizer

# summarizer(D_path, f_method, seq_method, lemmatizer, session_id=1)

#from multilang_summarizer.lemmatizer import Lemmatizer
#lemmatizer = Lemmatizer.for_language("en")

def main():
    
    st.title("Rissa's Summarizer App")
    
    activities = ["Summarize Via Text", "Summarize Via URL", "Summarize Via Upload"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    if choice == 'Summarize Via Text':
        st.subheader("Summary using NLP")
        raw_text = st.text_area("Enter Text Here")
        summary_choice = st.selectbox("Summary Choice" , ["Gensim","Sumy Lex rank","NLTK"])
        if st.button("Summarize Via Text"):
            if summary_choice == 'Gensim':
                summary_result = summarize(raw_text)
            
            st.write(summary_result)      
              
if __name__ == '__main__':
    main()