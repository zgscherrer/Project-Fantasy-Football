SQLite Fantasy Football Database
Database Name: fantasy_football_2018.db

Weekly PPR Projections Tables
Use: import this for our customized weighting page data, it only includes players that actually were included in ALL of the four projections scraped
separate table for each week, currently have two:
week1_ppr_projections
Week2_ppr_projections
Has columns of: PLAYER, POS, TEAM, FPTS_PPR_ESPN, FPTS_PPR_CBS, FPTS_PPR_SHARKS, FPTS_PPR_SCOUT, FPTS_PPR_PRVS_WK_ACTUAL

Weekly PPR Projections All Scraped Players Tables
Use: import this for our pure raw data table page, it includes every player scraped, even if they were only included in one of the projection sites. This way people can see more players (including one site that had individual defensive players) but won’t mess up our customized weighting where you would not want any null data 
separate table for each week, currently have two:
week1_ppr_projections_all_scraped
week2_ppr_projections_all_scraped
Has columns of: PLAYER, POS, TEAM, FPTS_PPR_ESPN, FPTS_PPR_CBS, FPTS_PPR_SHARKS, FPTS_PPR_SCOUT, FPTS_PPR_PRVS_WK_ACTUAL

Weekly PPR Actuals Tables
Use: for comparing projections to actual results, will have to JOIN with projections tables
Separate table for each week, currently have one:
week1_ppr_actuals
Has columns of: PLAYER, POS, TEAM, FPTS_PPR_ACTUAL, WEEK

Weekly FanDuel Salaries Tables
Use: for calculating a pts/dollar comparison, will have to JOIN with the projections tables
Separate table for each week, currently have two:
week1_salaries_fanduel
Note: this one is an empty table with headers - I wasn’t able to find archived fanduel salary data from week 1, but wanted the table to exist for when we run some of our logic so doesn’t reference a table that doesn’t exist when trying to join, etc.
week2_salaries_fanduel
Has columns of: PLAYER, POS, TEAM, SALARY_FANDUEL, WEEK