#!python2
import media 
import fresh_tomatoes

# toy story
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://img1.wikia.nocookie.net/__cb20140816182710/disney/images/4/4c/Toy-story-movie-posters-4.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
						
#print(toy_story.storyline)
# avatar
avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"https://www.movieposter.com/posters/archive/main/101/MPW-50968",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")
					
#print(avatar.storyline)

#avatar.show_trailer()

# willy_wonka
willy_wonka = media.Movie("Willie Wonka"
						  , "A boy wins a golden ticket to a magical chocolate factory",
						  "http://images.huffingtonpost.com/2015-09-08-1441712584-9265331-WillyWonkaandtheChocolateFactorymovieposter.jpg",
						  "https://www.youtube.com/watch?v=2cBja3AbahY")

# ratatouille
ratatouille = media.Movie("Ratatouille"
						  , "Anyone can cook.",
						  "http://www.pixartalk.com/wp-content/uploads/2009/06/ratfinlandtheatrical.jpg",
						  "https://www.youtube.com/watch?v=c3sBBRxDAqk&t=2s")

# the lego movie
the_lego_movie = media.Movie("The Lego Movie"
						  , "An ordinary Lego Man must save the world.",
						  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MDk1ODExN15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
						  "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

# hunger games						  
hunger_games = media.Movie("Hunger Games"
						  , "A Dystopian world of fighting to the death.",
						  "https://2982-presscdn-29-70-pagely.netdna-ssl.com/wp-content/uploads/2015/11/The-Hunger-Games-Poster1.jpg",
						  "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# list of all movie objects
movies = [toy_story, avatar, willy_wonka, ratatouille, the_lego_movie, hunger_games]				
fresh_tomatoes.open_movies_page(movies)		## open movies
						  