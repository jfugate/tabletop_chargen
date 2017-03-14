#!/usr/bin/python

#This script will form the menus, and call the functions that both build and store relevant information, then display it to the user

def main_menu():
	menu = {}
	menu['1']="Pick a Name"
	menu['2']="Roll Stats"
	menu['3']="Pick a Class"
	menu['4']="Pick an Alignment"
	menu['5']="Pick a Race"
	menu['6']="Build Sheeet"
	menu['7']="Exit"

	while True:
		options=menu.keys()
		options.sort()
		print("Please Choose the options in order.")
		  for entry in options:
		  	print entry, menu[entry]

		 selection=raw_input("Your Choice: ")
		 if selection == 1:
		 	#function code for inserting character name to be
		 	#stored in a separate file, returning a variable that we will later pass
		 	#to the build funciton
		 elif selection == 2:
		 	#function code for stat rolling, will include two options
		 	#traditional 5d6 method and the d10+8 method
		 	#this will also refer to a json doc to be made soon with ability modifier to be stored/returned here
		 elif selection == 3:
		 	"""going to begin with base classes only, will expand after. will refer to a json doc to be created
		 	with nearly all class information. it is important that stats are rolled first so there should be a 
		 	check to make sure that is the case, as we need to do character level and skills, etc here. Multi-classing
		 	not available in version alpha. All functions from the main_menu() funtion will be in their own files,
		 	and imported at the top of this script once created."""
		 elif selection == 4:
		 	"""This will be a simple list of all 9 alignments, and return the user's choice"""
		 elif selection == 5:
		 	"""Race, this honestly should come before class, and after abilities scores. Abiliy scores will be assigned at time
		 	of rolling. Note to self to move this above class but below stats."""
		 elif selection == 6:
		 	"""Build sheet function will provide some pretty form of output in a .txt file, that can either be printed, or viewed
		 	to transfer the information to a legit character sheet"""
		 elif selection == 7:
		 	break
		 else:
		 	print("Unknown Option Selected!")
