from sportsipy.nfl.teams import Teams, Schedule
import json

football_list = []
teams = Teams(2021)
for team in teams:
    for game in Schedule(f'{team.abbreviation}'):
        football_dict = {
            'model':'event_manager.event',
            'fields': {
                'sport': 'football',
                'team': team.abbreviation,
                'date': game.datetime.strftime("%Y-%m-%d"),
                'opponent': game.opponent_abbr,
                'location': game.location
            }
        }
        football_list.append(football_dict)


with open('../fixtures/football_API.json', 'w') as f:
    f.write(json.dumps(football_list))