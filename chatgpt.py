from transformers import pipeline, set_seed
import os

#Isso baixa (ou carrega) o modelo GPT-2 e cria uma IA capaz de gerar texto
gerador = pipeline('text-generation', model='gpt2')

set_seed(42)

print("Chatbot GPT-2 iniciado. Digite 'sair' para encerrar.")

while True:
    entrada = input("Você: ")

    if entrada.lower() == "sair":
        print("Bot: Até logo!")
        break

    resposta = gerador(entrada, max_length=50, num_return_sequences=1)[0]['generated_text']
    print("Bot:", resposta)