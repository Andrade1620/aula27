qtd_aluno = int(input("Digite a quantidade de alunos:"))
for i in range(qtd_aluno):
    print("Digite a 1° nota:")
n1=float(input())
print("Digite a 2° nota:")
n2=float(input())
print("Digite a 3° nota:")
n3=float(input())
print("Digite a 4° nota:")
n4=float(input())
media= (n1+n2+n3+n4)/4
print("Quantidades de faltas do aluno:")
qtd_faltas=int(input())
if media >=8:
    print("Parabéns, você foi aprovado(a)!!")
    situacao= "Aprovado"
elif media >=5:
    print("Você falhou e está na recuperação!")
elif media <5:
    print("Infelizmente, você foi reprovado!")
if qtd_faltas >=30:
    print("Você foi reprovado, pela quantidade de faltas!")

    print("Nome:")
nome= input()
