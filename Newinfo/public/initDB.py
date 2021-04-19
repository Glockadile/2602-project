
from models import Players, db 
import csv


# add code to parse csv, create and save pokemon objects
with open('./public/players_raw.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            first_nameP = 0
            second_nameP = 0
            assistsP = 0
            clean_sheetsP = 0
            formP = 0
            goals_concededP= 0
            goals_scoredP= 0
            minutesP= 0
            penalties_savedP= 0
            red_cardsP= 0
            savesP= 0
            yellow_cardsP= 0


            for idx, x in enumerate(row): #ennumerate to access index in the loop, https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
                if x== 'first_name':
                    first_nameP=idx
                if x== 'second_name':
                    second_nameP=idx
                if x== 'assists':
                    assistsP=idx
                if x== 'clean_sheets':
                    clean_sheetsP=idx
                if x== 'form':
                    formP=idx
                if x== 'goals_conceded':
                    goals_concededP=idx
                if x== 'goals_scored':
                    goals_scoredP=idx
                if x== 'minutes':
                    minutesP=idx
                if x== 'penalties_saved':
                    penalties_savedP=idx
                if x== 'red_cards':
                    red_cardsP=idx
                if x== 'saves':
                    savesP=idx
                if x== 'yellow_cards':
                    yellow_cardsP=idx

            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row[yellow_cardsP])
            allPlayers= Players(first_name=row[first_nameP], second_name=row[second_nameP], assists=row[assistsP], clean_sheets=row[clean_sheetsP], form=row[formP], goals_conceded=row[goals_concededP], goals_scored=row[goals_scoredP] ,minutes=row[minutesP],penalties_saved=row[penalties_savedP],red_cards=row[red_cardsP],yellow_cards=row[yellow_cardsP])
            db.session.add(allPlayers)
            db.session.commit()
            line_count += 1
