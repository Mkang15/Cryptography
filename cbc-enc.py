import argparse
from Crypto.Cipher import AES

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--input",help="input file")
	parser.add_argument("-o","--output",help="output file")
	parser.add_argument("-k","--key",help="key file")
	args=parser.parse_args()

	if args.input:
		inputf = args.input
	if args.output:
		outputf = args.output
	if args.key:
		keyf = args.key
	return inputf, outputf, keyf

def aesCbc(infile,outfile,key):
	
	#Run AES get IV	
	cK = key
	IV = AES.new(cK,AES.MODE_ECB, nonce=nonce)

	#XOR IV with Block of Message.
	
	
	#Run AES on New Xored Block
	
	
	#Xor That Output with next Block.

def blockAndBuff(inn):
	#convert message from string into Bytes.
	mess = bytes.fromhex(inn)

	#cut Bytes into an array with blocks size of 128 bits(8 byte)
	
	


if __name__=="__main__":

	infile,outfile,key = parse_args()
	
	f = open(infile,'r')
	inn = f.read()
	
	BlockandBuff(inn);


	fkey = open(key,'r')
	keyinn = fkey.read()
