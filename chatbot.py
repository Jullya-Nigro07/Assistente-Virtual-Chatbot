import sys
import io
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def falar(texto):
    engine = pyttsx3.init()              #inicializa e retorna um objeto engine do pyttsx3 -> ele sintetiza voz a partir de texto
    engine.setProperty('rate', 150)      #setProperty() -> configura a propriedade rate(velocidade de fala, 150 palavras por min) e getProperty() -> obtem o valor atual do rate
    print(f"Assistente: {texto}")        
    engine.say(texto)                    #o pyttsx3 foi projetado para trabalhar com fila, say -> envia a frase em fila para o motor de conversão de texto em fala
    engine.runAndWait()                  #dispara o motor(fala tudo o que está na fila) e espera terminar
    engine.stop()                        #Cancela a fila e interrompe a fala


def ouvir():
    reconhecedor = sr.Recognizer()                                            #cria o reconhecedor de fala
    with sr.Microphone() as mic:                                              #indica que a fonte de entrada é o microfone
        print(f"ouvindo...")
        try:
            audio = reconhecedor.listen(mic)                                  #escuta você falando no microfone
            texto = reconhecedor.recognize_google(audio, language="pt-BR")    #envia para o Google e converte para texto, ou seja nao funciona sem internet
            print(f"Você: {texto}")
            return texto.lower()
        except:
            print("Não entendi!.. Tente novamente")
            return ""


def interpretar_comando(comando, nome):
    if "navegador" in comando or "google" in comando:
        falar(f"Abrindo o navegador google para você pesquisar, {nome}")
        webbrowser.open("https://google.com")                                         #módulo padrão do Py que abre URLs no navegador

    elif "horas" in comando:
        hora = datetime.now().strftime("%H:%M")
        falar(f"Agora são {hora}")

    elif "dia" in comando or "data" in comando:
        agora = datetime.now()

        dias_semana = [
            "segunda-feira", "terça-feira", "quarta-feira",
            "quinta-feira", "sexta-feira", "sábado", "domingo"
        ]
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]

        dia_semana = dias_semana[agora.weekday()]
        dia = agora.day
        numero_mes = agora.month
        nome_mes = meses[numero_mes - 1] # -1 pq o indice começa do 0, e month pega de 1 á 12
        ano = agora.year

        falar(f"Hoje é {dia_semana}, dia {dia}, do mês {numero_mes}, de {nome_mes}, de {ano}.")


    elif "abrir github" in comando or "git" in comando:
        falar(f"Abrindo o seu Git Hub, para você {nome}")
        webbrowser.open("https://github.com/Impacta-Jullya-Nigro")
        #os.startfile(os.path.expanduser("~/Documets"))                               #abre caminhos locais

    elif "sair" in comando:
        falar(f"Encerrando... até a proxima {nome}, espero ter te ajudado!")
        return False

    else:
        falar("Desculpe, não entendi")

    return True

def inicar_assistente():
    falar("Olá! Eu sou sua assistente virtual Lola. Qual é o seu nome? ")
    nome = ouvir()
    falar(f"Olá {nome}, no que posso te ajudar? ")
    while True:
        comando = ouvir()
        if not interpretar_comando(comando, nome):
            break

if __name__ == "__main__":
    inicar_assistente()
