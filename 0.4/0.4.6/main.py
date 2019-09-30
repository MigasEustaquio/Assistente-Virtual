from config import *

"""                             #USANDO pyttsx3
reproducao = pyttsx3.init()
reproducao.setProperty('voice', reproducao.getProperty('voices')[53].id) #BR
def sai_som(resposta):			
	reproducao.say(resposta)
	reproducao.runAndWait()


def sai_som(audio):				#USANDO gtts
	tts = gTTS(audio,lang='en-us')
	#Salva o arquivo de audio
	tts.save('audios/hello.mp3')
	#Da play ao audio
	playsound('audios/hello.mp3')
"""

def assistente():
	sai_som("Hello, I'm Xion, your personal virtual assistant.")
	sai_som("What's your name?")

	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					user_name = rec.recognize_google(audio, language="en")
					user_name = verifica_nome(user_name)
					name_list()
					apresentacao = "{}".format(verifica_nome_exist(user_name))

					sai_som(apresentacao)
			
					brute_user_name = user_name
					user_name = user_name.split(" ")
					user_name = user_name[0]
					break
				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)
			break

	dic = ler_dicionario('dados/conversas.txt')
	print("="* len(apresentacao))
	print("Listening...")

	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					entrada = rec.recognize_google(audio, language="en")
					print("{}: {}".format(user_name, entrada))
					"""
					if "aprender" in entrada:            #caso utilize essa função antes mudar o 'if' seguinte para 'elif'
						resposta = aprender(entrada)
"""
					# Abri links no navegador
					if "abrir" in entrada:
						resposta = abrir(entrada)

					# Operações matemáticas
					elif "quanto é" in entrada:

						entrada = entrada.replace("quanto é", "")
						resposta = calcula(entrada)
					# Pede tempo
					elif "qual a temperatura" in entrada:

						lista_tempo = temperatura()
						temp = lista_tempo[0]
						temp_max = lista_tempo[1]
						temp_min = lista_tempo[2]

						resposta = "A temperatura de hoje é {:.2f}º. Temos uma máxima de {:.2f}º e uma minima de {:.2f}º".format(temp, temp_max, temp_min)

					# Informações da cidade
					elif "informações" in entrada and "cidade" in entrada:

						resposta = "Mostrando informações da cidade"
					else:
						if entrada in dic:
							resposta = choice(dic[entrada])
						else:
							resposta = conversas[entrada]

					if resposta == "Mostrando informações da cidade":
						#mostra informações da cidade

						lista_infos = clima_tempo()
						longitude = lista_infos[0]
						latitude = lista_infos[1]
						temp = lista_infos[2]
						pressao_atm = lista_infos[3]
						humidade = lista_infos[4]
						temp_max = lista_infos[5]
						temp_min = lista_infos[6]
						v_speed = lista_infos[7]
						v_direc = lista_infos[8]
						nebulosidade = lista_infos[9]
						id_da_cidade = lista_infos[10]

						print("Mostrando informações de {}\n\n".format(cidade))
						sai_som("Mostrando informações de {}".format(cidade))
						print("Longitude: {}, Latitude: {}\nId: {}\n".format(longitude, latitude, id_da_cidade))
						print("Temperatura: {:.2f}º".format(temp))
						print("Temperatura máxima: {:.2f}º".format(temp_max))
						print("Temperatura minima: {:.2f}º".format(temp_min))
						print("Humidade: {}".format(humidade))
						print("Nebulosidade: {}".format(nebulosidade))
						print("Velocidade do vento: {}m/s\nDireção do vento: {}".format(v_speed,v_direc))

					else:
						sai_som("{}".format(resposta))


				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)
				except KeyError:
					pass


if __name__ == '__main__':
	intro()
	assistente()
