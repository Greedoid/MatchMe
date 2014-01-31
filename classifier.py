from db import DB
import sys
import math
from retrieval import init_vector
import random

class Classifier:
	
	def __init__(self):
		self.db = DB()
		self.w0 = init_vector()
		self.player_list = self.db.get_all_players()
		self.player_vector = self.get_list()

	def get_distances(self, player_id):
		sublist = []
		for item in self.player_list:
			if item['summoner_id'] == player_id:
				prime_vector = item['champ_vector']
			else:
				sublist.append(item)
		for player in sublist:
			print 'Distance from ' + player['name'] + ': ' + str(self.euclidean_distance(prime_vector, player['champ_vector']))
	
	def get_list(self): #Returns a subset of items from the DB with just (Vector, Name) - used for kmeans
		sublist = []
		for item in self.player_list:
			sublist.append((item['champ_vector'], item['name']))
		return sublist

	def euclidean_distance(self, vec1, vec2):
		total = 0
		for item1, item2 in zip(vec1.values(), vec2.values()):
			total = total + ((item1 - item2)**2)
		return math.sqrt(total)
	
	def random_centroids(self, num):
		return random.sample(self.player_vector, num)

	def kmeans(self):
		centroids = self.random_centroids(5)
		clusters = []
		for centroid in centroids:
			clusters.append(centroid) #seed clusters w/ appropriate centroids
		for item in self.player_vector:
			best_distance = 10000
			current_centroid = 0
			for centroid in centroids:
				current_distance = self.euclidean_distance(centroid[0], item[0])
				if current_distance < best_distance:
					current_centroid = centroid
					best_distance = current_distance
			print "Best fit for " + item[1] + ": current_centroid " + str(current_centroid[1])


if __name__ == '__main__':
	classy = Classifier()
	#classy.get_distances(20386296)
	#print classy.random_centroids(5)
	classy.kmeans()




