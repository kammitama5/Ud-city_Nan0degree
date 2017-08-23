#!python2
import media 
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://img1.wikia.nocookie.net/__cb20140816182710/disney/images/4/4c/Toy-story-movie-posters-4.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
						
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
					"A marine on an alien planet",
					"https://www.movieposter.com/posters/archive/main/101/MPW-50968",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")
					
#print(avatar.storyline)

#avatar.show_trailer()

willy_wonka = media.Movie("Willie Wonka"
						  , "A boy wins a golden ticket to a magical chocolate factory",
						  "http://images.huffingtonpost.com/2015-09-08-1441712584-9265331-WillyWonkaandtheChocolateFactorymovieposter.jpg",
						  "https://www.youtube.com/watch?v=2cBja3AbahY")
						  
#willy_wonka.show_trailer()

# school of rock
# ratatouille
# midnight in paris 
# hunger games

movies = [toy_story, avatar, willy_wonka]				
fresh_tomatoes.open_movies_page(movies)		
						  