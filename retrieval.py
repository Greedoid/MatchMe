from hercule import Request
from config import api_key

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

def get_player_object(player_id):
	obj = {}
	r = Request(api_key)
	player_name = r.get_name_from_id(player_id)
	obj['name'] = player_name 
	obj['summoner_id'] = player_id
	obj['champ_vector'] = set_vector(player_name)
	obj['tier'], obj['rank'] = get_rank_and_tier_from_id(player_id)
	return obj

def get_rank_and_tier_from_id(player_id):
	r = Request(api_key)
	for item in r.get_leagues_from_id(player_id)[str(player_id)]['entries']:
		if item['playerOrTeamId'] == str(player_id):
			return item['tier'], item['rank']
	

def get_player_object_from_name(player_name):
	player_id = Request(api_key).get_id_from_name(player_name)
	return get_player_object(player_id)

def get_played_champs_in_order_from_name(player_name):
        r = Request(api_key)
        ranked_obj = r.get_ranked_summary_from_name(player_name, 'na', 'SEASON3')
        return get_played_champs_in_order(ranked_obj)

def weighted(won, total): #Can't go just by total - somone could play a champ a lot and just be bad at them. Conversely, someone could be 6-0, but it's not representative
        percent = (float(won)/float(total))
        return percent*float(total*.5)

def set_vector(player_name):
	w0 = init_vector()
	champs = get_played_champs_in_order_from_name(player_name)
	for guy in champs:
		w0[guy[2]] = 1
	return w0

def init_vector():
	champs = {}
	data = Request(api_key).get_champions()
	for item in data['champions']:
		champs[item['name']] = 0
	return champs

if __name__ == '__main__':
	print get_rank_and_tier_from_id(26483194)
