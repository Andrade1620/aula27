#LER ENTRADAS DO USUÁRIO
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
    print("Você está aprovado!")
elif media >=5:
    print("Você está na recuperação!")
elif media <5:
    print("Você está REPROVADO!")
if faltas >30:
    print("Você está REPROVADO pela quantidade de faltas!")
