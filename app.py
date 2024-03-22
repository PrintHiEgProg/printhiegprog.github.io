from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database_springs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM springs')
    springs = cursor.fetchall()
    conn.close()
    
    return render_template('list_springs.html', springs=springs)

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database_dumps.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dumbs')
    dumbs = cursor.fetchall()
    conn.close()
    
    return render_template('list_dumps.html', dumbs=dumbs)

if __name__ == '__main__':
    app.run(debug=True)
