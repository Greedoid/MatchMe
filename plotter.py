from hercule import Request
from config import api_key
import retrieval

def init_vector():
	champs = {}
	data = Request(api_key).get_champions()
	for item in data['champions']:
		champs[item['name']] = 0
	return champs

def set_vector(player_name):
	w0 = init_vector()
	champs = retrieval.get_played_champs_in_order_by_name(player_name)
	for guy in champs:
		w0[guy[2]] = 1
	return w0


if (__name__ == '__main__'):
	print set_vector('Greedoid')

