import streamlit as st
import pandas as pd
import random

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="4Kids Dictionary", page_icon="📚")

# Estilo visual para crianças (CSS simples)
st.markdown("""
    <style>
    .main { background-color: #F0F8FF; }
    .stButton>button { background-color: #FF4B4B; color: white; border-radius: 20px; }
    h1 { color: #1E90FF; font-family: 'Comic Sans MS'; }
    </style>
    """, unsafe_allow_html=True)

# --- CARREGAMENTO DE DADOS ---
# Aqui simulamos a leitura dos teus CSVs. 
# No VS Code, certifica-te que o ficheiro CSV está na mesma pasta.
@st.cache_data
def carregar_dados():
    # Substitui 'teu_arquivo.csv' pelo nome do ficheiro de escopo que me enviaste
    # df = pd.read_csv("Conteúdos_Escopo.csv") 
    
    # Exemplo de estrutura baseada no teu escopo:
    dados = [
        {"Português": "Cadeira", "Inglês": "Chair", "Exemplo": "The chair is blue. (A cadeira é azul.)"},
        {"Português": "Maçã", "Inglês": "Apple", "Exemplo": "An apple a day! (Uma maçã por dia!)"},
        {"Português": "Escola", "Inglês": "School", "Exemplo": "I go to school. (Eu vou à escola.)"}
    ]
    return pd.DataFrame(dados)

df = carregar_dados()

# --- INTERFACE DO UTILIZADOR ---
st.title("📚 4Kids: Dicionário Visual")
st.subheader("Aprende Inglês de forma divertida!")

# Barra de Busca
busca = st.text_input("Escreve uma palavra em Português ou Inglês:", "").strip().lower()

if busca:
    # Filtra na base de dados (procura em ambas as colunas)
    resultado = df[(df['Português'].str.lower() == busca) | (df['Inglês'].str.lower() == busca)]
    
    if not resultado.empty:
        res = resultado.iloc[0]
        st.success(f"### 🇬🇧 {res['Inglês']} = 🇵🇹 {res['Português']}")
        st.info(f"**Frase de Exemplo:** \n\n {res['Exemplo']}")
    else:
        st.warning("Ups! Não encontramos essa palavra. Tenta outra!")

# --- SECÇÃO DE JOGOS ---
st.divider()
st.sidebar.header("🎮 Centro de Jogos")
if st.sidebar.button("Gerar Caça-Palavras"):
    st.write("### 🧩 Caça-Palavras do Dia")
    palavras_jogo = df['Inglês'].sample(3).tolist()
    st.write(f"Encontra estas palavras: **{', '.join(palavras_jogo).upper()}**")
    
    # Gerar Grade 10x10
    grade = [[random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(10)] for _ in range(10)]
    # (Lógica de inserção de palavras seria expandida aqui)
    st.table(grade)