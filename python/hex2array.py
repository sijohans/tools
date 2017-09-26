#!/usr/bin/python

import sys
import re
import argparse

def main():

	usage = '''Usage:
$ python hex2array.py -n 3 12345678 aaff456678 0x12345678123456781223
[4] = { /* 0x12345678 */
        0x23, 0x34, 0x45, 0x56
};
[5] = { /* 0xaaff456678 */
        0xaf, 0xff, 0xf4, 0x45,
        0x56
};
[10] = { /* 0x12345678123456781223 */
        0x23, 0x34, 0x45, 0x56,
        0x67, 0x78, 0x81, 0x12,
        0x23, 0x34
};'''

	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
									 description='Create arrays from hex representations of byte arrays.',
									 epilog=usage)
	parser.add_argument('-n', default=4, type=int)
	parser.add_argument('strings', metavar='S', type=str, nargs='+',
						help='Hex representation of byte array to convert to array')

	try:
		args = parser.parse_args()
	except:
		parser.print_help()
		exit(0)

	search = re.compile(r'[^a-fA-F0-9]').search

	for hexString in args.strings:

		# String length must be a multiple of 2
		if len(hexString) & 1 == 1 and len(hexString) >= 2:
			print 'Bad length (%d) of string "%s", expected length as multiple of 2.' % (len(hexString), hexString)
			continue

		if hexString[0:2] == '0x' or hexString[0:2] == '0X':
			hexString = hexString[2:]

		# Hex representation may only include [a-fA-F0-9]
		if search(hexString):
			print 'Bad characters in string "%s", expected [a-fA-F0-9]' % hexString
			continue

		n = 1

		sys.stdout.write('[%d] = { /* 0x%s */\r\n\t' % ((len(hexString)/2), hexString))

		for i in range(0, len(hexString), 2):
			sys.stdout.write('0x%c%c' % (hexString[i], hexString[i+1]))
			if i + 2 == len(hexString):
				sys.stdout.write('\r\n')
			elif n % args.n == 0:
				sys.stdout.write(',\r\n\t')
			else:
				sys.stdout.write(', ')
			n += 1

		sys.stdout.write('};\r\n')

if __name__ == "__main__":
	main()
