def calPor(total, parcial):
    return ((100 * parcial) / total);

def calMega(valor):
    return (valor/1024/1024);

lines = [];
with open('./usuarios.txt', 'r') as usuarios:
    lines = usuarios.readlines();


relatorio = [];
tamanhoTotal = 0;
idUser = 0;
for line in lines:
    striredLine = line.strip();
    nomeUsuario = striredLine[0:15];
    tamanhoBytesStr = striredLine[15:];
    tamanhoBytes = int(tamanhoBytesStr);
    tamanhoTotal += tamanhoBytes;
    idUser += 1;
    relatorio.append({ 'nome': nomeUsuario, 'valor': tamanhoBytes, 'id': idUser });

for rel in relatorio:

    porcentagem = float("{0:.2f}".format(calPor(tamanhoTotal, rel['valor'])));
    rel['percentual'] = porcentagem;

    valor = float("{0:.2f}".format(calMega(rel['valor'])));
    rel['valor'] = valor;

with open('./relatorio.txt', 'w') as relatoriofile:
    relatoriofile.write('ACME Inc.                  Uso do espaço em disco pelos usuários\n');
    relatoriofile.write('----------------------------------------------------------------\n');
    relatoriofile.write('Nr.       Usuário        Espaço utilizado             % do uso\n\n');

    for rel in relatorio:
        relatoriofile.write(str(rel['id']));
        relatoriofile.write(' ' * 9);
        relatoriofile.write(rel['nome']);
        relatoriofile.write(' ' * (7 - len(str(rel['valor']))));
        relatoriofile.write(str(rel['valor']));
        relatoriofile.write(' MB');
        relatoriofile.write(' ' * 21);
        relatoriofile.write(' ' * (5 - len(str(rel['percentual']))));
        relatoriofile.write(str(rel['percentual']));
        relatoriofile.write('%\n');

    totalMega = calMega(tamanhoTotal);
    total = float("{0:.2f}".format(totalMega));
    medio = float("{0:.2f}".format(totalMega/len(relatorio)));

    relatoriofile.write('\nEspaço total ocupado: ' + str(total) + ' MB');
    relatoriofile.write('\nEspaço médio ocupado: ' + str(medio) + ' MB');
