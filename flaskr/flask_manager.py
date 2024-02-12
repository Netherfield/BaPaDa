from flask import *
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


#PAGINA ADMIN PER CRUD
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = db.create_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        author = request.form['author']
        year = request.form['year']
        link = request.form['link']
        action = request.form['action']

        if action == 'Aggiungi':
            cursor.execute('SELECT * FROM quadri WHERE Quadro = %s AND Autore = %s', (name, author))
            existing_quadro = cursor.fetchone()
            if existing_quadro is None:
                cursor.execute('INSERT INTO quadri (Quadro, Autore, Anno, Link) VALUES (%s, %s, %s, %s)',
                               (name, author, year, link))
                conn.commit()
            else:
                print("Il quadro esiste già nel database.")
        elif action == 'Rimuovi':
            cursor.execute('DELETE FROM quadri WHERE id=%s', (id,))
        conn.commit()
        return redirect(url_for('admin'))
    return render_template('__ADMIN__.html')

