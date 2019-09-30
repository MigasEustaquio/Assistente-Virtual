import requests as rq
import webbrowser
import wikipedia

import speech_recognition as sr

from gtts import gTTS
from playsound import playsound

import pyttsx3

from random import choice

version = "0.5.3"
cidade = 'goiânia'
caminho_navegador = "/usr/bin/firefox.sh %s" #ALTERAR CAMINHO DO NAVEGADOR!!

def intro():
	msg = "Assistente - version {} / by: Miguel Eustáquio Silva".format(version)
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))
	sai_som("Initializing")
	dic = ler_dicionario('dados/conversas.txt')
	sai_som("Hello, I'm Xion, your personal virtual assistant.")
#	sai_som("What's your name?")
	return dic

def web_search(query):

	if query.startswith('search'):
		query = query.replace("search ", "")
	else:
		pesquisa = query.split("search ")
		query = pesquisa[1]
	if query.startswith('for'):
		query = query.replace("for ", "")
	pesquisa = query.split(" on the")
	query = pesquisa[0]
	print('Searching {} on the web...'.format(query))
	sai_som2('Searching {} on the web...'.format(query))
	if ' ' in query:
		query = query.replace(" ", "+")
	webbrowser.open('http://www.google.com/search?q={}'.format(query), 2)

def youtube_search(query):

	if query.startswith('search'):
		query = query.replace("search ", "")
	else:
		pesquisa = query.split("search ")
		query = pesquisa[1]
	if query.startswith('for'):
		query = query.replace("for ", "")
	pesquisa = query.split(" on youtub")
	query = pesquisa[0]
	print('Searching {} on Youtube...'.format(query))
	sai_som2('Searching {} on Youtube...'.format(query))
	if ' ' in query:
		query = query.replace(" ", "+")
	webbrowser.open('http://www.youtube.com/results?search_query={}'.format(query), 2)


lista_erros = [
		"I'm sorry, i didn't understand that",
		"Can you repeat, please?"
]

conversas = {
	"Olá": "oi, tudo bem?",
	"sim e você": "Estou bem obrigada por perguntar",
	"hi": "hello, how are you?",
	"I'm fine": "that's great!"
}

comandos = {
	"desligar": "desligando",
	"reiniciar": "reiniciando"
}


def verifica_nome(user_name):
	if user_name.startswith(" "):
		user_name = user_name.replace(" ", "")


	if user_name.startswith("Meu nome é"):
		user_name = user_name.replace("Meu nome é ", "")
	if user_name.startswith("Eu me chamo"):
		user_name = user_name.replace("Eu me chamo ", "")
	if user_name.startswith("Eu sou o"):
		user_name = user_name.replace("Eu sou o ", "")
	if user_name.startswith("Eu sou a"):
		user_name = user_name.replace("Eu sou a ", "")

	if user_name.startswith("my name is"):
		user_name = user_name.replace("my name is ", "")
	if user_name.startswith("name is"):
		user_name = user_name.replace("name is ", "")
	if user_name.startswith("is"):
		user_name = user_name.replace("is ", "")

	if user_name.startswith("when is"):
		user_name = user_name.replace("when is ", "")

	if user_name.startswith("I am"):
		user_name = user_name.replace("I am ", "")
	if user_name.startswith("I'm"):
		user_name = user_name.replace("I'm ", "")
	if user_name.startswith("it's me"):
		user_name = user_name.replace("it's me ", "")
	if user_name.startswith("it's"):
		user_name = user_name.replace("it's ", "")


	return user_name 


def  verifica_nome_exist(nome):
	dados = open("dados/nomes.txt", "r")
	nome_list = dados.readlines()

	if not nome_list:
		nome = new_user(nome)

		vazio = open("dados/nomes.txt", "r")
		conteudo = vazio.readlines()
		conteudo.append("{}".format(nome))
		vazio = open("dados/nomes.txt", "w")
		vazio.writelines(conteudo)
		vazio.close()

		return "Okay. Nice to meet you {}!".format(nome)

	for linha in nome_list:
		if linha == nome:
			return "Hello {}, long time no see!".format(nome)

	nome = new_user(nome)

	vazio = open("dados/nomes.txt", "r")
	conteudo = vazio.readlines()
	conteudo.append("\n{}".format(nome))
	vazio = open("dados/nomes.txt", "w")
	vazio.writelines(conteudo)
	vazio.close()

	return "Okay. Nice to meet you {}!".format(nome)


def name_list():
	try:
		nomes = open("dados/nomes.txt", "r")
		nomes.close()

	except FileNotFoundError:
		nomes = open("dados/nomes.txt", "w")
		nomes.close()


