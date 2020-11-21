import telebot # Para funcionar no seu pc abra o cmd ou PowerShell e digite: pip install --user pyTelegramBotAPI e para atualizar: pip install --user pyTelegramBotAPI --upgrade pip
import requests # Tem que instalar requests tambem pelo cmd ou PowerShell: pip install requests
from telebot import types
from selenium import webdriver # Tem que instalar selenium tambem pelo cmd ou PowerShell
import time
from selenium.webdriver.support.select import Select   


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
	msg_help = bot.reply_to(message, "Você não se lembra das funções? \n Opção 1: /cadastro \n Opção 2: /categoria \n Opção 3: /imagens \n Opção 4: /documentos \n Opção 5: /sigaa")
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


@bot.message_handler(commands=['sigaa', 'Sigaa'])
def send_teste_(message):
	cid = message.chat.id
	msg = bot.reply_to(message, "Gostaria de acessar o Sigaa? /sim ou /nao")


@bot.message_handler(commands=['sim']) # Esse comando para iniciar o processo de impressão do documento sigaa
def send_sim_(message):
	cid = message.chat.id
	msg = bot.reply_to(message, "Ok, Digite seu usuario SIGAA: ")
	# Essa sequencia de comentarios era para testar as variaveis
	#login = input("digite algo: ")
	#print("O que voce digitou foi: %s" %(login))
	#var = login
	#print("Imprimindo var: %s" %(var))
	#time.sleep(1)
	#bot.send_message(cid, var)
	bot.register_next_step_handler(msg,process_usuario_step) # Chamar o proximo passo


def process_usuario_step(message):
	try:
		usuario = message.text # Armazenamento do input do usuario no telegram 
		print('Imprimindo usuario : %s' %(usuario))
		msg = bot.reply_to(message,'Qual sua senha?')
		bot.register_next_step_handler(msg,process_senha_step)
		
		
	except Exception as e: # O uso do try except é porque dos outros jeitos estava dando muitos bugs
		bot.reply_to(message,e)


def process_senha_step(message):
	try:
		senha = message.text # Aramazenamento do inputo da senha no telegram
		print('Imprimindo senha : %s' %(senha))
		msg = bot.reply_to(message,'Proseguir? /yes ou /no?')
		bot.register_next_step_handler(msg,process_siga_step)
	except Exception as e:
		bot.reply_to(message,e)
	

def process_siga_step(message): # execução do programa de imprimir documentos via Sigaa. Tambem esta dentro do try except por causa de bugs
	try:
		mensagem_usuario= "180122908" # Aqui tem que ser uma variavel
		mensagem_senha= "Kalmar91" # Aqui tem que ser uma variavel
		options = webdriver.ChromeOptions()
		options.add_argument('lang=pt-br')
		driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
		driver.get('https://sig.unb.br/sigaa/portais/discente/discente.jsf')
		time.sleep(2)
		caixa_usuario = driver.find_element_by_id('username')
		time.sleep(1)
		caixa_usuario.click()
		caixa_usuario.send_keys(mensagem_usuario)
		time.sleep(1)
		caixa_senha = driver.find_element_by_id('password')
		time.sleep(1)
		caixa_senha.click()
		caixa_senha.send_keys(mensagem_senha)
		time.sleep(1)
		botao_enviar = driver.find_element_by_xpath("//button[@name='submit']")
		time.sleep(1)
		botao_enviar.click()
		time.sleep(3)
		achar_matricula = driver.find_element_by_xpath("//*[@id='menu_form_menu_discente_j_id_jsp_340461267_98_menu']/table/tbody/tr/td[1]/span[2]")
		achar_matricula.click()
		time.sleep(1)
		matricula_vinculada = driver.find_element_by_xpath("//*[@id='cmSubMenuID1']/table/tbody/tr[5]") # Para acessar outros documentos basta acrescentar ou subtrair um numero no "tr[]""
		matricula_vinculada.click()
		time.sleep(1)
	except Exception as e:
		bot.reply_to(message,e)	

bot.polling()





