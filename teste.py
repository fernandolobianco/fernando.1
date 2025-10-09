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
