from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/list')
def list():
   con = sql.connect("my_lite_store.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from actual_ppr")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)