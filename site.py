from flask import Flask, render_template, request, redirect

site = Flask(__name__)

tipo = ""
senha_admin = "Miguel"

@site.route("/")
def home():
    return render_template("front.html")

@site.route("/criar", methods=["POST"])
def criar_conta():

    criar_usuario = request.form.get("usuario")
    criar_senha = request.form.get("senha")

    conta_cliente = "cliente"

    with open ("cadastro.txt", "a") as arquivo:
        arquivo.write(f"{criar_usuario},{criar_senha},{conta_cliente}\n")

    return "Usuário criado com sucesso"

@site.route("/login", methods=["POST"])
def login():

    login_usuario = request.form.get("usuario")
    login_senha = request.form.get("senha")

    with open ("cadastro.txt", "r") as arquivo:
        for linha in arquivo:
            u, s = linha.strip().split(",")

            if login_usuario == u and login_senha == s:
                if tipo == "admin":
                    return redirect("/admin")
                else: 
                    return redirect("/cliente")
    
@site.route("/apagar", methods=["POST"])
def apagar_conta():
    deletar_usuario = request.form.get("usuario")      

    with open("cadastro.txt", "r") as arquivo: 
        listas = arquivo.readlines()

    with open("cadastro.txt", "w") as arquivo:
        for linha in listas: 
            u, s = linha.strip().split(",")

            if u != deletar_usuario: 
                    arquivo.write(linha)
            return "Usuário deletado com sucesso!!"
        
    return"Usuário não encontrado"

@site.route("/ver", methods=["POST"])
def ver_senhas():
    senha_admin2 = request.form.get("senha_admin")
    if senha_admin2 != senha_admin:
        return "Senha Invalida!!"    

    resultado = ""

    with open("cadastro.txt", "r") as arquivo:
        for linha in arquivo:
            u, s = linha.strip().split(",")
            resultado += f"{u} - {s}<br>"

    return resultado

# Rota para crirar uma conta admin

@site.route("/criar_admin")
def criar_admin():
    criar_admin = request.form.get("admin_conta")
    criar_senha_admin = request.form.get("admin_senha")

    contadoadmin = "admin"

    with open("cadastro.txt", "r") as arquivo: 
        arquivo.write(f"{criar_admin},{criar_senha_admin},{contadoadmin}")

    return "Conta do Adminstrador criada"

# Rota para as paginas de cliente e admin

@site.route("/cliente")
def cliente(): 
    return render_template("pagina_admin.html")

@site.route("/admin")
def admin():
    return render_template("pagina_admin.html")

# RODAR

if __name__ == "__main__":
    site.run(debug=True)
