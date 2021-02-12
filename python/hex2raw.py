#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
	print("Error")
	exit(-1)

hexString = sys.argv[1]

if len(hexString) & 1 == 1 and len(hexString) >= 2:
	print(f"Bad length ({len(hexString)}) of string \"{hexString}\", expected length as multiple of 2.")
	exit(-1)

if hexString[0:2] == '0x' or hexString[0:2] == '0X':
	hexString = hexString[2:]

sys.stdout.buffer.write(bytearray.fromhex(hexString))
