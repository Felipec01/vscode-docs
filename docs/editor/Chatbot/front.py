import streamlit as st

st.title("Prueba chatbot")

#Variables de estado
if "messages" not in st.session_state:
    st.session_state.messages = [] #Historico del chat
if "first_message" not in st.session_state:
    st.session_state.first_message = True #Variable para ver si es el primer mensaje del chat

for message in st.session_state.messages: ##Recorrer array de mensajes
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.first_message: #Comprobar si es el primer mensaje
    with st.chat_message("assistant"):
        st.markdown("Hola! Bienvenido al chat de nuestra empresa. Como puedo ayudarte?")

    st.session_state.messages.append({"role": "assistant", "content": "Hola! Bienvenido al chat de nuestra empresa. Como puedo ayudarte?"})
    st.session_state.first_message = False

#Crear prompt para el usuario y mostrar respuesta en pantalla
if prompt := st.chat_input("En que te puedo ayudar?"):
    with st.chat_message("over"):
        st.markdown(prompt) #Mostrar lo escrito por el usuario en pantalla
    st.session_state.messages.append({"role": "over", "content": prompt}) #guardar mensaje en histórico

    with st.chat_message("assistant"): #Respuesta del chatbot
        st.markdown(prompt)
    st.session_state.messages.append({"role": "assistant", "content": prompt})