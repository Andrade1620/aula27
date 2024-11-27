n1=float(input())
n2=float(input())
n3=float(input())
n4= float(input())
media= (n1+n2+n3+n4)/4
qtd_faltas= int(input())
qtd_alunos= int(input())
if media >=8:
    print("Parabéns, você foi aprovado(a)!!")
elif media >=5:
    print("Você falhou, e , está na recuperação!")
elif media <5:
    print("Infelizmente, você foi reprovado!")
