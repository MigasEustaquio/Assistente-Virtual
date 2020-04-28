from config import *

def ordena_calendario():

	dic = carregar_json('dados/calendario.json')
	base = carregar_json('dados/base.json')
	dic_ordenado = sorted(dic)

	i=0
	while i<len(dic):
		base[dic_ordenado[i]] = dic[dic_ordenado[i]]
		i = i + 1

	escrever_json(base, 'dados/calendario.json')


def salva_calendario(query, data):
	today = 0
	
	calendario = carregar_json('dados/calendario.json')
	eventos = carregar_json('dados/eventos.json')

	numeroEventos = int(calendario["0"])

	if data == "today":
		today = 1

	data = datetime.datetime.now().strftime("%D")
	day = data.split("/")

	if today == 1:
		day[1] = str(int(day[1])-1)

	if int(day[1])+1 < 10:
		day[1] = "0" + str(int(day[1])+1)
	else:
		day[1] = str(int(day[1])+1)


	data = day[0] + "/" + day[1] + "/" + day[2]


	numeroEventos = numeroEventos + 1

	calendario["0"] = numeroEventos


	try:
		calendario[data] = calendario[data] + [numeroEventos]

	except:
		calendario[data] = [numeroEventos]

	eventos[numeroEventos] = [query]

	if today == 1:

		while True:
			sai_som("Would you like me to notify you at the time?")
			answer = takeCommand().lower()

			if 'ye' in answer or 'ok' in answer or 'sure' in answer:
				notification(query)
				break

			elif 'none' in answer:
				sai_som("I'm sorry, I didn't understand that")

			elif 'no' in answer:
				sai_som("Okay. I've just saved it in your agenda then.")
				break

			else:
				sai_som("I'm sorry, I didn't understand that")


	else:
		sai_som2("Okay. I will remind you " + query + " tomorrow")
		print("Ava: Okay. I will remind you " + query + " tomorrow\n")


	escrever_json(calendario, 'dados/calendario.json')
	escrever_json(eventos, 'dados/eventos.json')
	ordena_calendario()




def salva_calendario_dia(query, data):
	
	calendario = carregar_json('dados/calendario.json')
	eventos = carregar_json('dados/eventos.json')

	numeroEventos = int(calendario["0"])

	if data.startswith("on"):
		data = data.replace("on ", "")

	fala = data
	mes = ""
	dia = ""

	if "january" in data:
		mes = "01"
		x = data.split("ary ")
		data = x[1]

	elif "february" in data:
		mes = "02"
		x = data.split("ary ")
		data = x[1]

	elif "march" in data:
		mes = "03"
		x = data.split("rch ")
		data = x[1]

	elif "april" in data:
		mes = "04"
		x = data.split("ril ")
		data = x[1]

	elif "may" in data:
		mes = "05"
		x = data.split("ay ")
		data = x[1]

	elif "june" in data:
		mes = "06"
		x = data.split("une ")
		data = x[1]

	elif "july" in data:
		mes = "07"
		x = data.split("ly ")
		data = x[1]

	elif "august" in data:
		mes = "08"
		x = data.split("ust ")
		data = x[1]

	elif "september" in data:
		mes = "09"
		x = data.split("ber ")
		data = x[1]

	elif "october" in data:
		mes = "10"
		x = data.split("ber ")
		data = x[1]

	elif "november" in data:
		mes = "11"
		x = data.split("ber ")
		data = x[1]

	elif "december" in data:
		mes = "12"
		x = data.split("ber ")
		data = x[1]

#


	if "s" in data:
		x = data.split("s")
		dia = data[0]

	elif "n" in data:
		x = data.split("n")
		dia = data[0]

	elif "r" in data:
		x = data.split("r")
		dia = data[0]

	elif "th" in data:
		dia = data.replace("th", "")

	if int(dia) < 10:
		dia = "0" + dia

