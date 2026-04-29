import streamlit as st
from transformers import pipeline

st.title("Ai Content Generator")
generator = pipeline("text-generation", model="gpt2")
topic = st.text_input("Enter your topic:")
content_type = st.selectbox(
    "Choose Content Type",
    ["Blog", "Instagram Caption", "Advertisement", "Story", "Motivational Quote"]
)

if st.button("Generate Content"):

    prompt = f"Write a {content_type} about {topic}:"

    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        temperature=0.9
    )

    st.subheader("Generated Content:")
    st.write(result[0]["generated_text"])
