import telebot
from dotenv import load_dotenv
import os

load_dotenv()

group_id = os.getenv('GROUP_ID')
api = os.getenv('API_BOT')
bot = telebot.TeleBot(api)


def send_mensage(mensagem):
    bot.send_message(group_id, mensagem )



