#CADASTRO DE USUÁRIO E SENHA
saldo = 0.0 #Variável que guardará o saldo do usuário
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
            print("Bem vindo! ", usuario)
            while True:#Enquanto que exibirá o menu principal
                print("1. Deposito 2. Sacar 3. Pix 4. Extrato 5. Encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1:#se usuário escolher depósito 
                    #Lê o valor a ser depositado
                    valor_deposito = float(input("Digite o valor que você deseja depositar:"))
                    saldo = saldo + valor_deposito #Atualiza o valor 
                    print("Novo saldo é ", saldo)
                elif escolha_principal == 2: #SAQUE
                    valor_saque = float(input("Digite o valor que você deseja sacar:"))
                    senha_saque = input("Digite sua senha: ")
                    if senha_saque == senha:#Se senha estiver correta
                        saldo = saldo - valor_saque #Subtrai o valor do saldo
                        
                    else:
                        print("Senha incorreta!") 
                elif escolha_principal == 3: #Se o usuário escolher pix
                    valor_pix = float(input("Digite o valor do pix:")) 
                    senha_pix = input("Digite sua senha:")  
                    if senha_pix == senha:
                        saldo = saldo - valor_pix
                    else:
                        print("Senha incorreta!")
                elif escolha_principal == 4:#Se o usuário escolher visualizar 
                    senha_extrato = input("Digite sua senha!")
                    if senha_extrato == senha:
                        print("Extrato: ", saldo)
                    else:
                        print("Senha incorreta!")
                elif escolha_principal == 5:#Encerrar
                    senha_encerrar = input("Digite sua senha!")
                    if senha_encerrar == senha:
                        break
                    else:
                        print("Senha incorreta!")
        else:
            print("Usuário ou senha incorretos!")

