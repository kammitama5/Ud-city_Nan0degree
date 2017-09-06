#!python2
## import webrowser module
import webbrowser

## initialize class
class Movie():
	
	## define constructor method with arguments -> movie_title, movie_storyline, poster_image, trailer_youtube
	## instances of method defined
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
	## open trailer from Youtube url using webbrowser
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) ## instance of method
	
	
