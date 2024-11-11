from flask import Flask, render_template
app = Flask(__name__)
# route -> o caminho ou link das páginas. ex: cantina.com.br/contatos
# função -> o que quer exibir naquela página
# templates -> para inserir os códigos html dentro da pasta. criar html file dentro dela.

@app.route("/")
def homepage():
    return render_template("homepage.html")
@app.route("/portaria")
def portaria():
    return render_template("portaria.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
