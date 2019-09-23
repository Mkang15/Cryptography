import argparse


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input",help="input file")
	parser.add_argument("-o","--output",help="output file")
	parser.add_argument("-k","--key",help="key file")
	args=parser.parse_args()

	if args.input:
		print(args.input)
	if args.output:
		print(args.output)
	if args.key:
		print(args.key)
