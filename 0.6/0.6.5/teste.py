import json
import datetime


def escrever_json(lista, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)




if __name__ == "__main__":

	data = datetime.datetime.now().strftime("%D")
	print(data)











