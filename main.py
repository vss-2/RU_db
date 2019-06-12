lerArquivo = open('jantas.txt', 'r')

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
    
    escArquivo = write('jantas.txt', 'w')
    escArquivo.write(valorNovo)
    escArquivo.close()
    
    if(valorNovo == 1):
        print('Atencao, esta e sua penultima janta')
    elif(valorNovo == 0):
        print('Atencao, esta foi sua ultima janta')
        
    exit()

except NameError:
    pass
