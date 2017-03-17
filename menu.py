#!/usr/bin/python

#This script will form the menus, and call the functions that both build and store relevant information, then display it to the user
import char_name
import stat_roller

def main_menu():
	menu = {}
	menu['1']="Pick a Name"
	menu['2']="Roll Stats"
	menu['3']="Pick a Race"
	menu['4']="Pick a Class"
	menu['5']="Pick an Alignment"
	menu['6']="Build Sheeet"
	menu['7']="Exit"

	#initial set of option use vars, this way they won't reset during the while-true loop
	option_1=False
	option_2=False
	option_3=False
	option_4=False
	option_5=False
	option_6=False

	while True:
		options=menu.keys()
		options.sort()
		print("Please Choose the options in order.")
		  for entry in options:
		  	print entry, menu[entry]

		 selection=raw_input("Your Choice: ")
		 if selection == 1:
		 	name=str(char_name.name_saver())
		 	option_1=True
		 elif selection == 2:
		 	stat_roller.scores()
		 	option_2=True
		 elif selection == 3:
		 	"""Race, will need ability scores as parameters, just in case a race is chosen than alters those scores"""		 	
		 elif selection == 4:
		 	"""going to begin with base classes only, will expand after. will refer to a json doc to be created
		 	with nearly all class information. it is important that stats are rolled first so there should be a 
		 	check to make sure that is the case, as we need to do character level and skills, etc here. Multi-classing
		 	not available in version alpha. All functions from the main_menu() funtion will be in their own files,
		 	and imported at the top of this script once created."""		 	
		 elif selection == 5:
		 	"""This will be a simple list of all 9 alignments, and return the user's choice"""
		 elif selection == 6:
		 	"""Build sheet function will provide some pretty form of output in a .txt file, that can either be printed, or viewed
		 	to transfer the information to a legit character sheet"""
		 elif selection == 7:
		 	break
		 else:
		 	print("Unknown Option Selected!")
