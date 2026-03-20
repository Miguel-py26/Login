from flask import Flask, render_template, request

site = Flask(__name__)

senha_admin = "Miguel"

@site.route("/")
def home():
    return render_template("front.html")

@site.route("/criar", methods=["POST"])
def criar_conta():

    criar_usuario = request.form["usuario"]
    criar_senha = request.form["senha"]

    with open ("cadastro.txt", "a") as arquivo:
        arquivo.write(f"{criar_usuario},{criar_senha}\n")

    return "Usuário criado com sucesso"

@site.route("/login", methods=["POST"])
def login():

    login_usuario = request.form["usuario"]
    login_senha = request.form["senha"]

    with open ("cadastro.txt", "r") as arquivo:
        for linha in arquivo:
            u, s = linha.strip().split(",")

            if login_usuario == u and login_senha == s:
                return "Login realizado com sucesso!!"

    return "Falha no login!!" 
    
@site.route("/apagar", methods=["POST"])
def apagar_conta():
    deletar_usuario = request.form["usuario"]
    senha_do_admin = request.form["senha_admin"]
        
    if senha_admin != senha_do_admin:
        return "Senha do Adminstrador incorreta!!"

    with open("cadastro.txt", "r") as arquivo: 
        listas = arquivo.readlines()

    with open("cadastro.txt", "w") as arquivo:
        for linha in listas: 
            u, s = linha.strip().split(",")

            if u != deletar_usuario: 
                    arquivo.write(linha)

    return "Usuário deletado com sucesso!!"  

@site.route("/ver", methods=["POST"])
def ver_senhas():
    senha_admin2 = request.form["senha_admin"]
    if senha_admin2 != senha_admin:
        return "Senha Invalida!!"    

    resultado = ""

    with open("cadastro.txt", "r") as arquivo:
        for linha in arquivo:
            u, s = linha.strip().split(",")
            resultado += f"{u} - {s}<br>"

    return resultado
if __name__ == "__main__":
    site.run(debug=True)