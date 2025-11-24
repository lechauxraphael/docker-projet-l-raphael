from flask import Flask, render_template, request
import mysql.connector
import os
import random

app = Flask(__name__, template_folder='templates')

DB_HOST = os.environ.get('DATABASE_HOST', 'db')
DB_PORT = int(os.environ.get('DATABASE_PORT', 3306))
DB_USER = os.environ.get('DATABASE_USER', 'banduser')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'bandpass')
DB_NAME = os.environ.get('DATABASE_NAME', 'bandnames')

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connection_timeout=5
        )
        return conn
    except mysql.connector.Error:
        return None

@app.route('/', methods=['GET','POST'])
def index():
    message = None
    names = []

    if request.method == 'POST' and request.form.get('action') == 'check_db':
        conn = get_db_connection()
        if conn:
            conn.close()
            message = "Communication avec la base de données établie"
        else:
            message = "Impossible de se connecter à la base de données"

    if request.method == 'POST' and request.form.get('action') == 'generate':
        conn = get_db_connection()
        if conn is None:
            message = "Impossible de se connecter à la base de données"
        else:
            cur = conn.cursor()
            cur.execute("SELECT adjective FROM adjectives")
            adjectives = [r[0] for r in cur.fetchall()]
            cur.execute("SELECT noun FROM nouns")
            nouns = [r[0] for r in cur.fetchall()]
            cur.close()
            conn.close()

            if len(adjectives) < 10 or len(nouns) < 10:
                message = "Jeu de données insuffisant en base."
            else:
                for _ in range(10):
                    names.append(f"The {random.choice(adjectives)} {random.choice(nouns)}")

    return render_template('index.html', message=message, names=names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
