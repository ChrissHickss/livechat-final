import json

# open JSON
f = open('../fixtures/stats-api-mlb.json')

# return JSON object as dict
data = json.load(f)

dates = data['dates']
one_game = data['dates'][1]['games'][0]
one_game_pretty = json.dumps(one_game, indent=2)


events = []

for date in dates:
    for game in date['games']:
        game_dict = {
        'model': 'event_manager.event',
        'fields': {
                'sport': 'baseball',
                'team': game['teams']['home']['team']['name'],
                'day_or_night': game['dayNight'],
                'date': game['gameDate'],
                'opponent':game['teams']['away']['team']['name'],
                'location': game['venue']['name']
        }
        }
        events.append(game_dict)


# Serializing json 
json_object = json.dumps(events, indent = 4)
  
# Writing to sample.json
with open("../fixtures/baseball_API_with_times.json", "w") as outfile:
    outfile.write(json_object)


