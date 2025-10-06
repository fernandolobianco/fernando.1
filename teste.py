import streamlit as st
st.title ("MEU PROGRAMA")
st.write ("Alô mundo")
seunome = text_input("Qual o seu nome?")
    if seunome: 
      st.write(seunome.upper())
      
