#! python
import sys
import csv

# Test Python version
# sys.stdout.write("hello from Python %s\n" % (sys.version,))

# Read data
with open('data.csv', 'rt', encoding='utf-8') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	
	# Show data
	for row in spamreader:
		string = ", ".join(row)
		print(string)