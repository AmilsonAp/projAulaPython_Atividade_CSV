import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["atividade_CVS"]
mycol = mydb["dados_CSV"]

numero = []
modalidade = []
unidadeGestora = []
situacao = []
objeto = []
opcao = None

with open('licitacoes_2021.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')
    for i, linha in enumerate(arquivo_csv):
        item = ''.join(linha)
        numero.append(item.split(';')[0])
        modalidade.append(item.split(';')[1])
        unidadeGestora.append(item.split(';')[2])
        situacao.append(item.split(';')[3])
        objeto.append(item.split(';')[4])


#for i, dado in enumerate(numero):
    #mycol.insert_one({'NUMERO' : numero[i], 'MODALIDADE': modalidade[i], 'UNID. GESTORA': unidadeGestora[i],
                      #'SITUACAO': situacao[i], 'OBJETO': objeto[i]})

while opcao != 0:
    print("#### ESCOLHA UMA DAS OPÇÕES ABAIXO ####")
    print("1 - Consultar NUMERO")
    print("2 - Consultar MODALIDADE")
    print("3 - Consultar UNID. GESTORA")
    print("4 - Consultar SITUACAO")
    print("5 - Consultar OBJETO")
    print("0 - SAIR")

    opcao = int(input())

    if opcao == 0:
        print("PROGRAMA ENCERRADO")
    else:
        if opcao == 1:
            for x in mycol.find({}, {"_id": 0, "NUMERO": 1}):
                print(x)
            print("ESCOLHA UMA OPÇÃO")
            print("1 - Gerar Arquivo NUMEROS")
            print("0 - SAIR")
            opcao = int(input())
            if opcao == 1:
                arquivo = open('arquivos/NUMEROS.txt', 'w')
                for obj1 in numero:
                    arquivo.writelines(str(obj1) + "\n")
                arquivo.close()
            if opcao == 0:
                print("PROGRAMA FINALIZADO")
        elif opcao == 2:
            for x in mycol.find({}, {"_id": 1, "MODALIDADE": 1}):
                print(x)
            print("ESCOLHA UMA OPÇÃO")
            print("1 - Gerar Arquivo MODALIDADE")
            print("0 - SAIR")
            opcao = int(input())
            if opcao == 1:
                arquivo = open('arquivos/MODALIDADE.txt', 'w')
                for obj2 in modalidade:
                    arquivo.writelines(str(obj2) + "\n")
                arquivo.close()
            if opcao == 0:
                print("PROGRAMA FINALIZADO")
        elif opcao == 3:
            for x in mycol.find({}, {"_id": 2, "UNID. GESTORA": 1}):
                print(x)
            print("ESCOLHA UMA OPÇÃO")
            print("1 - Gerar Arquivo UNID. GESTORA")
            print("0 - SAIR")
            opcao = int(input())
            if opcao == 1:
                arquivo = open('arquivos/UNIDIDADE_GESTORA.txt', 'w')
                for obj3 in unidadeGestora:
                    arquivo.writelines(str(obj3) + "\n")
                arquivo.close()
            if opcao == 0:
                print("PROGRAMA FINALIZADO")
        elif opcao == 4:
            for x in mycol.find({}, {"_id": 3, "SITUACAO": 1}):
                print(x)
            print("ESCOLHA UMA OPÇÃO")
            print("1 - Gerar Arquivo SITUACAO")
            print("0 - SAIR")
            opcao = int(input())
            if opcao == 1:
                arquivo = open('arquivos/SITUAÇÃO.txt', 'w')
                for obj4 in situacao:
                    arquivo.writelines(str(obj4) + "\n")
                arquivo.close()
            if opcao == 0:
                print("PROGRAMA FINALIZADO")
        elif opcao == 5:
            for x in mycol.find({}, {"_id": 4, "OBJETO": 1}):
                print(x)
            print("ESCOLHA UMA OPÇÃO")
            print("1 - Gerar Arquivo OBJETO")
            print("0 - SAIR")
            opcao = int(input())
            if opcao == 1:
                arquivo = open('arquivos/OBJETO.txt', 'w')
                for obj5 in objeto:
                    arquivo.writelines(str(obj5) + "\n")
                arquivo.close()
            if opcao == 0:
                print("PROGRAMA FINALIZADO")
        else:
            print("#### OPÇÃO INVÁLIDA ####")
            print("ESCOLHA UMA OPÇÃO")
            print("1 - Voltar a tela de Consulta")
            print("0 - SAIR")
            opcao = int(input())

