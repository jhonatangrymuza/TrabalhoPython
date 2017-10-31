'''usar o mesmo arquivo contido nos arquivos usar o arquivo ip'''
arq = open("ip.txt", 'r')
lista = arq.readlines()

for i in lista:
    print (i.strip())
