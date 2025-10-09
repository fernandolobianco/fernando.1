import streamlit as st

st.title ("Medalha de São Bento")
st.write ("Fala, Professor!")
seunome = st.text_input("Qual o seu nome?")
if seunome: 
    st.write(f"Seu nome é: {seunome.upper()}")
resposta = st.text_input("Você gostaria de saber qual é a Medalha de São Bento? (sim/não): ").strip().lower()  
if resposta == "sim":
    imagemdamedalha = "https://reginafidei.com.br/wp-content/uploads/2025/07/Medalha-de-Sao-Bento.jpg"
    st.image(imagemdamedalha, caption="Medalha de São Bento")
else:
    st.write ("Você jamais conhecerá a medalha mais bonita do mundo...")
        
