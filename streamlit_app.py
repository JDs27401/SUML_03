import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(page_title="EN-DE Translator", page_icon="🫖🍺")
st.title("🫖 English - German 🍺 Translator")

st.write("""
Hello! This app is used for translating English to German! 
\nPlease input text you want to translate and press \"Translate\" button.
""")

input_text = st.text_area("Input text in English:", height=150)

if st.button("Translate"):
    if input_text:
        with st.spinner('Translating, please wait...'):
            try:
                model_name = "Helsinki-NLP/opus-mt-en-de"
                tokenizer = AutoTokenizer.from_pretrained(model_name)
                model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

                inputs = tokenizer(input_text, return_tensors="pt")
                outputs = model.generate(**inputs)
                output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

                st.success("Translation finished")
                st.write("Result:")
                st.info(output_text)

            except Exception as e:
                st.error(f"An error occurred 💀: {e}")
    else:
        st.warning("First, please input text you want to translate...")

st.markdown("---")
st.write("Numer indeksu: s27401")