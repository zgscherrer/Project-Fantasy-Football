import os

import pandas as pd
import numpy as np
import json
from scipy import stats
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, request
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
@app.route("/data", methods=['POST', 'GET'])
def data():
    if request.method == "GET":
        # Return an initial blank form before user inputs their custom factors
        #call database test
        stmt = """
            SELECT *
            FROM week3_ppr_projections
            """
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        initialTableData = df_proj.to_dict('records')
        return render_template("data.html", tableData=initialTableData)
        
    elif request.method == "POST":
        # use the user input to operate on the dataframe and then a list of dictionaries (records) that can be referenced in the html
        print(request.form)
        filter_player_name = request.form.get("player_name", "no_player")
        filter_position = request.form.get("position", "no_position")
        filter_team = request.form.get("team", "no_team")
        if filter_player_name != "":
        # return jsonify(request.form)
        # scout = request.form.get('')

            #call database test
            stmt = """
                SELECT *
                FROM week3_ppr_projections
                WHERE PLAYER LIKE '%{}%'

                """.format(filter_player_name)
        elif filter_position != "":
                # return jsonify(request.form)
                # scout = request.form.get('')

                    #call database test
                stmt = """
                    SELECT *
                    FROM week3_ppr_projections
                    WHERE POS = '{}'

                    """.format(filter_position)
        elif filter_team != "":
                # return jsonify(request.form)
                # scout = request.form.get('')

                    #call database test
                stmt = """
                    SELECT *
                    FROM week3_ppr_projections
                    WHERE TEAM = '{}'

                    """.format(filter_team)

        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        userTableData = df_proj.to_dict('records')
        return render_template("data.html", tableData=userTableData)

# Connor
@app.route("/tweet", methods=['POST', 'GET'])
def tweet():
    if request.method == "GET":
        # Return an initial blank form before user inputs their custom factors
        #call database test
        stmt = """
            SELECT *
            FROM week_3_tweets
            """
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        initialTableData = df_proj.to_dict('records')
        return render_template("tweet.html", tableData=initialTableData)
        
    elif request.method == "POST":
        # use the user input to operate on the dataframe and then a list of dictionaries (records) that can be referenced in the html
        filter_player_name = request.form.get("player_name")
        # return jsonify(request.form)
        # scout = request.form.get('')

        #call database test
        stmt = """
            SELECT *
            FROM week_3_tweets
            WHERE player = '{}'
            """.format(filter_player_name)
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        userTableData = df_proj.to_dict('records')
        return render_template("tweet.html", tableData=userTableData)





# Mike
@app.route("/input", methods=['POST', 'GET'])
def input():
    if request.method == "GET":
        # Return an initial blank form before user inputs their custom factors
        return render_template("input.html")
        
    elif request.method == "POST":
        # use the user input to operate on the dataframe and then a list of dictionaries (records) that can be referenced in the html
        #define all of our variables from the form POST data
        week = request.form.get('Week')
        espn_wt = eval(request.form.get('ESPN'))
        cbs_wt = eval(request.form.get('CBS'))
        sharks_wt = eval(request.form.get('Sharks'))
        scout_wt = eval(request.form.get('Scout'))
        prior_wt = eval(request.form.get('Prior'))
        def_boost = request.form.get('Defense')
        overunder_boost = request.form.get('OverUnder')
        twitter_boost = request.form.get('Twitter')

        #convert weights to percentages
        espn_pct = espn_wt/100
        cbs_pct = cbs_wt/100
        sharks_pct = sharks_wt/100
        scout_pct = scout_wt/100
        prior_pct = prior_wt/100

        #call database test
        stmt = f"""
                SELECT *
                FROM week{week}_ppr_projections
                """
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #create initial custom weighted average of the five projection sources based on user input
        df_proj['FPTS_PPR_CUSTOM_AVG'] = df_proj.apply(lambda row: 
                                            (row['FPTS_PPR_ESPN']*espn_pct +
                                            row['FPTS_PPR_CBS']*cbs_pct +
                                            row['FPTS_PPR_SHARKS']*sharks_pct +
                                            row['FPTS_PPR_SCOUT']*scout_pct +
                                            row['FPTS_PPR_PRVS_WK_ACTUAL']*prior_pct),
                                            axis='columns')

        #send dataframe to records (a list of dictionaries for each row)
        userTableData = df_proj.to_dict('records')
        return render_template("input.html", tableData=userTableData)




