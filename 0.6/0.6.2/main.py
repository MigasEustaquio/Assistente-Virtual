from library import *

def assistente():

	sleep_count = 0

	while True:

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
			print(f"It's {strTime}")
			sai_som2(f"It's {strTime}")


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

		elif 'return' in query or 'bye-bye' in query or 'goodbye' in query or 'see you later' in query or 'see ya later' in query:
			sai_som("Goodbye!")
			return


		else:
			sleep_count = sleep_count + 1
			sai_som("I'm sorry, I don't know what that means.")



if __name__ == "__main__":

	primeira_entrada = 0

	dic = intro()
	while True:
		if primeira_entrada == 0:
			primeira_entrada = 1
			sai_som("How can I help you?")
			assistente()
		query = takeCommand().lower()
		if 'ava' in query or 'deva' in query:
			sai_som(choice(dic["introduction"]))
			assistente()










