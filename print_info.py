# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    print_info.py                                      :+:    :+:             #
#                                                      +:+                     #
#    By: krioliin <krioliin@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 13:21:33 by krioliin       #+#    #+#                 #
#    Updated: 2019/10/20 14:32:51 by krioliin      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import json

def print_info(machine_descript):
	print("Alphabet:", machine_descript["alphabet"])
	print("States  :", machine_descript["states"])
	print("Initial :", machine_descript["initial"])
	print("Finals  :", machine_descript["finals"])