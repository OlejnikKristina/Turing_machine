import argparse
import sys
import json

def get_params():
	parser = argparse.ArgumentParser(description = 'Turing machine')
	parser.add_argument('json_file', help = 'json machine description')
	parser.add_argument('commands', help = 'instructions fot Turing machine')
	args = parser.parse_args()
	return args
 

args = get_params()
data_validation(args)