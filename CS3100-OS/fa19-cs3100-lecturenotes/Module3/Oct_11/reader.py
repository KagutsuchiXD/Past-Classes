import sys

name = sys.argv[1]

while True:
	print(f"Reader '{name}' attempts to open lorem.txt for reading...")
	f = open("lorem.txt", mode="r")

	for line in f:
		for word in line.split():
			word = word.strip()
			print(f"Reader '{name}' read the word {word}")
	f.close()
