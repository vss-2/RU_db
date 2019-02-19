# Pra atualizar o arquivo a partir
# do que está no GitHub
# 'git pull origin master'

# Pega a versao mais atual do github
git pull origin master

# Inicia o python
python

# Abre o arquivo jantas
lerArquivo = open("jantas.txt","r")
escArquivo = read("jantas.txt","w+")
# Le o conteudo do arquivo
quantidade = lerArquivo.read()

if(conteudo == '1')
    print('Aviso: esta é sua última janta')
    escArquivo.write('0')
else
    quantidade = int(quantidade)
    quantidade = quantidade - 1
    escArquivo.write(quantidade)
    
exit()

git push origin master
