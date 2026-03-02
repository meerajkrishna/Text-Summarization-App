import streamlit as st
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit App
st.title("Summarization App")

# Input text area for user to enter the article
article = st.text_area("Enter the article:", "", height=300)

if st.button("Generate Summary"):
    if article:
        # Generate summary using the summarizer pipeline
        summary_result = summarizer(article, max_length=130, min_length=30, do_sample=False)

        # Extract the summary text
        summary_text = summary_result[0]['summary_text']

        # Display the summary
        st.subheader("Summary:")
        st.write(summary_text)
    else:
        st.warning("Please enter an article for summarization.")
