"""

def ler_dicionario(endereco):
	with open(endereco, "r") as anexo:
		dic = {}
		for linha in anexo.readlines():
			dicionario = linha.split("']")
			del dicionario[len(dicionario)-1]
			for frases in dicionario:
				val = frases.split("':")
				chave = val[0]
				if chave.startswith("{'"):
					chave = chave.replace("{'", "")
				elif chave.startswith(", '"):
					chave = chave.replace(", '", "")
				val[1] = val[1].replace(" [", " ")
				del val[0]
				for vetor in val:
					frase = vetor.split("', '")
					if len(frase) == 1:
						frase[0] = frase[0].replace(" '", "")
					for i in range(0, len(frase)-1):
						frase[i] = frase[i].replace(" '", "")
					dic[chave] = frase
	return dic
"""


def ler_dicionario(endereco):
	with open(endereco, "r") as anexo:
		dic = {}
		for linha in anexo.readlines():
			dicionario = linha.split("]")
			del dicionario[len(dicionario)-1]
			for frases in dicionario:
				val = frases.split(":")
				chave = val[0]
				if chave.startswith("{'"):
					chave = chave.replace("{'", "")
					chave = chave.replace("'", "")
				elif chave.startswith('{"'):
					chave = chave.replace('{"', '')
					chave = chave.replace('"', '')
				elif chave.startswith(", '"):
					chave = chave.replace(", '", "")
					chave = chave.replace("'", "")
				elif chave.startswith(', "'):
					chave = chave.replace(', "', '')
					chave = chave.replace('"', '')

				val[1] = val[1].replace(" [", "")
				del val[0]
				final = []
				for vetor in val:
					if "', " in vetor:
						frase = vetor.split("', ")
						for novo in frase:
							if '", ' in frase:
								novo2 = novo.split('", ')
								final.append(novo2)
							else:
								final.append(novo)
					elif '", ' in vetor:
						final = vetor.split('", ')
					for i in range(0, len(final)):
						if final[i].startswith("'"):
							final[i] = final[i].replace("'", "")
						if final[i].startswith('"'):
							final[i] = final[i].replace('"', '')

					dic[chave] = final
	return dic

def gravar_dicionario(dic, endereco):

	arquivo = open(endereco, 'w')
	arquivo.write(str(dic))
	arquivo.close()


if __name__ == "__main__":
	dic = ler_dicionario('dados/conversas.txt')

	print(dic)
	print("\n\n\n")

	dic["final test"] = ["it's done", 'it worked', "that's great", 'nice', "I'm awesome"]

	gravar_dicionario(dic, 'dados/conversas.txt')

	print(dic)
	print("\n\n\n")

	dic = ler_dicionario('dados/conversas.txt')

	print(dic)