#

	data = mes + "/" + dia + "/20"


	numeroEventos = numeroEventos + 1

	calendario["0"] = numeroEventos


	try:
		calendario[data] = calendario[data] + [numeroEventos]

	except:
		calendario[data] = [numeroEventos]

	eventos[numeroEventos] = [query]

	sai_som2("Okay. I will remind you " + query + " on " + fala)
	print("Ava: Okay. I will remind you " + query + " on " + fala + "\n")


	escrever_json(calendario, 'dados/calendario.json')
	escrever_json(eventos, 'dados/eventos.json')
	ordena_calendario()





def salva_calendario_semana(query, data):	#FUNÇÃO NEXT FALTA IMPLEMENTAR (ex: next saturday)

	calendario = carregar_json('dados/calendario.json')
	eventos = carregar_json('dados/eventos.json')


	numeroEventos = int(calendario["0"])

	if data.startswith("on"):
		data = data.replace("on ", "")

	fala = data
	mes = ""
	dia = ""
	diaSemana = 0

	weekday = datetime.datetime.now().weekday() 

	dataHoje = datetime.datetime.now().strftime("%D")
	day = dataHoje.split("/")
	mes = day[0]
	dia = day[1]


	if "next" in fala:
		print("\n\nTESTE\n\n")

	else:
		if "monday" in data:
			diaSemana = 0

		elif "tuesday" in data:
			diaSemana = 1

		elif "wednesday" in data:
			diaSemana = 2

		elif "thursday" in data:
			diaSemana = 3

		elif "friday" in data:
			diaSemana = 4

		elif "saturday" in data:
			diaSemana = 5

		elif "sunday" in data:
			diaSemana = 6


	if diaSemana > weekday:
		diaSemana = diaSemana - weekday
	else:
		diaSemana = 7 + diaSemana - weekday

	

	x = int(dia) + diaSemana


	if x < 10:

		dia = "0" + str(x)


	elif x > 29:


		if int(mes) == 1 or int(mes) == 3 or int(mes) == 5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(mes) == 12:
			if x > 31:
				mes = str(int(mes) + 1)
				dia = "0" + str(x-31)

		elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
			if x > 30:
				mes = str(int(mes) + 1)
				dia = "0" + str(x-30)

		else:
			if x > 28:
				mes = str(int(mes) + 1)
				dia = "0" + str(x-28)

	else:

		dia = str(x)



	data = mes + "/" + dia + "/20"


	numeroEventos = numeroEventos + 1

	calendario["0"] = numeroEventos


	try:
		calendario[data] = calendario[data] + [numeroEventos]

	except:
		calendario[data] = [numeroEventos]

	eventos[numeroEventos] = [query]

	sai_som2("Okay. I will remind you " + query + " " + fala)
	print("Ava: Okay. I will remind you " + query + " " + fala + "\n")


	escrever_json(calendario, 'dados/calendario.json')
	escrever_json(eventos, 'dados/eventos.json')
	ordena_calendario()



def reminder2(query):

		sai_som('Okay, and when do you want to be reminded?')

		while True:
			data = takeCommand().lower()

			if 'today' in data:
				salva_calendario(query, "today")
				return

			elif "tomorrow" in data:
					
				salva_calendario(query, data)
				return

			elif "day" in data:
					
				salva_calendario_semana(query, data)
				return


			elif "1" in data or "2" in data or "3" in data or "4" in data or "5" in data or "6" in data or "7" in data or "8" in data or "9" in data:

				salva_calendario_dia(query, data)
				return

			elif "nevermind" in data:
				sai_som("Okay")
				return


			else:

				sai_som("I'm sorry, I didn't understand")



def reminder(query):


	if 'something' in query:

		sai_som('Sure, what do you want to be reminded?')


		while True:
			query = takeCommand().lower()

			if query.startswith("remind me"):
				query = query.replace("remind me ", "")

			if query.endswith("please"):
				query = query.replace(" please", "")

			if "remind me" in query:
				fala = query.split("remind me ")
				query = fala[1]

			if "nevermind" in query:
				sai_som("Okay")
				return



			reminder2(query)
			return


#			else:
#				sai_som("I'm sorry, I didn't understand")

	else:

		frase = query.split("remind me ")
		query = frase[1]

		if query.endswith("please"):
			query = query.replace(" please", "")


		reminder2(query)
		return



