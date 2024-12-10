#CADASTRO DE USUÁRIO E SENHA
while True:
#MENU PRINCIPAL
    print("Bem vindo! \n Digite 1.Cadastrar 2.Login 3.encerrar")

    #LER ESCOLHA DO USUARIO
    escolha_menu = int(input())#Lê a escolha como um número inteiro

    #Se o usuário esolher cadastro
    if escolha_menu == 1:
        #Cria um usuário e uma senha com tipo string
        usuario = input("Crie um nome de usuário:")
        senha = input("Crie uma senha:")
    elif escolha_menu == 2: #Se o usuário escolher login
    #Compara as inf. cadastradas com uma leitura
        login_usuario = input("Digite o nome do seu usuário:")
        login_senha = input("Digite sua senha:")
        if login_usuario == usuario and login_senha == senha:
            print("Login realizado com sucesso!")
            #Se login correto, entra no
            #Menu principal do APP
        else:
            print("Usuário ou senha incorretos!")
