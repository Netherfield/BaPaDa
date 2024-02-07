from flask import Flask, jsonify, render_template

# CREAZIONE APP FLASK
app = Flask(__name__)


# RENDER HOMEPAGE -> __HOME__.html
@app.route("/")
def homepage():
    return render_template("__HOME__.html")

if __name__ == '__main__':
    app.run(debug=True)