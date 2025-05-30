import streamlit as st
import os
import streamlit.components.v1 as components
st.title("Chiesa")


html_pages = [file for file in os.listdir(PATH_HTML) if file.endswith(".html")]

box_html= st.selectbox("Seleziona file desiderato\n", html_pages)

if st.button("Ricerca", box_html):

    file_path= os.path.join(PATH_HTML,box_html)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")
