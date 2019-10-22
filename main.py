# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    main.py                                            :+:    :+:             #
#                                                      +:+                     #
#    By: krioliin <krioliin@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 13:21:33 by krioliin       #+#    #+#                 #
#    Updated: 2019/10/21 18:30:46 by krioliin      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import argparse
import sys
import json

from validation import data_validation
from print_info import print_info
from turing_machine import set_turing_machine
	
def get_params():
	parser = argparse.ArgumentParser(description = 'Turing machine')
	parser.add_argument('json_file', help = 'json machine description')
	parser.add_argument('commands', help = 'instructions fot Turing machine')
	args = parser.parse_args()
	return args

def main():
	args = get_params()
	machine_descript = data_validation(args)
	print_info(machine_descript)
	set_turing_machine(args.commands, machine_descript)

main()