from sportsipy.mlb.teams import Teams, Schedule
import json

baseball_list = []
teams = Teams(2022)
for team in teams:
    for game in Schedule(f'{team.abbreviation}'):
        baseball_dict = {
            'model':'event_manager.event',
            'fields': {
                'sport': 'baseball',
                'team': team.abbreviation,
                'date': game.datetime.strftime("%Y-%m-%d"),
                'opponent': game.opponent_abbr,
                'day_or_night': game.day_or_night,
                'location': game.location
            }
        }
        baseball_list.append(baseball_dict)


with open('../fixtures/baseball_API.json', 'w') as f:
    f.write(json.dumps(baseball_list))

# with open('baseball_API.json', 'r') as f:
#     print(f.read())