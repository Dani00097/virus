
import tkinter as tk
from tkinter import messagebox
import os

# Cria uma pasta para guardar os cadastros
pasta_dados = os.path.join(
    os.environ["LOCALAPPDATA"],
    "SistemaCadastro"
)

# Cria a pasta automaticamente
os.makedirs(pasta_dados, exist_ok=True)

# Define o arquivo onde os dados serão salvos
arquivo_cadastros = os.path.join(
    pasta_dados,
    "cadastros.txt"
)


def cadastrar():

    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    idade = entrada_idade.get().strip()
    telefone = entrada_telefone.get().strip()

    # Verifica se os campos estão preenchidos
    if not nome or not email or not idade or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    try:

        # Abre o arquivo para acrescentar um novo cadastro
        with open(arquivo_cadastros, "a", encoding="utf-8") as arquivo:

            arquivo.write("========== NOVO CADASTRO ==========\n")
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"E-mail: {email}\n")
            arquivo.write(f"Idade: {idade}\n")
            arquivo.write(f"Telefone: {telefone}\n")
            arquivo.write("===================================\n\n")

        messagebox.showinfo(
            "Sucesso",
            "Cadastro salvo com sucesso!"
        )

        # Limpa os campos
        entrada_nome.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_telefone.delete(0, tk.END)

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cadastro:\n\n{erro}"
        )


# ==========================================
# JANELA
# ==========================================

janela = tk.Tk()

janela.title("Sistema de Cadastro")
janela.geometry("450x500")
janela.resizable(False, False)


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    janela,
    text="CADASTRO",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=(30, 5))


subtitulo = tk.Label(
    janela,
    text="Preencha os dados abaixo",
    font=("Arial", 10)
)

subtitulo.pack(pady=(0, 25))


# ==========================================
# NOME
# ==========================================

tk.Label(
    janela,
    text="Nome completo",
    font=("Arial", 11, "bold")
).pack(anchor="w", padx=50)

entrada_nome = tk.Entry(
    janela,
    width=40,
    font=("Arial", 11)
)

entrada_nome.pack(pady=(5, 15))


# ==========================================
# EMAIL
# ==========================================

tk.Label(
    janela,
    text="E-mail",
    font=("Arial", 11, "bold")
).pack(anchor="w", padx=50)

entrada_email = tk.Entry(
    janela,
    width=40,
    font=("Arial", 11)
)

entrada_email.pack(pady=(5, 15))


# ==========================================
# IDADE
# ==========================================

tk.Label(
    janela,
    text="Idade",
    font=("Arial", 11, "bold")
).pack(anchor="w", padx=50)

entrada_idade = tk.Entry(
    janela,
    width=40,
    font=("Arial", 11)
)

entrada_idade.pack(pady=(5, 15))


# ==========================================
# TELEFONE
# ==========================================

tk.Label(
    janela,
    text="Telefone",
    font=("Arial", 11, "bold")
).pack(anchor="w", padx=50)

entrada_telefone = tk.Entry(
    janela,
    width=40,
    font=("Arial", 11)
)

entrada_telefone.pack(pady=(5, 25))


# ==========================================
# BOTÃO
# ==========================================

botao = tk.Button(
    janela,
    text="📝  CADASTRAR",
    font=("Arial", 13, "bold"),
    width=25,
    height=2,
    command=cadastrar,
    cursor="hand2"
)

botao.pack()


# ==========================================
# RODAPÉ
# ==========================================

rodape = tk.Label(
    janela,
    text="Os dados serão salvos em cadastros.txt",
    font=("Arial", 9)
)

rodape.pack(side="bottom", pady=15)


# ==========================================
# INICIAR
# ==========================================

janela.mainloop()
