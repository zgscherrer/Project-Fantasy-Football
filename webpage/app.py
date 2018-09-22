import os

import pandas as pd
import numpy as np
import json
from scipy import stats
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from boost_functions import *
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
                    WHERE POS LIKE '%{}%'

                    """.format(filter_position)
        elif filter_team != "":
                # return jsonify(request.form)
                # scout = request.form.get('')

                    #call database test
                stmt = """
                    SELECT *
                    FROM week3_ppr_projections
                    WHERE TEAM LIKE '%{}%'

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
            WHERE player LIKE '%{}%'
            """.format(filter_player_name)
        df_proj = pd.read_sql_query(stmt, db.session.bind)

        #send dataframe to records (a list of dictionaries for each row)
        userTableData = df_proj.to_dict('records')
        return render_template("tweet.html", tableData=userTableData)





# Mike
@app.route("/input", methods=['POST', 'GET'])
def input():
    if request.method == "GET":
        # Return an initial blank data page before user inputs their custom factors
        #have the default values populate as 20% for each one and Full for each boost
        defaultInputs = {'Week': '3',
                        'ESPN': '20',
                        'CBS': '20',
                        'Sharks': '20',
                        'Scout': '20',
                        'Prior': '20',
                        'Defense': 'Full',
                        'OverUnder': 'Full',
                        'Twitter': 'Full'}

        return render_template("input.html", formData=defaultInputs)
        
    elif request.method == "POST":
        # use the user input to operate on the dataframe and then a list of dictionaries (records) that can be referenced in the html
        #define all of our variables from the form POST data
        week = request.form.get('Week')
        espn_wt = eval(request.form.get('ESPN'))
        cbs_wt = eval(request.form.get('CBS'))
        sharks_wt = eval(request.form.get('Sharks'))
        scout_wt = eval(request.form.get('Scout'))
        prior_wt = eval(request.form.get('Prior'))
        def_boost_wt = request.form.get('Defense')
        overunder_boost_wt = request.form.get('OverUnder')
        twitter_boost_wt = request.form.get('Twitter')


        ### CUSTOM PROJECTIONS AVERAGE ###
        #convert weights to percentages
        espn_pct = espn_wt/100
        cbs_pct = cbs_wt/100
        sharks_pct = sharks_wt/100
        scout_pct = scout_wt/100
        prior_pct = prior_wt/100

        #get the projections for the week from the database
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

        
        
        ### BOOST FACTORS ###
        
        #GET DEFENSE DATA for your week selected - all defense data for each week is one database,
        #select only columns you want
        #NOTE - currently it is pulling in defense sentiment always for week 3 - no sentiments for other weeks
        stmt_def = f"""
                    SELECT team_abbr, week_{week}_opp, week_{week}_proj, score_sentiment
                    FROM def_scores
                    """
        df_defense = pd.read_sql_query(stmt_def, db.session.bind)

        #currently score_sentiment is for the offensive opponenet perspective so Min's really good Defense
        #against Buf has score sentiment of 'Terrible' which is terrible for Buf, so all Buf players
        #would get negative points weighting - rename column
        #rename team_abbr to def_team_abbr
        df_defense.rename(columns={'score_sentiment': 'offense_opp_def_impact',
                                'team_abbr': 'def_team_abbr'}, inplace=True)


        #GET OVERUNDER DATA for your week selected
        try:
            stmt_overunder = f"""
                            SELECT *
                            FROM week_{week}_over_unders
                            """
            df_overunder = pd.read_sql_query(stmt_overunder, db.session.bind)
        
        except: #if error because table doesn't exist (we dont' have all previous week data)
            #then just return an empty dataframe with columns that match the other df so calcs run,
            # but end with zero boost factors
            df_overunder = pd.DataFrame(columns=['Unnamed: 0', 'team', 'over_under', 'team_abbr', 'binned', 'score_sentiment'])


        #GET TWEET DATA for your week selected
        try:
            stmt_tweets = f"""
                            SELECT *
                            FROM week_{week}_tweets
                            """
            df_tweets = pd.read_sql_query(stmt_tweets, db.session.bind)
        
        except: #if error because table doesn't exist (we dont' have all previous week data)
            #then just return an empty dataframe with columns that match the other df so calcs run,
            # but end with zero boost factors
            df_tweets = pd.DataFrame(columns=['Unnamed: 0', 'number', 'player', 'compound_score', 'binned',
                                                'expert_sentiment', 'color', 'all_tweets'])

        
        #MERGE BOOST FACTOR DATA TO PLAYERS/PROJECTION DF
        # #check size of starting df
        # print(df_proj.shape)

        #first merge in the twitter sentiment - always do left merge (rather have Nans for boost factors than lose players)
        df_boosts = pd.merge(df_proj, df_tweets[['player', 'compound_score', 'expert_sentiment']],
                            how='left', left_on='PLAYER', right_on='player')
        df_boosts.drop('player', axis='columns', inplace=True) #don't need to keep this added player name column
        # print(df_boosts.shape)

        #second merge in the overunder - always do left merge (rather have Nans for boost factors than lose players)
        df_boosts = pd.merge(df_boosts, df_overunder[['team_abbr', 'over_under', 'score_sentiment']],
                            how='left', left_on='TEAM', right_on='team_abbr')
        df_boosts.drop('team_abbr', axis='columns', inplace=True) #don't need to keep this added team abbr column
        # print(df_boosts.shape)

        #third merge in the defense projections - always do left merge (rather have Nans for boost factors than lose players)
        #will merge by the team of the datframe and in defense looking for the opponent (that is offensive opponent of the defense listed as team)
        df_boosts = pd.merge(df_boosts, df_defense[['def_team_abbr', f"week_{week}_opp", f"week_{week}_proj", 'offense_opp_def_impact']],
                            how='left', left_on='TEAM', right_on=f"week_{week}_opp")
        df_boosts.drop(f"week_{week}_opp", axis='columns', inplace=True) #don't need to keep this added team abbr column
        # print(df_boosts.shape)

        #convert any of the Nans in our binned sentiment columns to Neutral (that will just apply a zero boost to those players)
        df_boosts.fillna('Neutral', inplace=True)


        #CALCULATE BOOST FACTORS AND GET FINAL POINTS
        df_boosts['OPPOSING_DEFENSE_BOOST'] = df_boosts.apply(lambda row: 
                                                defense_boost_calculator(row, def_boost_wt),
                                                axis='columns')

        df_boosts['OVER_UNDER_BOOST'] = df_boosts.apply(lambda row: 
                                            over_under_boost_calculator(row, overunder_boost_wt),
                                            axis='columns')
                
        df_boosts['TWITTER_BOOST'] = df_boosts.apply(lambda row: 
                                            twitter_boost_calculator(row, twitter_boost_wt),
                                            axis='columns')

        #calculate final FPTS ADDING UP ALL BOOST PTS TO THE CUSTOM AVG
        df_boosts['FPTS_PPR_CUSTOM_AVG_BOOST'] = df_boosts[['FPTS_PPR_CUSTOM_AVG', 'OPPOSING_DEFENSE_BOOST',
                                                    'OVER_UNDER_BOOST', 'TWITTER_BOOST']].sum(axis='columns') 

        #reorder dataframe and limits columns for the final output data and sort descending by custom poitns
        df_boosts_output = df_boosts[['PLAYER', 'POS', 'TEAM', 'FPTS_PPR_CUSTOM_AVG_BOOST',
                                    'FPTS_PPR_ESPN', 'FPTS_PPR_CBS', 'FPTS_PPR_SHARKS', 'FPTS_PPR_SCOUT',
                                    'FPTS_PPR_PRVS_WK_ACTUAL', 'FPTS_PPR_CUSTOM_AVG', 
                                    'OVER_UNDER_BOOST', 'TWITTER_BOOST',
                                    'OPPOSING_DEFENSE_BOOST']].sort_values('FPTS_PPR_CUSTOM_AVG_BOOST',
                                                                            ascending=False)



        ### SEND DATA/RENDER TEMPLATE ###
        #round dataframe numbers to tenths place (so doesn't show up whole long decimal)
        df_boosts_output = df_boosts_output.round(decimals=1)

        #send dataframe to records (a list of dictionaries for each row)
        userTableData = df_boosts_output.to_dict('records')

        #render input.html template, return tableData that can build table of the data with user specified calculations, 
        #and return the original userinputs so that can populate those in the input fields so user can see what inputs
        #were being used for the calculations they are seeing
        return render_template("input.html", tableData=userTableData, formData=request.form)




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
    #get week <week> projections & actuals
    stmt_proj = "SELECT * FROM week{}_ppr_projections".format(week)
    df_ppr_projections = pd.read_sql_query(stmt_proj, db.session.bind)

    stmt_actual = "SELECT * FROM week{}_ppr_actuals".format(week)
    df_ppr_actuals = pd.read_sql_query(stmt_actual, db.session.bind)

    #merge starting with the actuals db and merge inner (don't want to evaluate correlations of players not in db)
    df_ppr = pd.merge(df_ppr_actuals, df_ppr_projections[['PLAYER', 'POS',
                                                'FPTS_PPR_ESPN', 'FPTS_PPR_CBS', 'FPTS_PPR_SHARKS',
                                                'FPTS_PPR_SCOUT', 'FPTS_PPR_PRVS_WK_ACTUAL']],
                        how='inner', on=['PLAYER', 'POS'])

    #average all four of our projection sources of ESPN, CBS, Sharks, and Scout
    df_ppr['FPTS_PPR_AVG_PROJ'] = df_ppr[['FPTS_PPR_ESPN','FPTS_PPR_CBS',
                                    'FPTS_PPR_SHARKS', 'FPTS_PPR_SCOUT']].mean(axis='columns')
   
   
    json_ppr = df_ppr.to_dict('records')

    return jsonify(json_ppr)



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


