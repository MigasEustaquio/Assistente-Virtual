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
					for i in range(0, len(frase)-1):
						frase[i] = frase[i].replace(" '", "")
					dic[chave] = frase
	return dic

def gravar_dicionario(dic, endereco):

	arquivo = open(endereco, 'w')
	arquivo.write(str(dic))
	arquivo.close()




if __name__ == '__main__':
	dic = ler_dicionario('./teste2.txt')
	gravar_dicionario(dic, './teste3.txt')
	dic2 = ler_dicionario('./teste3.txt')
	if dic == dic2:
		print("sucesso")



