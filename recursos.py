import streamlit as st
import os

# Diretório onde os PDFs estão localizados
pdf_directory = r'C:\Users\henrique.neves\PycharmProjects\RECURSOS'


# Função para criar um índice dos PDFs
def create_index(directory):
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    return pdf_files


# Função para remover a extensão do PDF do nome do arquivo
def remove_extension(file_name):
    return os.path.splitext(file_name)[0]


# Função para mostrar e permitir download dos PDFs
def display_pdf_options(pdf_files):
    # Barra de pesquisa
    search_query = st.text_input("Buscar por projeto:")
    if search_query:
        pdf_files = [file for file in pdf_files if search_query.lower() in remove_extension(file).lower()]

    # Filtro de alfabeto
    letters = sorted(set(file[0].upper() for file in pdf_files))
    selected_letter = st.selectbox("Filtrar por letra:", ['Todas'] + letters)

    if selected_letter != 'Todas':
        pdf_files = [file for file in pdf_files if file[0].upper() == selected_letter]

    # Exibir lista de arquivos PDF
    pdf_files_display = [remove_extension(file) for file in pdf_files]
    selected_file = st.selectbox("Escolha um projeto:", pdf_files_display)

    if selected_file:
        st.write(f"Você selecionou: {selected_file}")
        st.write("Clique no botão para baixar:")

        # Caminho completo do PDF selecionado
        file_path = os.path.join(pdf_directory, f"{selected_file}.pdf")

        # Mostrar botão para visualizar o PDF
        st.download_button(
            label="Baixar PDF",
            data=open(file_path, 'rb').read(),
            file_name=f"{selected_file}.pdf",
            key=f'download_{selected_file}'
        )


# Layout do Streamlit
st.set_page_config(page_title="Pesquisar por Recursos", layout="wide")
st.title("Pesquisar por Recursos")

# Criar índice dos PDFs
pdf_files = create_index(pdf_directory)

# Mostrar opções de PDFs
display_pdf_options(pdf_files)
