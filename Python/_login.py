senha_admin = "Miguel"
usuario_cliente = "cliente"
def criar_conta():

    criar_usuario = input("Nome de usuário: ")
    criar_senha = input("Criar Senha: ")

    with open ("cadastro.txt", "a") as arquivo:
        arquivo.write(f"{criar_usuario},{criar_senha},{usuario_cliente}\n")

    print("Usuário criado com sucesso")

def login():

    login_usuario = input("Digite nome de usuário para login: ")
    login_senha = input("Digite senha do usuário: ")
    verificador = False

    with open ("cadastro.txt", "r") as arquivo:
        for linha in arquivo:
            u, s = linha.strip().split(",")

            if login_usuario == u and login_senha == s:
                verificador = True
                break
            
    if verificador: 
        print("Login realizado com sucesso!!")
    else: 
        print("Falha no login!!")

def apagar_conta():
    verificador_admin = False
    tentativa = 3
    
    for tentativas in range(3):
        print(f"Você tem {tentativa} tentativas para acertar a senha!!")
        senha_do_admin = input("Digite senha do Adminstrador para deletar um usuário: ")
        
        if senha_admin != senha_do_admin:
            print("Senha do Admin incorreta!!")
            print("Voçê não tem permissão para deletar um usuário")
        else:
            print("Senha Valida")
            verificador_admin = True
            break
        tentativa = tentativa - 1 

    if verificador_admin:
        usuario_deletar = False
        deletar_usuario = input("Digite usuário que deseja deletar: ")

        with open("cadastro.txt", "r") as arquivo: 
            listas = arquivo.readlines()

        print(f"Tem certeza que deseja deletar o usuário {deletar_usuario} ?")
        print("== Digite -confirmar- para deleta usuário ==")
        print("== Digite -cancelar- para não deletar usuário ==")

        opcao = input("Digite opção: ").lower()
        if opcao == "confirmar":
            usuario_deletar = True
            print("Usuario deltado com sucesso!!")
            
        elif opcao == "cancelar":
            print("Operação cancelado")
            print("Usuário não deletado")
            return
        
        else:
            print("Opção Invalida")
            return


        with open("cadastro.txt", "w") as arquivo:
            for linha in listas: 
                u, s = linha.strip().split(",")

                if u != deletar_usuario: 
                    arquivo.write(linha)

def ver_senhas():
    tentativa = 2
    validador_admin = False

    for tentativas in range(2):

        print(f"Você tem {tentativa} tentativas")
        senha_admin2 = input("Digite a senha do Adminstrador para ver as senhas: ")
        if senha_admin == senha_admin2: 
            print("Senha Valida!!")
            validador_admin = True
            break
        else: 
            print("Senha Valida!!")
        tentativa = tentativa - 1

    if validador_admin:
        with open("cadastro.txt", "r") as arquivo:
            for linha in arquivo:
                u, s = linha.strip().split(",")
                print(f"Usuário{u}")
                print(f"Senha{s}\n")

def menu(): 
    while True:
        print("=====Menu=====\n")
        print("===== 1- Criar Usuário =====")
        print("===== 2- Fazer Login =====")
        print("===== 3- Apagar Conta=====")
        print("===== 4- Ver Senha =====")
        print("===== 5- Sair =====")


        opcao = input("Digite uma opção do menu: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2": 
            login()
        elif opcao == "3": 
            apagar_conta()
        elif opcao == "4":
            ver_senhas()
        elif opcao == "5": 
            print("Sistema finalizado!!!")
            break
        else:
            print("Opção invalida: ")
            print("Digite um numero do Menu\n")
            


menu()