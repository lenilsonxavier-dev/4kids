import PyPDF2
import pandas as pd
import re

def extrair_do_dicionario():
    palavras = []
    
    # 1. Extração do Dicionário eBooksBrasil (O seu PDF DOCX)
    try:
        reader = PyPDF2.PdfReader("Dicionario_Ingles_Portugues.docx.pdf")
        for page in reader.pages:
            texto = page.extract_text()
            # Procura o padrão: palavra-- tradução
            matches = re.findall(r'([a-zA-Z-]+)–\s*([^–\n]+)', texto)
            for en, pt in matches:
                palavras.append({"Inglês": en.strip(), "Português": pt.strip()})
    except Exception as e:
        print(f"Erro ao ler dicionário principal: {e}")

    # 2. Extração das 1000 palavras mais usadas
    try:
        reader = PyPDF2.PdfReader("1000-PALAVRAS-MAIS-USADAS-EM-INGLES.pdf")
        for page in reader.pages:
            texto = page.extract_text()
            # Padrão: Número Palavra Pronúncia Tradução
            matches = re.findall(r'\d+\s+([a-zA-Z-]+)\s+.*?\s+([a-zA-Z, \/ãáéíóúç]+)', texto)
            for en, pt in matches:
                palavras.append({"Inglês": en.strip(), "Português": pt.strip()})
    except:
        pass

    # Salvar tudo num CSV para o App Web
    df = pd.DataFrame(palavras).drop_duplicates(subset=['Inglês'])
    df['Exemplo'] = "Learn how to use " + df['Inglês'] + " in a sentence!"
    df.to_csv("dicionario_final.csv", index=False)
    print(f"Sucesso! {len(df)} palavras extraídas dos dicionários.")

if __name__ == "__main__":
    extrair_do_dicionario()