qtd_aluno = int(input("Digite a quantidade de alunos:"))
nome = input("DIGITE O NOME DO ALUNO: ")

n1=float(input("Digite a 1° nota:"))
n2=float(input("Digite a 2° nota:"))
n3=float(input("Digite a 3° nota:"))
n4=float(input("Digite a 4° nota:"))
media= (n1+n2+n3+n4)/4
qtd_faltas=int(input("Quantidades de faltas do aluno:"))

if qtd_faltas >= 31:
    situacao = 'reprovado'
elif media >= 8:
    situacao = 'aprovado'
elif media >= 5:
    rec = float(input("Digite a nota da rec do aluno"))
    media = media  - 10
    if media + rec >= 8:
        media = media + rec
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
else:
    situacao = 'reprovado'