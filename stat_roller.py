#!/usr/bin/python

"""This script will provide a couple of options for stat rolling, and then allow the user to assign the
   values of the rolls to the corresponding character ability"""

import random

def scores():
	score_menu={}
	score_menu['1']="Traditional D6 method"
	score_menu['2']="Patton's Patented D12 Method*TM"

	print("Please choose a rolling method below:")
	options=score_menu.keys()
	options.sort()

	for entry in options:
		print entry, options[entry]

	roll_method=raw_input("Method choide: ")

	if roll_method == 1:
		print("Traditional Method selected! Rolling up 6 random numbers")
		score_range=range(3, 18)
		score_set=[]
		for i in range(1, 6):
			score_set.append(random.choice(score_range))
		print("Scores generated, now to assign them, keep in mind what class you might choose!")
		assign_scores(score_set)
	elif roll_method == 2:
		print("Patton's D12 method selected! Rolling up 6 random numbers")
		score_range=range(9, 20)
		score_set=[]
		for i in range(1, 6):
			score_set.append(random.choice(score_range))
		print("Scores generated, now to assign them, keep in mind what class you might choose!")
		assign_scores(score_set)


	def assign_scores(my_list):
		print("Here are the scores: ", array_dump(my_list))
		strength=raw_input("Please input the value for strength: ")
		my_list.remove(strength)
		dexterity=raw_input("Please input the value for dexterity: ")
		my_list.remove(dexterity)
		constiution=raw_input("Please input the value for constitution: ")
		my_list.remove(constitution)
		intelligence=raw_input("Please input the value for intelligence: ")
		my_list.remove(intelligence)
		wisdom=raw_input("Please input the value for wisdom: ")
		my_list.remove(wisdom)
		charisma=raw_input("Please input the value for charisma: ")
		my_list.remove(charisma)
		