from sportsipy.nhl.teams import Teams, Schedule
import json


hockey_list = []
teams = Teams(2022)
for team in teams:
    for game in Schedule(f'{team.abbreviation}'):
        hockey_dict = {
            'model':'event_manager.event',
            'fields': {
                'sport': 'hockey',
                'team': team.abbreviation,
                'date': game.datetime.strftime("%Y-%m-%d"),
                'opponent': game.opponent_abbr,
                'location': game.location
            }
        }
        hockey_list.append(hockey_dict)


with open('../fixtures/hockey_API.json', 'w') as f:
    f.write(json.dumps(hockey_list))

# with open('hockey_API.json', 'r') as f:
#     data = json.load(f)
#     for team in data.items():
#         for x,y in team[1].items():
#             # print(f'{x} {team[0]} vs {y["opponent"]}')
#             # print(type(datetime.datetime.strptime(x, '%Y-%m-%d')))
#             new_event = Event(
#                 sport = 'hockey',
#                 date = datetime.datetime.strptime(x, '%Y-%m-%d'),
#                 is_home_team = True if y['location'] == 'Home' else False,
#                 team = team[0],
#                 opponent = y["opponent"]
#             )