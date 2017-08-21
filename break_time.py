""""
wait 2 hours 
open browser
"""
import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on {}".format(time.ctime()))
while(break_count < total_breaks):
	time.sleep(7200)
	webbrowser.open("https://www.youtube.com/watch?v=aZ5gkJDmZv4")
	break_count = break_count + 1
