# This file is just so I can output a text file with prefixes and copy for Tableau

regions = ['APAC_North','APAC_South','EMEA', 'North_America', 'South_America']
preseason = ['Preseason_Qualifier_1', 'Preseason_Qualifier_2', 'Preseason_Qualifier_3', 'Preseason_Qualifier_4']
rounds = ['Round_1', 'Round_2', 'Round_3', 'Quarterfinals', 'Semifinals', 'Finals']
split = ['Split_1', 'Split_2']
challenger_circuit = ['challenger_circuit_1', 'challenger_circuit_2', 'challenger_circuit_3', 'challenger_circuit_4']
championship = ['LCQ_1', 'LCQ_2']
brackets = ['Finals, Losers_Bracket, Winners_Bracket']
bracket_stages = ['Bracket_Stage','Champ_Finals','Group_Stage']
champ_games = ['Championship','Split 2 Playoffs']


with open('./column_prefix.txt', 'a') as file:

    for region in regions:
        for pre in preseason:
            for round in rounds:
                file.write(f'{region}_{pre}_{round}\n')
    
    for region in regions:
        for s in split:
            for challenge in challenger_circuit:
                for round in rounds:
                    file.write(f'{region}_{s}_{challenge}_{round}\n')
    
    for region in regions:
        for s in split:
            file.write(f'{region}_{s}_playoffs\n')

    for region in regions:
        for s in split:
            file.write(f'{region}_{s}_pro_league\n')
    
    for region in regions:
        for s in split:
            for champ in championship:
                for bracket in brackets:
                    file.write(f'{region}_{s}_{champ}_{bracket}\n')
    
    # for championship
    for champ in champ_games:
        for bracket in bracket_stages:
            file.write(f'{champ}_{bracket}\n')



