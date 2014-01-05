import retrieval
import db
import sys

def main(player_name):
	obj = retrieval.get_player_object_from_name(player_name)
	mydb = db.DB()
	mydb.insert(obj)
	print mydb.get_player_from_name(player_name)


if (__name__ == '__main__'):
	print sys.argv[1]
	main(sys.argv[1])
