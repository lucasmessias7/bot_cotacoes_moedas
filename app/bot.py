import telebot
from dotenv import load_dotenv
from request_api import last_recorrence_coin
import os
import asyncio

load_dotenv()

group_id = os.getenv('GROUP_ID')
api = os.getenv('API_BOT')
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, text="📊 Bem-vindo ao CriptoBot 📊 \nseu radar inteligente do mercado financeiro!\n Aqui você encontra cotações em tempo real, notícias atualizadas e análises rápidas para tomar decisões mais informadas.\nSeja você investidor iniciante ou experiente, estou pronto para te ajudar a acompanhar o mercado com agilidade e precisão.\n\n")

@bot.message_handler(commands=['COTACAO_REAL_DOLAR'])
def send_mensage(message):
    bot.reply_to(message=message, text=last_recorrence_coin('last/BRL-USD', 'BRLUSD'))


@bot.message_handler(commands=['COTACAO_REAL_EURO'])
def send_mensage(message):
    bot.reply_to(message=message, text=last_recorrence_coin('last/BRL-EUR', 'BRLEUR'))


@bot.message_handler(commands=['COTACAO_REAL_YUAN'])
def send_mensage(message):
    bot.reply_to(message=message, text=last_recorrence_coin('last/BRL-CNY', 'BRLCNY'))


@bot.message_handler(commands=['COTACAO_REAL_BTC'])
def send_mensage(message):
    bot.reply_to(message=message, text=last_recorrence_coin('last/USD-CNH', 'USDCNH'))



bot.polling()