def verifica_calendario(query): #PERGUNTAR QUANDO NÃO IMPLEMENTADO


	calendario = carregar_json('dados/calendario.json')
	eventos = carregar_json('dados/eventos.json')

	data = datetime.datetime.now().strftime("%D")
	day = data.split("/")



	if 'today' in query:

		try:

			lista_eventos = calendario[data]
			numero_eventos = len(lista_eventos)

			for x in lista_eventos:

				if x > lista_eventos[0]:

					sai_som2("You also asked me to remind you " + eventos[str(x)][0] + " today")
					print("Ava: You also asked me to remind you " + eventos[str(x)][0] + " today\n")
				else:

					sai_som2("You asked me to remind you " + eventos[str(x)][0] + " today")
					print("Ava: You asked me to remind you " + eventos[str(x)][0] + " today\n")



				while True:
					sai_som("Would you like me to notify you about it later?")
					answer = takeCommand().lower()

					if 'ye' in answer or 'ok' in answer or 'sure' in answer:
						notification(query)
						break

					elif 'none' in answer:
						sai_som("I'm sorry, I didn't understand that")

					elif 'no' in answer:
						sai_som("Okay. I'll just keep it in mind then.")
						break

					else:
						sai_som("I'm sorry, I didn't understand that")



			return

		except:
			sai_som("There's nothing on the agenda for today")


	elif 'tomorrow' in query:

		try:

			day = data.split("/")
			data = day[0] + "/" + str(int(day[1])+1) + "/" + day[2]

			lista_eventos = calendario[data]
			numero_eventos = len(lista_eventos)


			for x in lista_eventos:

				if x > lista_eventos[0]:

					sai_som2("You also asked me to remind you " + eventos[str(x)][0] + " tomorrow")
					print("Ava: You also asked me to remind you " + eventos[str(x)][0] + " tomorrow\n")
				else:

					sai_som2("You asked me to remind you " + eventos[str(x)][0] + " tomorrow")
					print("Ava: You asked me to remind you " + eventos[str(x)][0] + " tomorrow\n")

			return

		except:
			sai_som("There's nothing on the agenda for tomorrow")



	elif 'day' in query:

		data =  query

		y = query.split("on ")
		query = y[1]

		weekday = datetime.datetime.now().weekday() 

		dataHoje = datetime.datetime.now().strftime("%D")
		day = dataHoje.split("/")
		mes = day[0]
		dia = day[1]
		diaSemana = 0



		if "next" in query:
			print("\n\nTESTE\n\n")

		else:
			if "monday" in data:
				diaSemana = 0

			elif "tuesday" in data:
				diaSemana = 1

			elif "wednesday" in data:
				diaSemana = 2

			elif "thursday" in data:
				diaSemana = 3

			elif "friday" in data:
				diaSemana = 4

			elif "saturday" in data:
				diaSemana = 5

			elif "sunday" in data:
				diaSemana = 6

		if diaSemana > weekday:
			diaSemana = diaSemana - weekday
		else:
			diaSemana = 7 + diaSemana - weekday


		x = int(dia) + diaSemana


		if x < 10:

			dia = "0" + str(x)


		elif x > 29:


			if int(mes)==1 or int(mes)==3 or int(mes)==5 or int(mes) == 7 or int(mes) == 8 or int(mes) == 10 or int(mes) == 12:
				if x > 31:
					mes = str(int(mes) + 1)
					dia = "0" + str(x-31)

			elif int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11:
				if x > 30:
					mes = str(int(mes) + 1)
					dia = "0" + str(x-30)

			else:
				if x > 28:
					mes = str(int(mes) + 1)
					dia = "0" + str(x-28)

		else:

			dia = str(x)


		data = mes + "/" + dia + "/20"



		try:

			lista_eventos = calendario[data]
			numero_eventos = len(lista_eventos)

			for x in lista_eventos:

				if x > lista_eventos[0]:

					sai_som2("You also asked me to remind you " + eventos[str(x)][0] + " on " + query)
					print("Ava: You also asked me to remind you " + eventos[str(x)][0] + " on " + query + "\n")
				else:

					sai_som2("You asked me to remind you " + eventos[str(x)][0] + " on " + query)
					print("Ava: You asked me to remind you " + eventos[str(x)][0] + " on " + query + "\n")





			return

		except:
			sai_som("There's nothing on the agenda for that day")



	elif "1" in query or "2" in query or "3" in query or "4" in query or "5" in query or "6" in query or "7" in query or "8" in query or "9" in query:

		y = query.split("on ")
		query = y[1]


		mes = ""
		data = query

		if "january" in data:
			mes = "01"
			x = data.split("ary ")
			data = x[1]

		elif "february" in data:
			mes = "02"
			x = data.split("ary ")
			data = x[1]

		elif "march" in data:
			mes = "03"
			x = data.split("rch ")
			data = x[1]

		elif "april" in data:
			mes = "04"
			x = data.split("ril ")
			data = x[1]

		elif "may" in data:
			mes = "05"
			x = data.split("ay ")
			data = x[1]

		elif "june" in data:
			mes = "06"
			x = data.split("une ")
			data = x[1]

		elif "july" in data:
			mes = "07"
			x = data.split("ly ")
			data = x[1]

		elif "august" in data:
			mes = "08"
			x = data.split("ust ")
			data = x[1]

		elif "september" in data:
			mes = "09"
			x = data.split("ber ")
			data = x[1]

		elif "october" in data:
			mes = "10"
			x = data.split("ber ")
			data = x[1]

		elif "november" in data:
			mes = "11"
			x = data.split("ber ")
			data = x[1]

		elif "december" in data:
			mes = "12"
			x = data.split("ber ")
			data = x[1]


