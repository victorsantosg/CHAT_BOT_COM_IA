# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

st.write("### ChatBot com IA") # markdown

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


