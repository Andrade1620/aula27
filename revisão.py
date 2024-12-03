#LER ENTRADAS DO USUÁRIO
cont = 0#variavel que controla a repetição
escolha_usuario= int(input())#variavel que guarda quantas vezes o código vai rodar
while cont < escolha_usuario:
    nome= input("Digite o nome do aluno:")#ARMAZENA o nome do aluno
    print(nome)
    nota1=float(input("Digite a primeira nota:"))#4 notas do aluno
    nota2=float(input("Digite a segunda nota:"))
    nota3=float(input("Digite a terceira nota:"))
    nota4=float(input("Digite a quarta nota:"))

    faltas= int(input("Digite a quantidade de faltas do aluno:"))
    #calculo da média
    media= (nota1+nota2+nota3+nota4)/4
    print(media)
    if media >=8:
        situacao="Você está aprovado!"
    elif media >=5:
        recuperacao= float(input())
        if recuperacao >=(10-media):
            situacao= "Aprovado na recuperação!"
        else:
            situacao= "REPROVADO na RECUPERAÇÃO!"
    else:
        situacao= "REPROVADO por média!"
    #RELATORIO
    print("Nome: ", nome)
    print("Notas: ", nota1, nota2, nota3, nota4)
    print("Faltas: ", faltas)
    print("Media: ", media)
    print("Situacao: ", situacao)
cont = cont + 1
