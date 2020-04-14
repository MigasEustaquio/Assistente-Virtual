import json
import datetime
from random import choice

def escrever_json(arquivo, lista):
    with open(arquivo, 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)




if __name__ == "__main__":


	strDate = datetime.datetime.now().strftime("%D")
	weekday = datetime.datetime.now().weekday()

	print (strDate + "\n\n\n" + str(weekday) + "\n\n\n")

	day = strDate.split("/")

	print(int(day[1])+1)













