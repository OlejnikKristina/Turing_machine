# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    print_info.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: krioliin <krioliin@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 13:21:33 by krioliin       #+#    #+#                 #
#    Updated: 2019/10/22 22:18:13 by krioliin      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import json

def print_description(program_descrip):
	i = 0
	for c in program_descrip:
		print(c, end='', sep='')
		if i == 77:
			i = 0
		i += 1
	print('\n')

def print_header(program_name):
	WHITE = '\033[1;37;10m'
	spaces = 41 - len(program_name) / 2
	print(WHITE, '\n', "* " * 42, sep='')
	print('*', ' ' * 79, '*')
	print('*', ' ' * int(spaces), program_name, ' ' * int(spaces), '*', sep='', )
	print('*', ' ' * 79, '*')
	print("* " * 42, '\n', sep='')

def print_info(machine_descript):
	WHITE = '\033[1;37;10m'
	BLUE = '\033[1;34;10m'
	MAGENTA = '\033[1;35;10m'
	i = 0
	print_header(machine_descript["name"])
	try:
		if machine_descript["description"]:
			print_description(machine_descript["description"])
	except:
		print()
	print(BLUE, "Alphabet: ", WHITE, machine_descript["alphabet"], sep='')
	print(BLUE, "States :  ", WHITE, sep='', end='')
	for state in machine_descript["states"]:
		if i == 5:
			i = 0
			print('\n', ' ' * 9, end='')
		print(MAGENTA, '[', WHITE, state, MAGENTA, '] ', end='', sep='')
		i += 1
	print('\n', BLUE, "Initial : ", WHITE, machine_descript["initial"], sep='')
	print(BLUE, "Finals  : ", WHITE, machine_descript["finals"], sep='')
	print('\n' + 42 * '* ' + '\n')
