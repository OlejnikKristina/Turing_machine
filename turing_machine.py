# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    turing_machine.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: krioliin <krioliin@student.codam.nl>         +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 13:21:33 by krioliin       #+#    #+#                 #
#    Updated: 2019/10/21 14:14:49 by krioliin      ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import json

def display_current_condition(machine):
	print('(', machine.state_name, ', ', sep='', end='')
	print(machine.character, ')', sep='', end='')
	print(" -> ", end='')

def display_next_condition(machine):
	print('(', machine.state_name, ', ', sep='', end='')
	print(machine.character, ', ', sep='', end='')
	print(machine.moving, ')', sep='')

class TuringMachine:
	def __init__(self, state, state_name, character, moving, head):
		self.state_name = state_name
		self.state = state
		self.character = character
		self.moving = moving
		self.head = head

def instruct_position(command, state):

	instructions_in_state = len(state)
	num = 0

	while num < instructions_in_state:
		if state[num]["read"] == command:
			return num
		num += 1


def init_turing_machine(command, machine_desc):

	current_state_name = machine_desc["initial"]
	# current_state_name = ''.join(current_state_name)
	
	# print("current_state_name: ", current_state_name)
	# print("current_state: ", machine_desc["transitions"]["find_letter"])
	current_state = machine_desc["transitions"][current_state_name]


	instruct_pos = instruct_position(command[0], current_state)

	move_to = current_state[instruct_pos]["action"]
	machine = TuringMachine(current_state, current_state_name, command[0], move_to, 0)
	return machine

def display_tape(commands, head):

	BLUE = '\033[1;34;10m'
	WHITE = '\033[1;37;10m'
	MAGENTA = '\033[1;35;10m'
	commands_len = len(commands)
	i = 0

	print(BLUE, '[', sep='', end='')
	while (i < commands_len):
		if i != head:
			print(WHITE, commands[i], sep='', end='')
		else:
			print(MAGENTA, commands[i], WHITE, sep='', end='')
		i += 1
	print(BLUE, '] ', WHITE, sep='', end='')

def execute_commands(commands, head, char_to_put):
	if commands[head] == char_to_put:
		return commands
	else:
		refreshed_commands = list(commands)
		refreshed_commands[head] = char_to_put
		refreshed_commands = ''.join(refreshed_commands)
		return refreshed_commands

def run_turing_machine(machine, commands, machine_desc):

	stop_blank = ''.join(machine_desc["finals"])

	instruct_pos = instruct_position(commands[machine.head], machine.state)
	machine.character =  machine.state[instruct_pos]["write"]
	machine.moving = machine.state[instruct_pos]["action"]
	machine.state_name = machine.state[instruct_pos]["to_state"]
	if machine.state_name == stop_blank:
		display_next_condition(machine)
		sys.exit() 
	machine.state = machine_desc["transitions"][machine.state_name]

	display_next_condition(machine)
	refreshed_commands = execute_commands(commands, machine.head, machine.character)
	if machine.moving == "RIGHT":
		machine.head += 1
	elif machine.moving == "LEFT":
		machine.head -= 1
	else:
		sys.exit()
	return refreshed_commands


def set_turing_machine(command, machine_desc):
	i = 0
	machine = init_turing_machine(command, machine_desc)
	# command = command.rjust(len(command) + 1, '.')
	command = command.ljust(len(command) * 2, '.')
	while i < 1000:
		display_tape(command, machine.head)
		#display_current_condition(machine)
		command = run_turing_machine(machine, command, machine_desc)
		i += 1
	
