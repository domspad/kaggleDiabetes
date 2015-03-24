import csv
from collections import Counter, defaultdict
import random
from shutil import copyfile


# Open csv and store data in list
labels = []
with open('data/trainLabels.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		labels.append(row)

# Remove csv header
labels = labels[1:]

# Count the number of different labels in the training set
label_cnts = Counter()
for item in labels:
	label_cnts[item[1]] += 1

# Segment the list based on the different lablels
left_segments = defaultdict(list)
right_segments = defaultdict(list)

for item in labels:
	if 'left' in item[0]:
		left_segments[int(item[1])].append(item[0])
	else:
		right_segments[int(item[1])].append(item[0])

# Pull a random sample of 20 files from each left_segment
samples = defaultdict(list)
for key in left_segments:
	samples[key] = random.sample(left_segments[key], 20)

# copy the left and right images for the sample into a seperate directory

for key in samples:
	for file_name in samples[key]:
		#copy left image:
		srcl = 'data/train/' + file_name + '.jpeg'
		destl = 'data/test_sample/' + file_name + '.jpeg'
		copyfile(srcl, destl)
		# copy right image
		srcr = 'data/train/' + file_name.replace('left', 'right') + '.jpeg'
		destr = 'data/test_sample/' + file_name.replace('left', 'right') + '.jpeg'
		copyfile(srcr, destr)