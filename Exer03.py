navio=''

result=''
while (navio!='sair'):

    navio = input('Digite o navio:')

    if (navio=='sair'):

        break
		
    lati = input ('Digite a latitude: ')
    long = input ('Digite a longitude: ')
    hora = input ('Digite a hora: ')
	
	
    result += '\n'+ navio + '\t' +  lati + '\t' + long  + '\t' + hora
f=open("file1",'w')

f.write('navio\tlatitude\tlongitude\thora' + result)

f.close()