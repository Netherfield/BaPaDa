from flask import Flask, jsonify, render_template
import db


# CREAZIONE APP FLASK
app = Flask(__name__)

# IMPORT QUADRI
def import_quadri():
    query = "SELECT * FROM quadri"
    return db.execute_query(query)


# RENDER HOMEPAGE -> __HOME__.html
@app.route("/")
def homepage():
    return render_template("__HOME__.html")

# RENDER LISTA QUADRi
@app.route("/quadro/all")
def show_all():
    quadri = import_quadri()
    return render_template("__ALL__.html", quadri=quadri)

# PAGINA INDIRIZZO QUADRO
@app.route('/quadro/<id>')
def quadro(id):
    if db.db_name:
        db.db_config["database"] = db.db_name
    conn = db.mysql.connector.connect(**db.db_config)
    cursor = conn.cursor()
    query = "SELECT * FROM quadri WHERE id = %s"
    cursor.execute(query, (id,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('__ONE__QUADRO__.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)