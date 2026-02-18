import streamlit as st
import pandas as pd

# Configuração da Interface Web
st.set_page_config(page_title="4Kids Dictionary", layout="centered")

def carregar_dicionario():
    # Integração dos ficheiros fornecidos (PDFs convertidos ou CSVs)
    # Aqui simulamos a união do '1000-palavras', 'Dicionário_Ingles' e 'Livro'
    dados = {
        "Inglês": ["The", "Book", "School", "Noon", "Giant anteater"],
        "Português": ["O/A", "Livro", "Escola", "Meio-dia", "Tamanduá-bandeira"],
        "Exemplo": [
            "The apple is red.", 
            "I have a new book.", 
            "Welcome back to school!", 
            "We eat at noon.",
            "The giant anteater has a long snout."
        ]
    }
    return pd.DataFrame(dados)

df_4kids = carregar_dicionario()

# Título do App Web
st.title("📚 Dicionário Visual 4Kids")
st.markdown("---")

# Sistema de Busca
palavra_busca = st.text_input("Pesquise uma palavra (PT ou EN):").strip().lower()

if palavra_busca:
    # Busca inteligente nas duas colunas
    resultado = df_4kids[(df_4kids['Inglês'].str.lower() == palavra_busca) | 
                         (df_4kids['Português'].str.lower() == palavra_busca)]
    
    if not resultado.empty:
        item = resultado.iloc[0]
        st.success(f"### {item['Inglês']} ↔️ {item['Português']}")
        st.write(f"**Exemplo de uso:** {item['Exemplo']}")
    else:
        st.error("Palavra não encontrada no escopo escolar.")

# Rodapé Educativo
st.sidebar.image("https://img.icons8.com/color/96/000000/alphabet.png")
st.sidebar.info("Este dicionário baseia-se no currículo oficial e nos 3000 termos mais comuns.")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="4Kids Web", page_icon="🎨")

# Carregar os dados extraídos
@st.cache_data
def load_data():
    return pd.read_csv("dicionario_final.csv")

df = load_data()

st.title("🌟 Dicionário 4Kids")
st.write(f"Atualmente com {len(df)} palavras e expressões do seu escopo!")

# Busca
search = st.text_input("O que queres aprender hoje? (PT ou EN)").strip().lower()

if search:
    filt = df[(df['Inglês'].str.lower() == search) | (df['Português'].str.lower() == search)]
    if not filt.empty:
        st.balloons()
        row = filt.iloc[0]
        st.markdown(f"### 🇬🇧 {row['Inglês']} significa 🇵🇹 {row['Português']}")
        st.info(f"💡 **Frase de exemplo:** {row['Exemplo']}")
    else:
        st.warning("Ainda não tenho essa palavra. Tenta 'School' ou 'Book'!")

# Sidebar com Jogos baseados no CSV
st.sidebar.title("🎮 Jogos")
if st.sidebar.button("Cruzadinha Rápida"):
    palavras_aleatorias = df.sample(5)['Inglês'].tolist()
    st.sidebar.write("Dicas para a cruzadinha:")
    for p in palavras_aleatorias:
        traducao = df[df['Inglês'] == p]['Português'].values[0]
        st.sidebar.write(f"- Qual o inglês para: **{traducao}**?")