def calcula(entrada):
	if "mais" in entrada or "+" in entrada:
		# É soma
		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) + int(entradas_recebidas[3])

	elif "menos" in entrada or "-" in entrada:
		# É subtração

		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) - int(entradas_recebidas[3])

	elif "vezes" in entrada or "x" in entrada:
		# É vezes

		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) * float(entradas_recebidas[3]), 2)

	elif "dividido" in entrada or "/" in entrada:
		# É divisão

		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) / float(entradas_recebidas[4]), 2)

	else:

		resultado = "Operação não encontrada"


	return resultado



def clima_tempo():	
	endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=0e6b5349cabfe1b7d5c1cf69af0fed90="
	url = endereco_api + cidade

	infos = rq.get(url).json()


	# Coord
	longitude = infos['coord']['lon']
	latitude = infos['coord']['lat']
	# main
	temp = infos['main']['temp'] - 273.15 # Kelvin para Celsius
	pressao_atm = infos['main']['pressure'] / 1013.25 #Libras para ATM
	humidade = infos['main']['humidity'] # Recebe em porcentagem
	temp_max= infos['main']['temp_max'] - 273.15 # Kelvin para Celsius
	temp_min = infos['main']['temp_min'] - 273.15 # Kelvin para Celsius

	#vento
	v_speed = infos['wind']['speed'] # km/ h
	v_direc = infos['wind']['deg'] #Recebe em graus

	#clouds / nuvens

	nebulosidade = infos['clouds']['all']

	#id
	id_da_cidade = infos['id']

	# 11
	return [longitude, latitude, 
		temp, pressao_atm, humidade, 
		temp_max, temp_min, v_speed, 
		v_direc, nebulosidade, id_da_cidade]


def temperatura():
	temp_atual = clima_tempo()[2]
	temp_max = clima_tempo()[5]
	temp_min = clima_tempo()[6]
	
	return [temp_atual, temp_max, temp_min]

#def aprender(fala):


def abrir(fala):
	try:
		if "google" in fala:
			web.get(caminho_navegador).open("google.com.br/")
			return "abrindo google"
		elif "facebook" in fala:
			web.get(caminho_navegador).open("facebook.com.br/")
			return "abrindo facebook"
		else:
			return "site não cadastrado para aberturas"
	except:
		return "houve um erro"


def new_user(nome):

	sai_som("Would you like me to call you {}?".format(nome))

	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					resp = rec.recognize_google(audio, language="en")
					print("You: " + resp)

					if (resp.startswith("yes") or resp.startswith("sure")):

						return nome

					elif (resp.startswith("no")):

						sai_som("What would you rather for me to call you?")

						while True:
							try:
								audio = rec.listen(s)
								resp = rec.recognize_google(audio, language="en")
								print("You: " + resp)
								return new_user(resp)								

							except sr.UnknownValueError:
								sai_som(resposta_erro_aleatoria)
						break


					break
				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)


def sai_som(audio):

	print("Xion: " + audio)

	try:
		playsound("audios/{}.mp3".format(audio))

	except:

		tts = gTTS(audio,lang='en-us')
		#Salva o arquivo de audio
		tts.save("audios/{}.mp3".format(audio))
		#Da play ao audio
		playsound("audios/{}.mp3".format(audio))


def sai_som2(audio):

	tts = gTTS(audio,lang='en-us')
	tts.save("audios/temp_audio.mp3".format(audio))
	playsound("audios/temp_audio.mp3".format(audio))
	tts = gTTS("wikipedia",lang='en-us')
	tts.save("audios/temp_audio.mp3".format(audio))


def ler_dicionario(endereco):
	with open(endereco, "r") as anexo:
		dic = {}
		for linha in anexo.readlines():
			dicionario = linha.split("']")
			del dicionario[len(dicionario)-1]
			for frases in dicionario:
				val = frases.split("':")
				chave = val[0]
				if chave.startswith("{'"):
					chave = chave.replace("{'", "")
				elif chave.startswith(", '"):
					chave = chave.replace(", '", "")
				val[1] = val[1].replace(" [", " ")
				del val[0]
				for vetor in val:
					frase = vetor.split("', '")
					if len(frase) == 1:
						frase[0] = frase[0].replace(" '", "")
					for i in range(0, len(frase)-1):
						frase[i] = frase[i].replace(" '", "")
					dic[chave] = frase
	return dic

def gravar_dicionario(dic, endereco):

	arquivo = open(endereco, 'w')
	arquivo.write(str(dic))
	arquivo.close()


