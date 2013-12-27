import retrieval
import db

def main():
	player_name = 'SupremePinhead'
	obj = retrieval.get_player_object_from_name(player_name)
	mydb = db.DB()
	mydb.insert(obj)
	print mydb.get_player_by_name(player_name)


if (__name__ == '__main__'):
	main()
