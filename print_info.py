# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    print_info.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: krioliin <krioliin@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 13:21:33 by krioliin       #+#    #+#                 #
#    Updated: 2019/10/21 20:18:16 by krioliin      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import json

def print_info(machine_descript):
	WHITE = '\033[1;37;10m'
	BLUE = '\033[1;34;10m'
	MAGENTA = '\033[1;35;10m'
	i = 0
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
	print('\n' + 80 * '* ' + '\n')