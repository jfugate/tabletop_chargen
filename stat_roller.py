#!/usr/bin/python

"""This script will provide a couple of options for stat rolling, and then allow the user to assign the
   values of the rolls to the corresponding character ability"""

import random
def assign_scores(my_list):
	print("Here are the scores: ", my_list)
	strength=raw_input("Please input the value for strength: ")
	my_list.remove(int(strength))
	dexterity=raw_input("Please input the value for dexterity: ")
	my_list.remove(int(dexterity))
	constitution=raw_input("Please input the value for constitution: ")
	my_list.remove(int(constitution))
	intelligence=raw_input("Please input the value for intelligence: ")
	my_list.remove(int(intelligence))
	wisdom=raw_input("Please input the value for wisdom: ")
	my_list.remove(int(wisdom))
	charisma=raw_input("Please input the value for charisma: ")
	my_list.remove(int(charisma))
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