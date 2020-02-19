# -*- coding: utf-8 -*-
import datetime
from subprocess import call

def input_err(onde):
	print('Trollou o input em\n'+str(onde)+'\ntente novamente!')
	return

def verQnt():
	lerArquivo = open('jantas.txt', 'r')
	qnt_Jantas = int(lerArquivo.readline(1))
	return qnt_Jantas

def escQnt(num):
	call(['touch', 'jantas.txt'])
	escArquivo = open('jantas.txt', 'w')
	escArquivo.write(num)
	escArquivo.close()
	return

def adicionarJantas():
	qnt_Jantas = verQnt()
	adc_Jantas = input('Quantas jantas devo adicionar a quantidade ('+str(qnt_Jantas)+') existente?')
	
	if(type(adc_Jantas) == type(0)):
		escQnt(int(adc_Jantas)+int(qnt_Jantas))
	else:
		input_err('Ao inserir a quantidade de jantas, você não colocou um inteiro')
	return

def removerJantas():
	qnt_Jantas = verQnt()
	qnt_Jantas -= 1

	bool_Hoje = input('É hoje ou não (insira s ou o dia(int))')
	data = datetime.datetime.now()

	if(bool_Hoje.lower() == 's'):
		dia  = int(data.strftime('%d'))
	elif(type(bool_Hoje) == type(0)):
		dia  = int(bool_Hoje)
	else:
		input_err('Ao inserir algo diferente de s ou o dia em inteiros, na hora de remover')
		
	mes  = int(data.strftime('%m'))
	ano  = int(data.strftime('%Y'))

	if(qnt_Jantas == 1):
		print('Atenção, esta é sua penúltima janta!')
	elif(qnt_Jantas == 0):
		print('Atenção, esta foi sua última janta!')
	lerArquivo.close()
	
	call(['rm', 'jantas.txt'])
	escQnt(qnt_Jantas)
	return

if __name__ == "__main__":
	adc_rmv = input('Deseja adicionar X jantas ou remover 1 janta (adc/rmv)?')

	if(adc_rmv.lower() == 'adc'):
		adicionarJantas()
	elif(adc_rmv.lower() == 'rmv'):
		removerJantas()
	else:
		input_err('Na hora de dizer a quantidade para adicionar ou se é para remover')
	exit
