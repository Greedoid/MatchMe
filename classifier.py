from db import DB
import sys
import math
from retrieval import init_vector

class Classifier:
	
	def __init__(self):
		self.db = DB()
		self.w0 = init_vector()
		self.player_list = self.db.get_all_players()

	def get_distances(self, player_id):
		sublist = []
		for item in self.player_list:
			if item['summoner_id'] == player_id:
				prime_vector = item['champ_vector']
			else:
				sublist.append(item)
		for player in sublist:
			print 'Distance from ' + player['name'] + ': ' + str(self.euclidean_distance(prime_vector, player['champ_vector']))
	

	def euclidean_distance(self, vec1, vec2):
		total = 0
		for item1, item2 in zip(vec1.values(), vec2.values()):
			total = total + ((item1 - item2)**2)
		return math.sqrt(total)

if __name__ == '__main__':
	classy = Classifier()
	classy.get_distances(20386296)