# @app.route("/input/test") #?Week=<week>&ESPN=<espn_wt>&CBS=<cbs_wt>&Sharks=<sharks_wt>&Scout=<scout_wt>&Prior=<prior_wt>&Defense=<def_boost>&OverUnder=<overunder_boost>&Twitter=<twitter_boost>&message=<msg_text>")
# def calculate_custom_factors():
#     #get current week projections
#     stmt = """
#     SELECT *
#     FROM week3_ppr_projections
#     """
#     df_proj = pd.read_sql_query(stmt, db.session.bind)


#     #export df as json - orient='records' gives a json string that is a list of dictionaries, 
#     # one dictionary for each row in df with column as keys and row values as values
#     #also need to use python's json.loads function to create it to a real json and not string object
#     json_proj = json.loads(df_proj.to_json(orient='records'))

#     print(json_proj)
#     print(type(json_proj))
#     return render_template("input.html", jsonUser=jsonify(json_proj))



# Zach
@app.route("/compare/<week>", methods=['POST', 'GET'])
def getCharts(week):
    #get week 1 projections & actuals
    stmt = "SELECT * FROM week{}_ppr_projections".format(week)
    df_ppr_projections = pd.read_sql_query(stmt, db.session.bind)

    stmt = "SELECT * FROM week{}_ppr_actuals".format(week)
    df_ppr_actuals = pd.read_sql_query(stmt, db.session.bind)

    #merge starting with the actuals db and merge inner (don't want to evaluate correlations of players not in db)
    df_week1_ppr = pd.merge(df_ppr_actuals, df_ppr_projections[['PLAYER', 'POS',
                                                'FPTS_PPR_ESPN', 'FPTS_PPR_CBS', 'FPTS_PPR_SHARKS',
                                                'FPTS_PPR_SCOUT', 'FPTS_PPR_PRVS_WK_ACTUAL']],
                        how='inner', on=['PLAYER', 'POS'])

    #average all four of our projection sources of ESPN, CBS, Sharks, and Scout
    df_week1_ppr['FPTS_PPR_AVG_PROJ'] = df_week1_ppr[['FPTS_PPR_ESPN','FPTS_PPR_CBS',
                                                  'FPTS_PPR_SHARKS', 'FPTS_PPR_SCOUT']].mean(axis='columns')
    json_ppr_proj = df_week1_ppr.to_dict('records')
    return jsonify(json_ppr_proj)



# @app.route("/compare/<week>", methods=['POST', 'GET'])
# def getCharts(week):
#     #get week 1 projections
#     stmt = "SELECT * FROM week{}_ppr_projections".format(week)

#     df_ppr_projections = pd.read_sql_query(stmt, db.session.bind)
#     json_proj = df_ppr_projections.to_dict('records')
#     return jsonify(json_proj)



@app.route("/compare", methods=['POST', 'GET'])
def compare():
    if request.method == "GET":
        # Return an initial blank form before user inputs their custom factors
        stmt = """
            SELECT *
            FROM week3_ppr_projections
            """
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        initialTableData = df_proj.to_dict('records')
        return render_template("compare.html", tableData=initialTableData)
        
    elif request.method == "POST":
        # use the user input to operate on the dataframe and then a list of dictionaries (records) that can be referenced in the html
        
        #return jsonify(request.form)
        scout = request.form.get('')

        #call database test
        stmt = """
            SELECT *
            FROM week3_ppr_projections
            """
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        userTableData = df_proj.to_dict('records')
        return render_template("compare.html", tableData=userTableData)



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


