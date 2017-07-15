#!/usr/bin/python
"""this is the race seletcion menu. We will choose one of the basic
   races only in the first version. Expanded and third party races to be added
   much later"""

import stat_roller

menu = {}
menu['1']="Human"
menu['2']="Elf"
menu['3']="Half-Elf"
menu['4']="Half-Orc"
menu['5']="Gnome"
menu['6']="Dwarf"
menu['7']="Halfling"

print("Welcome to the race menu, please pick a race:")
while True:
	options=menu.keys()
	options.sort()
	print("Please Choose the options in order.")
	  for entry in options:
	  	print entry, menu[entry]
	selection=raw_input("Your Choice: ")

	if selection == '1':
		print("Human selected. Finding bonuses...")
		'''Figure out dynamically updating stats by importing the data from the previous
		function set'''
		speed="30 Ft"
		size="Medium"
		#Make language a function later to let user choose from list
		laguanges="Common, plus one per intelligence modifier (Except secret)"
		other=["One bonus feat", "One extra skill point at lvl 1 and 1/lvl"]
		