import sys

if len(sys.argv) < 2:
	print "ERROR"
	exit(-1)

if len(sys.argv[1]) % 2 != 0:
	print "ERROR"
	exit(-1)

sys.stdout.write(sys.argv[1].decode("hex"))
