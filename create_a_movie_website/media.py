#!python2
'''
Things for class movie to remember:
- title 
- storyline
- poster_image
- trailer_youtube
'''
'''
-both movie and Tvshow would inherit title and duration from Video

class Movie(Video):
-title
-storyline
-poster_image
-youtube_trailer

def show_trailer()

class TvShow(Video):
-title
-season
-episode
-tv_station

def get_local_listing()

class Video():
-title
-duration
'''
import webbrowser
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	
	
'''
Things for class movie to remember:
- title 
- storyline
- poster_image
- trailer_youtube
'''
'''
-both movie and Tvshow would inherit title and duration from Video

class Movie(Video):
-title
-storyline
-poster_image
-youtube_trailer

def show_trailer()

class TvShow(Video):
-title
-season
-episode
-tv_station

def get_local_listing()

class Video():
-title
-duration
'''