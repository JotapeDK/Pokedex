from io import BytesIO
import customtkinter as ctk
from PIL import Image, ImageTk, ImageMath
import requests



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def buscar_pokemon():
    pokemondigitado = entrada_nome.get().lower().strip()

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemondigitado}")

    if resposta.status_code == 200:
        dados = resposta.json()


        nome = dados['name'].capitalize()
        id_pokemon = dados['id']

        url_imagem = dados['sprites']['front_default']

        label_resultado.configure(text=f"{nome} #{id_pokemon}")

        if url_imagem:
            resposta_imagem = requests.get(url_imagem)
            img_bytes = BytesIO(resposta_imagem.content)

            img_pil = Image.open(img_bytes)
            imagem_ctk = ctk.CTkImage(light_image=img_pil, dark_image=img_pil, size=(150, 150))

            label_imagem.configure(image=imagem_ctk)
            label_imagem.image = imagem_ctk

    else:
        label_resultado.configure(text="Erro: Pokémon não encontrado!")
        label_imagem.configure(image=None)

janela = ctk.CTk()
janela.title("Minha Pokédex Python")
janela.geometry("400x450")


label_titulo = ctk.CTkLabel(janela, text="Pokédex", font=("Arial", 24, "bold"))
label_titulo.pack(pady=20)


entrada_nome = ctk.CTkEntry(janela, placeholder_text="Digite o nome do Pokémon")
entrada_nome.pack(pady=10)


botao_buscar = ctk.CTkButton(janela, text="Buscar", command=buscar_pokemon)
botao_buscar.pack(pady=10)


label_imagem = ctk.CTkLabel(janela, text="")
label_imagem.pack(pady=10)


label_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 18, "bold"))
label_resultado.pack(pady=10)


janela.mainloop()



