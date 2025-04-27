import random
import tkinter as tk
from tkinter import scrolledtext


def responder_melhor(user_input):
    user_input = user_input.lower()
    if "terror" in user_input:
        return random.choice([
            "Recomendo 'Hereditário', muito assustador!",
            "'Invocação do Mal' é um clássico do terror.",
            "'It: A Coisa' é uma boa escolha se curte suspense."
        ])
    elif "comédia" in user_input:
        return random.choice([
            "Você vai curtir 'Superbad'!",
            "'Se Beber, Não Case' é muito engraçado!",
            "'Brooklyn Nine-Nine' é uma série leve e divertida."
        ])
    elif "ação" in user_input or "adrenalina" in user_input:
        return random.choice([
            "'John Wick' é ação pura!",
            "'Missão Impossível: Efeito Fallout' é muito bom.",
            "'Mad Max: Estrada da Fúria' é imperdível!"
        ])
    elif "drama" in user_input:
        return random.choice([
            "'Oppenheimer' é um drama incrível!",
            "'O Irlandês' é ótimo se gosta de histórias mais densas.",
            "'A Rede Social' também é um drama interessante."
        ])
    elif "ficção" in user_input or "científica" in user_input:
        return random.choice([
            "'Duna' é obrigatório pra fãs de ficção!",
            "'Interestelar' é um dos melhores de ficção científica.",
            "'Blade Runner 2049' é muito bom também."
        ])
    elif "romance" in user_input or "amor" in user_input:
        return random.choice([
            "'Como Eu Era Antes de Você' é emocionante.",
            "'Orgulho e Preconceito' é um clássico do romance.",
            "'La La Land' é um romance musical maravilhoso."
        ])
    elif "suspense" in user_input:
        return random.choice([
            "'Seven: Os Sete Crimes Capitais' é incrível!",
            "'Garota Exemplar' é um suspense top!",
            "'Ilha do Medo' vai explodir sua cabeça!"
        ])
    elif "animação" in user_input:
        return random.choice([
            "'Toy Story' é nostálgico e divertido!",
            "'Divertida Mente' é uma animação linda!",
            "'Homem-Aranha no Aranhaverso' é sensacional!"
        ])
    elif "sair" in user_input or "tchau" in user_input:
        return "Até logo! Volte sempre para mais dicas de filmes e séries! 🎬"
    elif "oi" in user_input or "olá" in user_input:
        return "Olá! 🎬 Me pergunte sobre filmes ou séries que eu te recomendo!"
    else:
        return "Não entendi muito bem... Pergunte, por exemplo: 'me indica um filme de terror?' 😉"


def send_message():
    user_input = user_entry.get()
    chat_area.config(state='normal')
    chat_area.insert(tk.END, "Você: " + user_input + "\n")
    response = responder_melhor(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.config(state='disabled')
    user_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Chatbot de Filmes e Séries 🎬")
window.geometry("500x500")
window.configure(bg="#222831")  


chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, state='disabled', bg="#393E46", fg="#EEEEEE", font=("Arial", 11), bd=2, relief="solid", highlightthickness=1, highlightbackground="#00ADB5")
chat_area.pack(padx=10, pady=10)


user_entry = tk.Entry(window, width=50, bg="#EEEEEE", fg="#222831", font=("Arial", 12), bd=2, relief="solid", highlightthickness=1, highlightbackground="#00ADB5")
user_entry.pack(padx=10, pady=(0, 10))


send_button = tk.Button(window, text="Enviar", command=send_message, bg="#00ADB5", fg="white", font=("Arial", 12, "bold"), relief="flat", padx=10, pady=5)
send_button.pack(padx=10, pady=(0, 10))


def enter_pressed(event):
    send_message()

user_entry.bind("<Return>", enter_pressed)


window.mainloop()
