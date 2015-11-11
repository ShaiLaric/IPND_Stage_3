# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
# 1. When user logs on, start a counter.
# 2. While counter is < 3:
#    2a. Start a timer that counts 120 minutes
#	 2b. At 120 minutes, call a "take_break()" function
# 3. take_break() function:
#    3a. Display a "Take a break" message
#    3b. Open a browser window; link to the appropriate video
#    3c. Potentially, close window once video is done?
#    3d. Return that break is over
# 4. Increment the counter
# 
# Thought: Add an option to warn that a break is approaching and
# allow user to postpone the break by some amount of time.

import time
import webbrowser

def take_break():
    breaks = 0
    
    print "This program started at " + time.ctime()
    while breaks < 3:
        time.sleep(5)
        print "It's " + time.ctime() + ", so take a break!"
        webbrowser.open("https://www.youtube.com/watch?v=B5xUiayK-Pc")
        breaks += 1

take_break()