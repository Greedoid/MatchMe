from hercule import Request
from config import api_key

def get_rel_info(player_name):
	r = Request(api_key)
	obj = {}
	player_id = r.get_id_from_name(player_name)
	leagueinfo = r.get_leagues_from_id(player_id)
	obj['name'] = 'Greedoid'
	obj['summoner_id'] = player_id
	obj['league'] = leagueinfo
	stat_summary = r.get_stats_summary_from_id(player_id, 'na', 'SEASON3')
	obj['stats'] = stat_summary
	ranked_summary = r.get_ranked_summary_from_id(player_id, 'na', 'SEASON3')
	obj['ranked'] = ranked_summary
	games = r.get_recent_games_from_id(player_id)
	obj['games'] = games
	return obj 

def get_played_champs_in_order(ranked_obj):
	champs = []
	for item in ranked_obj['champions']:
		total = item['stats']['totalSessionsPlayed']
		won = item['stats']['totalSessionsWon']
		if item['name'] == 'Combined':
			overall_wins = item['stats']['totalSessionsWon']
		else:
			champs.append((won, total, item['name']))
	champs = filter(lambda y: float(y[0])/float(overall_wins) >= .05, champs) 
	champs.sort(key = lambda x: weighted(x[0], x[1]), reverse=True)
	return champs

def get_played_champs_in_order_by_name(player_name):
	r = Request(api_key)
	ranked_obj = r.get_ranked_summary_from_name(player_name, 'na', 'SEASON3')
	return get_played_champs_in_order(ranked_obj)


def weighted(won, total): #Can't go just by total - somone could play a champ a lot and just be bad at them. Conversely, someone could be 6-0, but it's not representative
	percent = (float(won)/float(total))
	return percent*float(total*.5)

if (__name__ == "__main__"):
	for item in get_played_champs_in_order_by_name('Scarra'):
		print item

