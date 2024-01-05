import os
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1]
	if not os.path.isfile(filename):
		print('[*] '+filename+'does mot exist')
		exit(0)
	if not os.access(filename.os.R_OK):
		print('[*]' +filename+'Access denied')
		exit(0)
	print('[*] Reading vulnerability from '+filename)
		 