# (verificar se a variável 'dia' não deveria receber x[0] ao invés de data[0])


		if "s" in data:
			x = data.split("s")
			dia = data[0]

		elif "n" in data:
			x = data.split("n")
			dia = data[0]

		elif "r" in data:
			x = data.split("r")
			dia = data[0]

		elif "th" in data:
			dia = data.replace("th", "")

		if int(dia) < 10:
			dia = "0" + dia

#

		data = mes + "/" + dia + "/20"


		try:

			lista_eventos = calendario[data]
			numero_eventos = len(lista_eventos)


			for x in lista_eventos:

				if x > lista_eventos[0]:

					sai_som2("You also asked me to remind you " + eventos[str(x)][0] + " on " + query)
					print("Ava: You also asked me to remind you " + eventos[str(x)][0] + " on " + query + "\n")
				else:

					sai_som2("You asked me to remind you " + eventos[str(x)][0] + " on " + query)
					print("Ava: You asked me to remind you " + eventos[str(x)][0] + " on " + query + "\n")

			return

		except:
			sai_som("There's nothing on the agenda for that day")
			return


	else:
		sai_som("I'm sorry, I didn't understand")
		return




def notification_thread(frase, hora, minuto):

	hora_atual = int(datetime.datetime.now().strftime("%H"))
	minuto_atual = int(datetime.datetime.now().strftime("%M"))

	time.sleep((((hora - hora_atual)*60)+(minuto-minuto_atual))*60)

	sai_som2("Excuse me " + name +".")
	print("Excuse me " + name +".")

	if minuto < 10:
		sai_som2("You asked me to remind you " + frase + " at " + str(hora) + ":0" + str(minuto))
		print("You asked me to remind you " + frase + " at " + str(hora) + ":0" + str(minuto) + "\n")
	else:
		sai_som2("You asked me to remind you " + frase + " at " + str(hora) + ":" + str(minuto))
		print("You asked me to remind you " + frase + " at " + str(hora) + ":" + str(minuto) + "\n")



