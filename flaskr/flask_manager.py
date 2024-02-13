from flask import Flask, render_template, request, redirect, url_for
import db_sqlite as db


# CREAZIONE APP FLASK
app = Flask(__name__)


# IMPORT QUADRI
def import_quadri(au=None):
    connection = db.create_db_connection("museo", "database/sqldb")
    if au:
        if db.db_name:
            db.db_config["database"] = db.db_name
        query = f"SELECT * FROM quadri WHERE Author = '{au}'"
        return db.execute_query(connection, query)
    else:
        query = "SELECT * FROM quadri"
        return db.execute_query(connection, query)

# IMPORT AUTORI
def import_autori():
    connection = db.create_db_connection("museo", "database/sqldb")    
    query = "SELECT DISTINCT(Author) from quadri"
    return db.execute_query(connection, query)

# RENDER HOMEPAGE -> __HOME__.html
@app.route("/")
def base():
    return render_template("base.html")

@app.route("/home")
def homepage():
    return render_template("home.html")


# RENDER LISTA QUADRi
@app.route("/quadro/all")
@app.route("/quadro/<author>")
def show_all(author=None):
    quadri = import_quadri(author)
    autori = import_autori()
    # print(quadri,autori)
    return render_template("mostre.html", quadri=quadri, autori=autori)


# PAGINA INDIRIZZO Title
@app.route('/quadro/id/<id>')
def quadro(id):
    connection = db.create_db_connection("museo", "database/sqldb")
    m_id = id
    query = f"SELECT * FROM quadri WHERE id = '{m_id}'"
    data = db.execute_query(connection, query)
    return render_template("informazioni.html", data=data[0])


#PAGINA ADMIN PER CRUD
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    connection = db.create_db_connection("museo", "database/sqldb")
    cursor = connection.cursor()

    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        author = request.form['author']
        year = request.form['year']
        link = request.form['link']
        action = request.form['action']

        if action == 'Aggiungi':
            cursor.execute('SELECT * FROM quadri WHERE Title = ? AND Author = ?', (name, author))
            existing_Title = cursor.fetchone()
            if existing_Title is None:
                cursor.execute('INSERT INTO quadri (Title, Author, Year, Link) VALUES (?, ?, ?, ?)',
                               (name, author, year, link))
                connection.commit()
            else:
                print("Il Title esiste già nel database.")
        elif action == 'Rimuovi':
            cursor.execute('DELETE FROM quadri WHERE id=?', (id,))
        connection.commit()
        return redirect(url_for('admin'))
    return render_template('admin.html')

@app.route('/informazioni')
def info():
    return render_template("informazioni.html")

@app.route('/contatti')
def contatti():
    return render_template("contatti.html")