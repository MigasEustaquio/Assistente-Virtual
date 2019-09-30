from config import *

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
        print(f"Miguel: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


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


		elif 'search' and 'on the web' in query:
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


		elif 'open google' in query:
			sai_som('Opening web browser...')
			webbrowser.open('http://www.google.com', 2)

		elif 'open github' in query:
			sai_som('Opening GitHub...')
			webbrowser.open('https://github.com/', 2)


#		elif 'play music' in query:
#			music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#			songs = os.listdir(music_dir)
#			print(songs)    
#			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")    
			sai_som(f"Sir, the time is {strTime}")

#		elif 'open code' in query:
#			codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#			os.startfile(codePath)

		elif query in dic:
			sai_som(choice(dic[query]))

		else:
			if query != 'none':
				sai_som("I'm sorry, I don't know what that means.")

