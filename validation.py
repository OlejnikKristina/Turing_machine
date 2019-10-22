# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    validation.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: krioliin <krioliin@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 13:21:33 by krioliin       #+#    #+#                 #
#    Updated: 2019/10/22 13:03:00 by krioliin      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import json

def check_json_input(json_file):
	with open(json_file, 'r') as read_file:
		try:
			machine_descript = json.load(read_file)
		except:
			print("Error! Machine description need to be a json format file.")
			sys.exit()
		return machine_descript

def check_user_input(commands, machine_descript):
	for command_char in commands:
		counter = False
		for alphabet_char in machine_descript["alphabet"]:
			if command_char == alphabet_char and machine_descript["blank"] != command_char:
				counter = True
		if counter == False:
			print("Turing machin doesn't support given instructions")
			print("Check allowed alphabet:")
			print(machine_descript["alphabet"])
			sys.exit()

def data_validation(args):
	machine_descript = check_json_input(args.json_file)
	check_user_input(args.commands, machine_descript)
	return machine_descript
