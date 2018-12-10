import os
import sys

if (len(sys.argv) < 3 or len(sys.argv) > 3): 
	print("""Provide commandline arguments: program name, extension, directory to search
		Example usage: python find.py, .txt, $HOME""")
	exit()

extension = str(sys.argv[1])
path = str(sys.argv[2])

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(extension):
             print(os.path.join(root, file))
