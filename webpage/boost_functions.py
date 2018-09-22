#this contains all the boost calculation functions for the player customization
#so that app.py can import them and have a little less long code in the app.py

def over_under_boost_calculator(row, user_boost_weight):
    #define the user's boost multiplier based on their selection of how much of the factor to apply
    if user_boost_weight == 'Full':
        user_boost_multiplier = 1.0
    elif user_boost_weight == 'Partial':
        user_boost_multiplier = 0.5
    else:
        user_boost_multiplier = 0
        
    #these are our custom boost factors based on our o/u score sentiments (can change these on the backend however we want)
    over_under_boost_values = {'Awesome': 0.2, 'Good': 0.1, 'Neutral': 0, 'Concerned': -0.1, 'Terrible': -0.2}
    
    #get the starting custom weighted average fantasy points projections by the user
    custom_points = row['FPTS_PPR_CUSTOM_AVG']
    
    #get boost multiplier based on the overunder binned sentiments and our dictionary of boost factors
    boost_multiplier = over_under_boost_values.get(row['score_sentiment'], 0)
    
    #calculate the boost points
    over_under_boost_points = custom_points * boost_multiplier * user_boost_multiplier
    
    return over_under_boost_points



def twitter_boost_calculator(row, user_boost_weight):
    #define the user's boost multiplier based on their selection of how much of the factor to apply
    if user_boost_weight == 'Full':
        user_boost_multiplier = 1.0
    elif user_boost_weight == 'Partial':
        user_boost_multiplier = 0.5
    else:
        user_boost_multiplier = 0
        
    #these are our custom boost factors based on our twitter sentiments (can change these on the backend however we want)
    twitter_boost_values = {'Awesome': 0.2, 'Good': 0.1, 'Neutral': 0, 'Concerned': -0.1, 'Terrible': -0.2}
    
    #get the starting custom weighted average fantasy points projections by the user
    custom_points = row['FPTS_PPR_CUSTOM_AVG']
    
    #get boost multiplier based on the overunder binned sentiments and our dictionary of boost factors
    boost_multiplier = twitter_boost_values.get(row['expert_sentiment'], 0)
    
    #calculate the boost points
    twitter_boost_points = custom_points * boost_multiplier * user_boost_multiplier
    
    return twitter_boost_points



def defense_boost_calculator(row, user_boost_weight):
    #if the player looking it as a Defense, we will want to skip and not boost the defense projection
    if row['POS'] == 'D/ST':
        return 0.0
    
    #otherwise apply the defense boost to all other positions (may in future want to consider removing kickers as
    #they are often unpredictable, and maybe the correlation of a harder defense is even positive on kicker points b/c they kick more FGs than TDs)
    else:
        #define the user's boost multiplier based on their selection of how much of the factor to apply
        if user_boost_weight == 'Full':
            user_boost_multiplier = 1.0
        elif user_boost_weight == 'Partial':
            user_boost_multiplier = 0.5
        else:
            user_boost_multiplier = 0

        #these are our custom boost factors based on our opposing defenses(can change these on the backend however we want)
        #the sentiment stored is from the offensive perspective of the opp def impact, so 'Good' means they 
        #are facing an easy defense and will get a positive boost, 'Terrible' means they are facing a hard 
        #defense and will get negative boost
        opp_defense_boost_values = {'Awesome': 0.2, 'Good': 0.1, 'Neutral': 0, 'Concerned': -0.1, 'Terrible': -0.2}

        #get the starting custom weighted average fantasy points projections by the user
        custom_points = row['FPTS_PPR_CUSTOM_AVG']

        #get boost multiplier based on the overunder binned sentiments and our dictionary of boost factors
        boost_multiplier = opp_defense_boost_values.get(row['offense_opp_def_impact'], 0)

        #calculate the boost points
        defense_boost_points = custom_points * boost_multiplier * user_boost_multiplier

        return defense_boost_points