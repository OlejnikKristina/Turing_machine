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