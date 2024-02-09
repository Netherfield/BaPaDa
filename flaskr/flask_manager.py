from flask import Flask, render_template
import db


# CREAZIONE APP FLASK
app = Flask(__name__)

# IMPORT QUADRI
def import_quadri(au=None):
    if au:
        if db.db_name:
            db.db_config["database"] = db.db_name
        query = f"SELECT * FROM quadri WHERE Autore = '{au}'"
        return db.execute_query(query)
    else:
        query = "SELECT * FROM quadri"
        return db.execute_query(query)

# IMPORT AUTORI
def import_autori():
    query = "SELECT Autore from quadri"
    return db.execute_query(query)

# RENDER HOMEPAGE -> __HOME__.html
@app.route("/")
def homepage():
    return render_template("__HOME__.html")


# RENDER LISTA QUADRi
@app.route("/quadro/all")
@app.route("/quadro/<autore>")
def show_all(autore=None):
    au = autore
    quadri = import_quadri(au)
    autori = import_autori()
    return render_template("__ALL__.html", quadri=quadri, autori=autori)

# PAGINA INDIRIZZO QUADRO
@app.route('/quadro/id/<id>')
def quadro(id):
    m_id = id
    query = f"SELECT * FROM quadri WHERE id = '{m_id}'"
    data = db.execute_query(query)
    return render_template("__ONE__QUADRO__.html", data=data[0])


# if __name__ == '__main__':
#     app.run(debug=True)