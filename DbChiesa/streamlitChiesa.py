import streamlit as st
import os
import streamlit.components.v1 as components
from PIL import Image
import base64 ,re
st.title("Benvenuti nello spazio dedicato ai momenti dello spirito")

def encode_image_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        ext = os.path.splitext(img_path)[1][1:]  # esempio: jpg, png
        return f"data:image/{ext};base64,{encoded_string}"

def embed_images_in_html(html_content, base_folder):
    matches = re.findall(r'<img\s+[^>]*src="([^"]+)"', html_content)
    for src in matches:
        img_path = os.path.join(base_folder, src)
        if os.path.exists(img_path):
            img_data_uri = encode_image_to_base64(img_path)
            html_content = html_content.replace(src, img_data_uri)
    return html_content

PATH_HTML_PRAY="./DbChiesa/PRAY"

PATH_HTML_ROSARY="./DbChiesa/ROSARY"

PATH_HTML_LITANIES="./DbChiesa/LITANIES"

PATH_HTML_CGREVENTS="./DbChiesa/CGREVENTS"

PATH_HTML_CGRBIBLE="./DbChiesa/CGRBIBLE"

PATH_HTML_PROVERB="./DbChiesa/PROVERBS"

PATH_HTML_SANTS="./DbChiesa/SANTS"

st.write("Momento dedicato alla Preghiera")

html_pages_pray = [file for file in os.listdir(PATH_HTML_PRAY) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_pray]

box_html_pray= st.selectbox("Seleziona la preghiera desiderato\n", display_names)

if st.button("Ricerca Preghiera", box_html_pray):

    # Ricostruisci il nome completo del file
    selected_file = box_html_pray + ".html"
    file_path= os.path.join(PATH_HTML_PRAY,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")


st.write("Momento dedicato al Rosario")

html_pages_rosary = [file for file in os.listdir(PATH_HTML_ROSARY) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_rosary]
box_html_rosary= st.selectbox("Seleziona il mistero desiderato\n", display_names)

if st.button("Ricerca Mistero", box_html_rosary):

    # Ricostruisci il nome completo del file
    selected_file = box_html_rosary + ".html"
    file_path= os.path.join(PATH_HTML_ROSARY,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")

st.write("Momento dedicato alle Litanie")

html_pages_litanies = [file for file in os.listdir(PATH_HTML_LITANIES) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_litanies]
box_html_litanies= st.selectbox("Seleziona le litanie desiderato\n", display_names)

if st.button("Ricerca Litanie", box_html_litanies):

    # Ricostruisci il nome completo del file
    selected_file = box_html_rosary + ".html"
    file_path= os.path.join(PATH_HTML_LITANIES,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")

st.write("Eventi CGR (Comunità Gesù Risorto)")
html_pages_cgr = [file for file in os.listdir(PATH_HTML_CGREVENTS) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_cgr]
box_html_cgr= st.selectbox("Seleziona Evento desiderato\n", display_names)

if st.button("Ricerca Eventi CGR", box_html_cgr):

    # Ricostruisci il nome completo del file
    selected_file = box_html_cgr + ".html"
    file_path= os.path.join(PATH_HTML_CGREVENTS,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    contenuto = embed_images_in_html(contenuto, PATH_HTML_CGREVENTS)

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")

st.write("Versetti Bibbia CGR (Comunità Gesù Risorto)")
html_pages_cgr = [file for file in os.listdir(PATH_HTML_CGRBIBLE) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_cgr]
box_html_cgr= st.selectbox("Seleziona il passo della Bibbia\n", display_names)

if st.button("Ricerca Versetti Bibbia CGR", box_html_cgr):

    # Ricostruisci il nome completo del file
    selected_file = box_html_cgr + ".html"
    file_path= os.path.join(PATH_HTML_CGRBIBLE,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    contenuto = embed_images_in_html(contenuto, PATH_HTML_CGRBIBLE)

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")

st.write("Proverbi di Gesù")
html_pages_proverbs = [file for file in os.listdir(PATH_HTML_PROVERB) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_proverbs]
box_html_proverbs= st.selectbox("Seleziona il proverbio desiderato\n", display_names)

if st.button("Ricerca del Proverbio", box_html_proverbs):

    # Ricostruisci il nome completo del file
    selected_file = box_html_proverbs + ".html"
    file_path= os.path.join(PATH_HTML_PROVERB,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    contenuto = embed_images_in_html(contenuto, PATH_HTML_PROVERB)

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")

st.write("Storia dedicata ai Santi")
html_pages_sants = [file for file in os.listdir(PATH_HTML_SANTS) if file.endswith(".html")]

display_names = [os.path.splitext(f)[0] for f in html_pages_sants]
box_html_sants= st.selectbox("Seleziona la storia desiderata\n", display_names)

if st.button("Ricerca del Santo", box_html_sants):

    # Ricostruisci il nome completo del file
    selected_file = box_html_sants + ".html"
    file_path= os.path.join(PATH_HTML_SANTS,selected_file)
    with open(file_path, "r+", encoding="utf-8") as file:

        contenuto= file.read()

    contenuto = embed_images_in_html(contenuto, PATH_HTML_SANTS)

    components.html(contenuto, height=600, scrolling=True)
else:
    st.write("\n")
