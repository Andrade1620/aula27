#LER ENTRADAS DO USUÁRIO
cont = 0#variavel que controla a repetição
escolha_usuario= int(input("Digite a quantidade de alunos que você deseja cadastrar:"))#variavel que guarda quantas vezes o código vai rodar
alunos = [] #lista que armazenará todos os alunos cadastrados
while cont < escolha_usuario:
    nome= input("Digite o nome do aluno:")#ARMAZENA o nome do aluno
    nota1=float(input("Digite a primeira nota:"))#4 notas do aluno
    nota2=float(input("Digite a segunda nota:"))
    nota3=float(input("Digite a terceira nota:"))
    nota4=float(input("Digite a quarta nota:"))

    faltas= int(input(f"Digite a quantidade de faltas o {nome} tem:"))
    #calculo da média
    media= (nota1+nota2+nota3+nota4)/4
    print(media)
    if media >=8:
        situacao="Aprovado acima da média!"
    elif media >=5:
        recuperacao= float(input("digite a nota da recuperação:"))
        if recuperacao >=(10-media):
            situacao= "Aprovado na recuperação!"
        else:
            situacao= "REPROVADO na RECUPERAÇÃO!"
    else:
        situacao= "REPROVADO por média!"
    #enviar os dados do aluno para a lista alunos
    alunos.append([nome, faltas, media, situacao])
    cont =+ 1
    #RELATORIO
print(alunos)