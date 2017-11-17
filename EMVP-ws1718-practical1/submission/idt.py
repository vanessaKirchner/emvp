#! python
import sys
import csv
import numpy
import matplotlib.pyplot as plt;


# Test Python version
# sys.stdout.write("hello from Python %s\n" % (sys.version,))

# Exercise 2.1


# Read data
datalist = []

# Read data and save to list
with open('data.csv', 'rt', encoding='utf-8') as csvfile:
	data = csv.reader(csvfile, delimiter='\t', quotechar='|')
	datalist = list(data)

	
# Show data
#print(datalist)

# Show one element
#print(datalist[1][1])

			
		
# Exercise 2.2

# Remove invalid data points

erased = []
print(len(datalist))

for x in range(2,len(datalist)) :
		
	if (datalist[x][5] != '0') and (datalist[x][10] != '0'):
		erased.append(datalist[x])
			
print(len(erased))
	
# TODO: Sind das wirklich alle die Invalid sind?


# Show data points on image
image_name = 'stimuli.jpg'

image = plt.imread(image_name);
implot = plt.imshow(image);

for x in range(2,len(datalist)) :
#for x in range(2,10) :
	
	# left eye
	plt.scatter([datalist[x][1]], [datalist[x][2]])
	
	# right eye
	plt.scatter([datalist[x][6]], [datalist[x][7]], c='r')


plt.savefig('eyes-overlay.png')
#plt.show()