def notification(frase):

	hora = 0
	minuto = 0

	while True:

		sai_som("At what time do you want to be remembered?")

		query = takeCommand().lower()


		if "0" in query or "1" in query or "2" in query or "3" in query or "4" in query or "5" in query or "6" in query or "7" in query or "8" in query or "9" in query: 

			if " " in query:
				x = query.split(" ")
				query = x[(len(x)-1)]

			if ":" in query:
				x = query.split(":")
				hora = int(x[0])
				minuto = int(x[1])
			else:
				if len(query) < 3:
					hora = int(query)

				elif len(query) < 4:
					hora = int(query[0])
					x = query.split(query[0])
					minuto = int(x[1])

				else:
					x = query.split(query[1])
					y = query.split(query[2])
					hora = int(y[0])
					minuto = int(x[1])

			if hora > 23:
				sai_som("I'm sorry, but I can't notify you at that time")



			elif int(datetime.datetime.now().strftime("%H")) < hora or int(datetime.datetime.now().strftime("%H")) == hora and int(datetime.datetime.now().strftime("%M")) < minuto:
				

				sai_som2("I will notify you about " + frase + " at " + str(hora) + ":" + str(minuto))
				print("Ava: I will notify you about " + frase + " at " + str(hora) + ":" + str(minuto) + "\n")

				t = threading.Thread(target=notification_thread, args=(frase, hora, minuto))
				t.start()

				return

			else:
				sai_som("I can't notify at " + hora + ":" + minuto + " because that time has already passed.")


		elif "return" in query:
			return

		else:
			sai_som("I'm sorry, I didn't understand")



def helper():

	dic = carregar_json('dados/helper.json')
	sai_som("Sure, what do you need help with? If you're kinda lost just say general.")

	while True:
		query = takeCommand().lower()


		if 'general' in query:

			print("Ava: " + dic["general"] + "\n")

			try:
				playsound("audios/{}.mp3".format("general"))

			except:

				tts = gTTS(dic["general"],lang='en-us')
				#Salva o arquivo de audio
				tts.save("audios/{}.mp3".format("general"))
				#Da play ao audio
				playsound("audios/{}.mp3".format("general"))

			return

		elif 'command' in query:

			print("Ava: " + dic["commands"] + "\n")

			try:
				playsound("audios/{}.mp3".format("commands"))

			except:

				tts = gTTS(dic["commands"],lang='en-us')
				#Salva o arquivo de audio
				tts.save("audios/{}.mp3".format("commands"))
				#Da play ao audio
				playsound("audios/{}.mp3".format("commands"))

			print(dic["command_list"])

			return



		elif 'remind' in query:
			sai_som(dic["remind"])
			return


		elif 'agenda' in query:
			sai_som(dic["agenda"])
			return





		else:
			sai_som("I'm sorry, I didn't understand")
			return


def daily_agenda(today):

	sai_som("Would you like to hear your agenda for the day?")

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


					while True:
						sai_som("Would you like me to notify you about it later?")
						answer = takeCommand().lower()

						if 'ye' in answer or 'ok' in answer or 'sure' in answer:
							notification(query)
							break

						elif 'none' in answer:
							sai_som("I'm sorry, I didn't understand that")

						elif 'no' in answer:
							sai_som("Okay. I'll just keep it in mind then.")
							break

						else:
							sai_som("I'm sorry, I didn't understand that")



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


def news():

	sai_som("This function is experimental. Are you sure you want to continue?")
	query = takeCommand().lower()
	if 'yes' in query:
		i=0
	else:
		return

	news_url="https://news.google.com/news/rss"
	Client=urlopen(news_url)
	xml_page=Client.read()
	Client.close()

	soup_page=soup(xml_page,"xml")
	news_list=soup_page.findAll("item")
	# Print news title, url and publish date
	i=0
	for news in news_list:
		if i > 3:
			break
		if 'Trump' in news.title.text:
			i=i
		else:
			print(news.title.text)
			print(news.link.text)
#			print(news.pubDate.text)
			print("-"*60)
			sai_som2(news.title.text)
			i=i+1


def shutdown():

	count = 0

	while True:

		if count > 1:
			sai_som("Shutdown canceled.")
			return

		sai_som("Are you sure you want me to shutdown?")

		query = takeCommand().lower()

		if 'yes'in query:
			sai_som("Shutting down all systems...")
			sys.exit()

		elif 'none' in query:
			count = count + 1

		else:
			sai_som("Shutdown canceled.")
			return


