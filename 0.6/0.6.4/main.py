from library import *

def daily_agenda(today):

	sai_som("Do you want to hear your agenda for the day?")

	while True:

		query = takeCommand().lower()

		if 'ye' in query or 'ok' in query or 'sure' in query:

			eventos = carregar_json('dados/eventos.json')
			calendario = carregar_json('dados/calendario.json')

			try:
				lista_eventos = calendario[today]
				for x in lista_eventos:
					if x > lista_eventos[0]:

						sai_som2("You also asked me to remind you " + eventos[str(x)][0] + " today.")
						print("Ava: You also asked me to remind you " + eventos[str(x)][0] + " today.\n")
					else:

						sai_som2("You asked me to remind you " + eventos[str(x)][0] + " today.")
						print("Ava: You asked me to remind you " + eventos[str(x)][0] + " today.\n")

			except:
				sai_som("There's nothing on your agenda for today")

			return

		elif 'none' in query:
			sai_som("I'm sorry, I didn't understand that")


		elif 'no' in query:
			sai_som("Okay")
			return


		else:
			sai_som("I'm sorry, I didn't understand that")




def sleep_mode():

	primeira_entrada = 0
	horario_antigo = ""
	horario = ""

	while True:

		strTime = datetime.datetime.now().strftime("%H")
		today = datetime.datetime.now().strftime("%D")


		if int(strTime) < 12:
			horario = "Morning"
		elif int(strTime) < 19:
			horario = "Afternoon"
		else:
			horario = "Evening"

		if primeira_entrada == 0:
			primeira_entrada = 1

			daily_agenda(today)		######

			sai_som("Is there anything else I can help you with?")
			horario_antigo = horario
			assistente()
		query = takeCommand().lower()
		if 'ava' in query or 'deva' in query or 'teva' in query:
			if horario == horario_antigo:
				sai_som(choice(dic["introduction"]))

			else:
				sai_som("Good " + horario + " " + name)

				daily_agenda(today)		#######

				sai_som("Is there anything else I can help you with?")
			horario_antigo = horario
			assistente()


def assistente():

	sleep_count = 0

	while True:

		print("Tip: If you need some help, just say it!\n")

		if sleep_count > 2:
			sleep_count = 0
			sai_som("Goodbye!")
			return

		query = takeCommand().lower()

		# Logic for executing tasks based on query
		if 'wikipedia' in query or 'what is' in query:
			sleep_count = 0
			wikipedia_search(query)

		elif 'open youtube' in query:
			sleep_count = 0
			sai_som('Opening Youtube...')
			webbrowser.open('http://www.youtube.com', 2)


		elif 'search' and 'on youtube' in query:
			sleep_count = 0
			youtube_search(query)

		elif 'search' and 'on the web' in query:
			sleep_count = 0
			web_search(query)

		elif 'open google' in query:
			sleep_count = 0
			sai_som('Opening web browser...')
			webbrowser.open('http://www.google.com', 2)

		elif 'open whatsapp' in query:
			sleep_count = 0
			sai_som('Opening WhatsApp web...')
			webbrowser.open('https://web.whatsapp.com/', 2)

		elif 'open github' in query:
			sleep_count = 0
			sai_som('Opening GitHub...')
			webbrowser.open('https://github.com/', 2)

		elif 'open your directory in github' in query:
			sleep_count = 0
			sai_som('Opening my directory in GitHub...')
			webbrowser.open('https://github.com/MigasEustaquio/Assistente-Virtual', 2)


		elif 'remind me' in query:
			sleep_count = 0
			reminder(query)
			sai_som("Is there anything else I can help you with?")


		elif 'agenda' in query:
			sleep_count = 0
			verifica_calendario(query)
			sai_som("Is there anything else I can help you with?")
			



#		elif 'play music' in query:
#			music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#			songs = os.listdir(music_dir)
#			print(songs)    
#			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'what' and 'time' in query:
			sleep_count = 0
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(f"It's {strTime}\n")
			sai_som2(f"It's {strTime}")


		elif 'command' in query:

			dic2 = carregar_json('dados/helper.json')

			print("Ava: " + dic2["commands"] + "\n")

			try:
				playsound("audios/{}.mp3".format("commands"))

			except:

				tts = gTTS(dic2["commands"],lang='en-us')
				#Salva o arquivo de audio
				tts.save("audios/{}.mp3".format("commands"))
				#Da play ao audio
				playsound("audios/{}.mp3".format("commands"))

			print(dic2["command_list"])

			return


		elif 'help' in query:
			sleep_count = 0
			helper()
			sai_som("Is there anything else I can help you with?")


		elif query in dic:
			sleep_count = 0
			fala = ""
			while fala == "":
				fala = choice(dic[query])
			sai_som(fala)

		elif 'return' in query or 'bye-bye' in query or 'goodbye' in query or 'see you later' in query or 'see ya later' in query or 'sleep' in query:
			sai_som("If you need anything you just have to call me! Goodbye!")
			return


		elif query == 'none':
			print("\n")


		else:
			sleep_count = sleep_count + 1
			sai_som("I'm sorry, I don't know what that means.")



if __name__ == "__main__":

	dic = intro()
	sleep_mode()










