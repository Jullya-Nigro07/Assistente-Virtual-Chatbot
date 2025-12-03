# 🤖 Lola - Assistente Virtual por Voz

---

## 🚀 Sobre o Projeto

O Lola é um **assistente virtual interativo** construído em Python que utiliza processamento de linguagem natural (via Google Speech Recognition) e síntese de voz (via `pyttsx3`) para receber comandos de voz do usuário e executar tarefas específicas.

Este projeto demonstra a integração de bibliotecas Python para **reconhecimento de fala** (`speech_recognition`), **conversão de texto em fala** (`pyttsx3`) e **automação de tarefas** (como abrir o navegador com `webbrowser`).

---

## ✨ Funcionalidades

O assistente Lola atualmente suporta os seguintes comandos de voz:

* **Abrir Navegador/Google**: Abre a página inicial do Google no seu navegador padrão.
* **Ver Horas**: Informa a hora atual (ex: "Agora são 10:30").
* **Ver Dia/Data**: Informa a data completa (dia da semana, dia, mês e ano).
* **Abrir GitHub**: Abre um URL específico do GitHub configurado no código (`https://github.com/Impacta-Jullya-Nigro`).
* **Sair/Encerrar**: Encerra a execução do assistente.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **`pyttsx3`**: Para conversão de texto em fala.
* **`speech_recognition`**: Para reconhecimento de voz, utilizando o Google Speech Recognition (requer conexão com a internet).
* **`PyAudio`**: (Dependência do `speech_recognition`) Necessário para acessar o microfone.
* **Módulos Padrão do Python**: `datetime`, `webbrowser`, `os`, `sys`, `io`.

---

## ⚙️ Instalação e Configuração

### Pré-requisitos

1.  Python 3.x instalado.
2.  Um microfone funcional.

### 1. Instalar as Dependências

É necessário instalar as bibliotecas `pyttsx3` e `SpeechRecognition`.

```bash
pip install pyttsx3
pip install SpeechRecognition
```

---

### 2. Executar o Assistente

Execute o arquivo principal `chatbot.py` em seu terminal:

```bash
python chatbot.py
```

---

## 🎤 Como Usar

1.  Ao iniciar, o assistente perguntará: **"Olá! Eu sou sua assistente virtual Lola. Qual é o seu nome?"**
2.  Fale seu nome.
3.  Lola saudará você e perguntará **"no que posso te ajudar?"**
4.  Fale um dos comandos listados na seção "Funcionalidades" após ouvir **"ouvindo..."**.
5.  Para sair, diga **"sair"** ou um comando similar que acione o encerramento.

---

## 📝 Estrutura do Código

| Função | Descrição |
| :--- | :--- |
| `falar(texto)` | Sintetiza o texto em voz usando `pyttsx3` e imprime no console. |
| `ouvir()` | Captura o áudio do microfone e usa o Google para converter a fala em texto (requer internet). |
| `interpretar_comando(comando, nome)` | Mapeia o texto reconhecido às ações (abrir browser, informar hora/data, etc.). |
| `inicar_assistente()` | Função principal que gerencia o ciclo de vida do assistente, desde a saudação até o loop de comandos. |
