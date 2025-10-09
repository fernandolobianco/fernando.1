import streamlit as st

st.title ("MEU PROGRAMA")
st.write ("Alô mundo")
seunome = st.text_input("Qual o seu nome?")
if seunome: 
    st.write(seunome.upper())
resposta = st.text_input("Você gostaria de saber qual é a Medalha de São Bento? (sim/não): ").lower()  
    if resposta == "sim":
        imagem_url = buscar_imagem ("Medalha de São Bento")
        print(imagem_url)
        webbrowser.open(imagem_url)
else:
    print ("Não consegui encontrar a imagem.")
