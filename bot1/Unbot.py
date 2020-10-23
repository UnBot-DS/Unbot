#-- coding: utf-8 --

import telebot 
from telebot import types

API_TOKEN = '1275291244:AAFQz-QR1eJwM6L5vm35pzjMRPSFlBfOjVc'                       

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	cid = message.chat.id
	msg = bot.reply_to(message, "Olá, este é o Unbot. \n Em que podemos ajudar")
	bot.send_message(cid, "Caso você precise de ajuda, use a função: /ajuda")
	

@bot.message_handler(commands=['ajuda'])
def send_help(message):
	cid = message.chat.id
	msg_help = bot.reply_to(message, "Você não se lembra das funções? \n Opção 1: /cadastro \n Opção 2: /categoria \n Opção 3: /imagens \n Opção 4: /documentos ")
	bot.send_message(cid, "Caso ainda encontre dificuldades, entre em contato pelo e-mail:           ")
	
	
@bot.message_handler(commands=['categoria'])
def send_category(message):
	cid = message.chat.id
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	markup.add('SIGAA','CLIMA','LOCALIZAÇÕES')
	msg_cat = bot.reply_to(message, "Escolhe a categoria que você deseja:", reply_markup=markup)
	
	
@bot.message_handler(commands=['documentos'])
def send_document(message):
	cid = message.chat.id
	doc = 'http://portalsig.unb.br/images/Manuais/Manual_Portal_do_Discente_-_Ambiente_Virtual.pdf'
	bot.send_document(cid, doc)
	

@bot.message_handler(commands=['imagens'])
def send_photo(message):
	cid = message.chat.id
	photo = 'https://upload.wikimedia.org/wikipedia/commons/f/f2/Campus_da_UnB_no_Gama_%28FGA%29_completa_10_anos_%2839135873690%29.jpg'
	bot.send_photo(cid, photo)
	

	
	
bot.polling()
	 
