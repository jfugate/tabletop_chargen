#!/usr/bin/python

"""This script will provide a couple of options for stat rolling, and then allow the user to assign the
   values of the rolls to the corresponding character ability"""

import random, json

stats={}

def calculate_mods(strength, dex, con, intelligence, wis, cha):
	with open('dicts/ability_modifiers.json') as mods_file:
		mods = json.load(mods_file)
	stats['str_mod'] = mods['ability'][0][strength]
	stats['dex_mod'] = mods['ability'][0][dex]
	stats['con_mod'] = mods['ability'][0][con]
	stats['int_mod'] = mods['ability'][0][intelligence]
	stats['wis_mod'] = mods['ability'][0][wis]
	stats['cha_mod'] = mods['ability'][0][cha]
	with open('ability_temp.json', 'w') as tmp_json:
		json.dump(stats, tmp_json)
	

def assign_scores(my_list):
	print("Here are the scores: ", my_list)
	stats['strength']=raw_input("Please input the value for strength: ")
	my_list.remove(int(stats['strength']))
	stats['dexterity']=raw_input("Please input the value for dexterity: ")
	my_list.remove(int(stats['dexterity']))
	stats['constitution']=raw_input("Please input the value for constitution: ")
	my_list.remove(int(stats['constitution']))
	stats['intelligence']=raw_input("Please input the value for intelligence: ")
	my_list.remove(int(stats['intelligence']))
	stats['wisdom']=raw_input("Please input the value for wisdom: ")
	my_list.remove(int(stats['wisdom']))
	stats['charisma']=raw_input("Please input the value for charisma: ")
	my_list.remove(int(stats['charisma']))
	print("now calculating modifiers")
	calculate_mods(stats['strength'], stats['dexterity'], stats['constitution'], stats['intelligence'], stats['wisdom'], stats['charisma'])
	""" will probably build a dictionary as the return object that goes back to the main script.
	    this is likely the easiest way to handle the data
	    for testing only I will print each variable separately"""
	#print strength, ' ', dexterity, ' ', constitution, ' ', intelligence, ' ', wisdom, ' ', charisma

def scores():
	score_menu={}
	score_menu['1']="Traditional D6 method"
	score_menu['2']="Patton's Patented D12 Method*TM"

	
	options=score_menu.keys()
	options.sort()
	print("Please choose a rolling method below:")
	for entry in options:
		print(entry, score_menu[entry])

	roll_method=raw_input("Method choide: ")
	#print(roll_method)

	if roll_method == '1':
		print("Traditional Method selected! Rolling up 6 random numbers")
		score_range=range(3, 18)
		score_set=[]
		for i in range(0, 6):
			score_set.append(random.choice(score_range))
		print("Scores generated, now to assign them, keep in mind what class you might choose!")
		assign_scores(score_set)
	elif roll_method == '2':
		print("Patton's D12 method selected! Rolling up 6 random numbers")
		score_range=range(9, 20)
		score_set=[]
		for i in range(0, 6):
			score_set.append(random.choice(score_range))
		print("Scores generated, now to assign them, keep in mind what class you might choose!")
		assign_scores(score_set)
	else:
		print("Invalid choice")
		scores()

scores()