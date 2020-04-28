import requests as rq
import webbrowser
import wikipedia
import datetime
import time
import json
import sys
import bs4
import threading
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

import speech_recognition as sr

from gtts import gTTS
from playsound import playsound

from random import choice

version = "0.6.5"
name = "Miguel"

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(name + f": {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def intro():
	msg = "Assistant - version {} / by: Miguel Eustáquio Silva".format(version)
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))
	sai_som("Initializing")
	dic = carregar_json('dados/conversas.json')
	sai_som("Hello, I'm Ava, your personal virtual assistant.")
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


def wikipedia_search(query):
		if 'search 'in query:
			pesquisa = query.split("search ")
			query = pesquisa[1]

		if query.endswith(' please'):
			pesquisa = query.split(" please")
			query = pesquisa[0]

		if query.endswith(' in wikipedia'):
			pesquisa = query.split(" in wikipedia")
			query = pesquisa[0]

		if query.endswith(' in Wikipedia'):
			pesquisa = query.split(" in Wikipedia")
			query = pesquisa[0]

		if query.startswith('for '):
			query = query.replace("for ", "")

		if 'what is' in query:
			pesquisa = query.split("what is ")
			query = pesquisa[1]

			if query.startswith('a '):
				query = query.replace("a ", "")
			elif query.startswith('an '):
				query = query.replace("an ", "")


		print('Ava: Searching in Wikipedia for {}...'.format(query))
		sai_som2('Searching in Wikipedia for {}...'.format(query))
		results = wikipedia.summary(query, sentences=2)
		sai_som("This may take some time...")
		sai_som("According to Wikipedia\n\n")
		print(results + "\n\n")
		sai_som2(results)
		sai_som('Would you like for me to do something else?')



"""
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
"""
"""
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
"""
"""
def name_list():
	try:
		nomes = open("dados/nomes.txt", "r")
		nomes.close()

	except FileNotFoundError:
		nomes = open("dados/nomes.txt", "w")
		nomes.close()
"""


#def aprender(fala):


"""
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
"""

def sai_som(audio):

	print("Ava: " + audio + "\n")

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




def escrever_json(lista, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)


