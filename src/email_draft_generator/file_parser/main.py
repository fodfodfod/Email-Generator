import sys
import argparse
import json
import email_draft_generator.file_parser.text_parser as text_parser

def main():
	# Command-line arguments
	parser = argparse.ArgumentParser(
		prog='email-list-parser',
		description='Takes a list of E-mail addresses and turns it into a JSON file.'
	)

	parser.add_argument('infile', type=argparse.FileType('r'), help='the list of e-mail addresses to parse')

	args = parser.parse_args()

	try:
		companies = text_parser.parse(args.infile.readlines())
	except:
		raise ValueError("Invalid input file")

	json.dump(companies, sys.stdout, indent="\t")