import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../data/fantasy_football_2018.db"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
week1_ppr_projections = Base.classes.week1_ppr_projections
# Samples = Base.classes.table2_name



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")



# Josh
@app.route("/data")
def data():
    # """Return a table on ufo template"""
    #get week 1 projections
    stmt = """
    SELECT *
    FROM week2_ppr_projections
    """

    # stmt = db.session.query(week1_ppr_projections).statement

    df_week1_ppr_projections = pd.read_sql_query(stmt, db.session.bind)
    print(df_week1_ppr_projections.head())
    return render_template("data.html")




# Connor
@app.route("/tweet")
def tweet():
    # """Return a table on ufo template"""
    #get week 1 projections
    stmt = """
    SELECT *
    FROM week2_ppr_projections
    """

    # stmt = db.session.query(week1_ppr_projections).statement

    df_week1_ppr_projections = pd.read_sql_query(stmt, db.session.bind)
    print(df_week1_ppr_projections.head())
    return render_template("tweet.html")





# Mike
@app.route("/input")
def input():
    # """Return a table on ufo template"""
    #get week 1 projections
    stmt = """
    SELECT *
    FROM week2_ppr_projections
    """

    # stmt = db.session.query(week1_ppr_projections).statement

    df_week1_ppr_projections = pd.read_sql_query(stmt, db.session.bind)
    print(df_week1_ppr_projections.head())
    return render_template("input.html")




# Zach
@app.route("/compare")
def compare():
    # """Return a table on ufo template"""
    #get week 1 projections
    stmt = """
    SELECT *
    FROM week2_ppr_projections
    """

    # stmt = db.session.query(week1_ppr_projections).statement

    df_week1_ppr_projections = pd.read_sql_query(stmt, db.session.bind)
    print(df_week1_ppr_projections.head())
    return render_template("compare.html")






if __name__ == '__main__':
   app.run(debug = True)




# from flask import Flask, render_template, request
# import sqlite3 as sql
# app = Flask(__name__)


# @app.route('/')
# def home():
#    return render_template('home.html')

# @app.route('/list')
# def list():
#    con = sql.connect("my_lite_store.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from actual_ppr")
   
#    rows = cur.fetchall()
#    return render_template("list.html",rows = rows)

# if __name__ == '__main__':
#    app.run(debug = True)