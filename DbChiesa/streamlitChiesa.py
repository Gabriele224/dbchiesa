import streamlit as st
import os
import streamlit.components.v1 as components
st.title("Benvenuti nello spazio dedicato ai momenti dello spirito")

PATH_HTML_PRAY="./PRAY"

PATH_HTML_ROSARY="./ROSARY"

PATH_HTML_LITANIES="./LITANIES"
st.write("Momento dedicato alla Preghiera")

html_pages_pray = [file for file in os.listdir(PATH_HTML_PRAY) if file.endswith(".html")]

box_html_pray= st.selectbox("Seleziona file desiderato\n", html_pages_pray)

if st.button("Ricerca Preghiera", box_html_pray):

    file_path= os.path.join(PATH_HTML_PRAY,box_html_pray)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")


st.write("Momento dedicato al Rosario")

html_pages_rosary = [file for file in os.listdir(PATH_HTML_ROSARY) if file.endswith(".html")]

box_html_rosary= st.selectbox("Seleziona file desiderato\n", html_pages_rosary)

if st.button("Ricerca Mistero", box_html_rosary):

    file_path= os.path.join(PATH_HTML_ROSARY,box_html_rosary)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")

st.write("Momento decicato alle Litanie")

html_pages_litanies = [file for file in os.listdir(PATH_HTML_LITANIES) if file.endswith(".html")]

box_html_litanies= st.selectbox("Seleziona file desiderato\n", html_pages_litanies)

if st.button("Ricerca Litanie", box_html_litanies):

    file_path= os.path.join(PATH_HTML_LITANIES,box_html_litanies)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")
