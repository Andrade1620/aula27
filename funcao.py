#DECLARANDO UMA FUNÇÃO
def saudacoes(hora_do_dia):#Exibe a saudação correspondente ao horário do dia
    #Condição para dar BOM DIA!
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print("Bom dia!!!!")
    #Condição para dar BOA TARDE!
    elif (hora_do_dia >=13) and (hora_do_dia <=18):
        print("Boa tarde!!!!!")
    #Condição para dar Boa noite
    elif (hora_do_dia >=19) and (hora_do_dia <=23):
        print("Boa noite!!!!!")
#FORA DA FUNÇÃO
#peço para o usuário dizer a hora atual
resposta = float(input("Digite que horas são: \n"))

saudacoes(resposta)