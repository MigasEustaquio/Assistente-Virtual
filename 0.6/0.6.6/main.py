from library import *

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

	tempo = 2

	timer = Thread_class(tempo)
	timer.start()


	while timer.isAlive():

		print("\nTip: If you need some help, just say it!\n")

		query = takeCommand().lower()

		# Logic for executing tasks based on query
		if 'wikipedia' in query or 'what is' in query:
			timer.set_tempo(tempo)
			wikipedia_search(query)

		elif 'open youtube' in query:
			timer.set_tempo(tempo)
			sai_som('Opening Youtube...')
			webbrowser.open('http://www.youtube.com', 2)


		elif 'search' and 'on youtube' in query:
			timer.set_tempo(tempo)
			youtube_search(query)

		elif 'search' and 'on the web' in query:
			timer.set_tempo(tempo)
			web_search(query)

		elif 'open google' in query:
			timer.set_tempo(tempo)
			sai_som('Opening web browser...')
			webbrowser.open('http://www.google.com', 2)

		elif 'open whatsapp' in query:
			timer.set_tempo(tempo)
			sai_som('Opening WhatsApp web...')
			webbrowser.open('https://web.whatsapp.com/', 2)

		elif 'open github' in query:
			timer.set_tempo(tempo)
			sai_som('Opening GitHub...')
			webbrowser.open('https://github.com/', 2)

		elif 'open your directory in github' in query:
			timer.set_tempo(tempo)
			sai_som('Opening my directory in GitHub...')
			webbrowser.open('https://github.com/MigasEustaquio/Assistente-Virtual', 2)


		elif 'remind me' in query:
			timer.set_tempo(tempo)
			reminder(query)
			sai_som("Is there anything else I can help you with?")


		elif 'agenda' in query:
			timer.set_tempo(tempo)
			verifica_calendario(query)
			sai_som("Is there anything else I can help you with?")
			


#		elif 'play music' in query:
#			music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#			songs = os.listdir(music_dir)
#			print(songs)    
#			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'what' and 'time' in query:
			timer.set_tempo(tempo)
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(f"It's {strTime}\n")
			sai_som2(f"It's {strTime}")
			sai_som("Is there anything else I can help you with?")


		elif 'notification' in query:	##TESTE
			timer.set_tempo(tempo)
			notification(query)
			sai_som("Is there anything else I can help you with?")


		elif 'news' in query:
			timer.set_tempo(tempo)
			news()
			sai_som("Is there anything else I can help you with?")


		elif 'command' in query:
			timer.set_tempo(tempo)

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

			sai_som("Is there anything else I can help you with?")

		elif 'shutdown' in query or 'shut down' in query:
			shutdown()
			sai_som("Is there anything else I can help you with?")


		elif 'help' in query:
			timer.set_tempo(tempo)
			helper()
			sai_som("Is there anything else I can help you with?")


		elif query in dic:
			timer.set_tempo(tempo)
			fala = ""
			while fala == "":
				fala = choice(dic[query])
			sai_som(fala)

		elif 'return' in query or 'bye-bye' in query or 'goodbye' in query or 'see you later' in query or 'see ya later' in query or 'sleep' in query:
			break


		elif query == 'none':
			print("\n")


		else:
			timer.set_tempo(tempo)
			sai_som("I'm sorry, I don't know what that means.")



	sai_som("If you need anything you just have to call me! Goodbye!")



if __name__ == "__main__":

	dic = intro()
	sleep_mode()










