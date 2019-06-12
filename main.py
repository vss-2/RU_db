lerArquivo = open('jantas.txt', 'r')

try:
    entrada = input()
    
    # Entrada pode ser no formato:
    # adicionar X, sendo X inteiro
    # remover
    
    if (entrada[1] == 'adicionar'):
        valorAntigo = lerArquivo.read()
        valorAntigo = int(valorAntigo.replace('\n',''))
        valorNovo = int(entrada[2])
        valorNovo = valorAntigo + valorNovo
    else:
        # Caso de remover
        valorAntigo = lerArquivo.read()
        valorAntigo = int(valorAntigo.replace('\n',''))
        valorNovo = valorAntigo - 1
    
    escArquivo = write('jantas.txt', 'w+')
    escArquivo.write(valorNovo)
    escArquivo.close()
    
    if(valorNovo == 1):
        print('Atencao, esta e sua penultima janta')
    elif(valorNovo == 0):
        print('Atencao, esta foi sua ultima janta')

except NameError:
    pass
