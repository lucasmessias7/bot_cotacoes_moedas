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
    bot.reply_to(message, text="📊 Bem-vindo ao CriptoBot 📊 \nseu radar inteligente do mercado financeiro!\nAqui você encontra cotações em tempo real, notícias atualizadas e análises rápidas para tomar decisões mais informadas.\nSeja você investidor iniciante ou experiente, estou pronto para te ajudar a acompanhar o mercado com agilidade e precisão.\n\n")


# print(last_recorrence_coin('last/ETH-BRL', 'ETHBRL'))
@bot.message_handler(commands=['COTACAO_REAL_BTC','COTACAO_REAL_EURO','COTACAO_REAL_YUAN','COTACAO_REAL_DOLAR','COTACAO_REAL_ETH'])
def send_mensage(message):
    resposta = message.text

    if resposta == '/COTACAO_REAL_BTC':    
        bot.reply_to(message, text=last_recorrence_coin('last/BTC-BRL', 'BTCBRL'))

    if resposta == '/COTACAO_REAL_EURO':
        bot.reply_to(message, text=last_recorrence_coin('last/EUR-BRL', 'EURBRL'))
    
    if resposta == '/COTACAO_REAL_YUAN':
        bot.reply_to(message, text=last_recorrence_coin('last/CNY-BRL', 'CNYBRL'))
    
    if resposta == '/COTACAO_REAL_DOLAR':
        bot.reply_to(message, text=last_recorrence_coin('last/USD-BRL', 'USDBRL'))

    if resposta == '/COTACAO_REAL_ETH':
        bot.reply_to(message, text=last_recorrence_coin('last/ETH-BRL', 'ETHBRL'))


bot.polling()



