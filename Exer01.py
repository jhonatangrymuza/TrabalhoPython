nome=''

result=''
while (nome!='sair'):

    nome = input('Digite o nome:')

    if (nome=='sair'):

        break

    tel = input ('Digite o telelfone: ')
    result += '\n'+ nome + '\t' +  tel
f=open("file1",'w')

f.write('Nome\tTelefone' + result)

f.close()
f=open('file1','r')
lista = f.readlines()

for i in lista:
    print (i)
f.close()
