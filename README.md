## 📈 Bot de Cotações de Moedas - Diretório app
Este diretório contém a lógica principal do bot de cotações de moedas, desenvolvido em Python. O objetivo do projeto é automatizar a coleta e o envio de informações sobre taxas de câmbio de diversas moedas, utilizando APIs externas e integração com o Telegram.

## 🚀 Funcionalidades
Consulta de cotações de moedas (ex: USD, EUR, BTC, etc.)
Integração com a API do Telegram para envio automático das cotações
Agendamento de tarefas com apscheduler
Suporte a múltiplas moedas e formatos de resposta
Logs de execução para monitoramento
## 📁 Estrutura do Diretório

app/

requirements.txt

# Configurações gerais do bot (tokens, URLs, etc.)

├── cotacoes.py        # Funções para buscar cotações de moedas

├── telegram_bot.py    # Lógica de envio de mensagens via Telegram

├── scheduler.py       # Agendamento de tarefas automáticas

└── utils.py           # Funções auxiliares
## 🛠️ Requisitos

Python 3.10+

## Bibliotecas:
Instale os requisitos com:

pip install -r requirements.txt

## ⚙️ Configuração

Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

API_BOT = sua API do telegram


## ▶️ Execução
Para iniciar o bot:

pyhon run bot.py

## 📌 Observações
## Ainda em construção ....

### adicionaremos: 

Enviar noticias sobre investimentos.

O bot será configurado para enviar cotações em horários específicos.

adaptar o projeto para outras plataformas além do Telegram.
