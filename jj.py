import sys
import json

# for penis_size in range(12, 22):
# 	print("right now im: ", penis_size, " cm long")

# def print_text(text):
# 	x = 3
# 	bla = x + 5
# 	bla = 0
# 	print(text)

# def give_5():
# 	return 5

# def return_a_lot():
# 	return 69, "hello", 2, (2 + 5)

# print_text(give_5())

# print(return_a_lot())

# some_data = return_a_lot()

# for x in some_data:
# 	print(x)

# "check_finish": [
# 			{"read": ".", "to_state": "show_result",  "write": ".", "action": "LEFT"},
# 			{"read": "+", "to_state": "go_to_start", "write": "+", "action": "LEFT"},
# 			{"read": "a", "to_state": "to_begining", "write": "a", "action": "LEFT"},
# 			{"read": "b", "to_state": "to_begining", "write": "b", "action": "LEFT"},
# 			{"read": "c", "to_state": "to_begining", "write": "c", "action": "LEFT"},
# 			{"read": "d", "to_state": "to_begining", "write": "d", "action": "LEFT"}
# 		],


"show_result": [
			{"read": ".", "to_state": "finish", 	 "write": "Y", "action": "RIGHT"},
			{"read": "+", "to_state": "show_result", "write": "Y", "action": "RIGHT"},
			{"read": "a", "to_state": "show_result", "write": "Y", "action": "RIGHT"},
			{"read": "b", "to_state": "show_result", "write": "Y", "action": "RIGHT"},
			{"read": "c", "to_state": "show_result", "write": "Y", "action": "RIGHT"},
			{"read": "d", "to_state": "show_result", "write": "Y", "action": "RIGHT"}
		],

class Jelmer:
	my_name = "heer jelmer"
	
	def __init__(self, new_name):
		self.my_name = new_name

	def print_my_name_with(self, girlfriend):
		print(self.my_name, " with ", girlfriend)

x = Jelmer("thoams")
x2 = Jelmer("REAL Jelmer")

x.print_my_name_with("kristian")
x2.print_my_name_with("Kristina")

print()

print(x.my_name)
print(x2.my_name)

x.my_name = "KAKAKAKKAKAKAKAKAKA"
x.print_my_name_with("Krisina")

# f = open("mashine_descrip/unary_sub.json", "r")

# json_object = json.load(f)

# for character in json_object["alphabet"]:
# 	print(character)