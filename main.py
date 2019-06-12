# -*- coding: utf-8 -*-

lerArquivo = open('jantas.txt', 'r')

try:
	try:
		entrada = input()
		entrada = entrada.split(' ')
		
		# Entrada pode ser no formato:
		# adicionar X, sendo X inteiro
		# remover
		valorAntigo = lerArquivo.read()
		
		if (entrada[0] == 'adicionar'):
			valorAntigo = int(valorAntigo.replace('\n',''))
			valorNovo = int(entrada[1])
			valorNovo = valorAntigo + valorNovo
		else: 
		#Caso de remover
			valorAntigo = int(valorAntigo.replace('\n',''))
			valorNovo = valorAntigo - 1

		print('Temos agora, no total:', valorNovo)
		

		escArquivo = open('jantas.txt', 'w')

		output = str(valorNovo) + " "
		escArquivo.write(output)
		escArquivo.close()
		
		if(valorNovo == 1):
			print('Atenção, esta é sua penultima janta')
		elif(valorNovo == 0):
			print('Atenção, esta foi sua última janta')
			
		exit()
		
	except ValueError:
		print('Valor inserido não é inteiro, parando execução')
    
except NameError:
    pass
