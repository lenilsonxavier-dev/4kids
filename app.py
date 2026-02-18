import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="4Kids - Dicionário", page_icon="📖")

@st.cache_data
def carregar_dados():
    if os.path.exists("dicionario_final.csv"):
        return pd.read_csv("dicionario_final.csv")
    else:
        return pd.DataFrame({"Inglês": ["A"], "Português": ["Um/Uma"], "Exemplo": ["A book."]})

df = carregar_dados()

st.title("📖 Dicionário 4Kids")
st.write("Pesquisa baseada nos dicionários oficiais carregados.")

# Barra de Busca
busca = st.text_input("Escreva a palavra (Inglês ou Português):").strip().lower()

if busca:
    resultado = df[(df['Inglês'].str.lower() == busca) | (df['Português'].str.lower() == busca)]
    
    if not resultado.empty:
        item = resultado.iloc[0]
        st.success(f"### {item['Inglês']} = {item['Português']}")
        st.info(f"💡 {item['Exemplo']}")
    else:
        st.warning("Palavra não encontrada no dicionário.")

# Gerador de Jogos (Caça-Palavras)
st.sidebar.title("🎮 Jogos")
if st.sidebar.button("Novo Caça-Palavras"):
    st.session_state.game_words = df.sample(5)['Inglês'].tolist()
    st.sidebar.write("Encontre estas palavras:")
    st.sidebar.write(st.session_state.game_words)