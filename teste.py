import streamlit as st
import requests

API_KEY = "SUA_API_KEY_AQUI"
CX = "SEU_CX_AQUI"

def buscar_imagem(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": API_KEY, "cx": CX, "q": query, "searchType": "image", "num": 1}
    r = requests.get(url, params=params).json()
    return r.get("items", [{}])[0].get("link")

st.title("Medalha de São Bento")
st.write("Fala, Josir!")

seunome = st.text_input("Qual o seu nome?")
if seunome:
    st.write(f"Seu nome é: {seunome.upper()}")

resposta = st.text_input("Você gostaria de saber qual é a Medalha de São Bento? (sim/não):").strip().lower()

if resposta == "sim":
    imagem = buscar_imagem("Medalha de São Bento")
    if imagem:
        st.image(imagem, caption="Medalha de São Bento")
    else:
        st.write("Não consegui encontrar a imagem.")
