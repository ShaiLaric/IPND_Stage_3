# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
# Step 1: Locate the directory with the files.
# Step 2: Generate a list of the files.
# Step 3: Loop through each file in the list.
# Step 4: In the loop, use a string function to strip out the numbers at the beginning of the name
# Step 4: Rename the file with the stripped string.

import os

def rename_files():
	# get filenames from a folder
	file_list = os.listdir(r"C:\Users\slaric\Documents\Education\Udacity\Intro to Programming\IPND_Stage_3\prank")
	# print file_list
	saved_path = os.getcwd()
	print ("CWD is: " + saved_path)
	os.chdir(saved_path + "\prank")
	saved_path = os.getcwd()
	print ("CWD is now: " + saved_path)

	# for each file, rename the filename
	for file_name in file_list:
		print("Old name is: " + file_name)
		os.rename(file_name, file_name.translate(None, "0123456789"))
		print("New name is: " + file_name.translate(None, "0123456789"))

rename_files()