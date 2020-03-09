from library import *

if __name__ == "__main__":
	dic = intro()
	sai_som("How can I help you?")

	while True:
#		sai_som("How can I help you?")
		query = takeCommand().lower()

		# Logic for executing tasks based on query
		if 'wikipedia' in query:
			if query.startswith('wikipedia '):
				pesquisa = query.split("wikipedia ")
			if query.startswith('Wikipedia '):
				pesquisa = query.split("Wikipedia ")
			query = pesquisa[1]
			if query.startswith('for '):
				query = query.replace("for ", "")
			print('Searching in Wikipedia for {}...'.format(query))
			sai_som2('Searching in Wikipedia for {}...'.format(query))
			results = wikipedia.summary(query, sentences=2)
			sai_som("This may take some time...")
			sai_som("According to Wikipedia\n\n")
			print(results + "\n\n")
			sai_som2(results)
			sai_som('Would you like for me to do something else?')

		elif 'open youtube' in query:
			sai_som('Opening Youtube...')
			webbrowser.open('http://www.youtube.com', 2)


		elif 'search' and 'on youtube' in query:
			youtube_search(query)

		elif 'search' and 'on the web' in query:
			web_search(query)


		elif 'open google' in query:
			sai_som('Opening web browser...')
			webbrowser.open('http://www.google.com', 2)

		elif 'open whatsapp' in query:
			sai_som('Opening WhatsApp web...')
			webbrowser.open('https://web.whatsapp.com/', 2)

		elif 'open github' in query:
			sai_som('Opening GitHub...')
			webbrowser.open('https://github.com/', 2)

		elif 'open your directory in github' in query:
			sai_som('Opening my directory in GitHub...')
			webbrowser.open('https://github.com/MigasEustaquio/Assistente-Virtual', 2)


		elif 'remind me' in query:
			reminder(query)
			sai_som("Is there anything else I can help you with?")


		elif 'agenda' in query:
			verifica_calendario(query)
			sai_som("Is there anything else I can help you with?")
			






#		elif 'play music' in query:
#			music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#			songs = os.listdir(music_dir)
#			print(songs)    
#			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'what' and 'time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(f"It's {strTime}")
			sai_som2(f"It's {strTime}")

#		elif 'open code' in query:
#			codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#			os.startfile(codePath)

		elif query in dic:
			fala = ""
			while fala == "":
				fala = choice(dic[query])
			sai_som(fala)

		else:
#			if query != 'none':
			sai_som("I'm sorry, I don't know what that means.")







