###############################################################################
# Solution 1
###############################################################################

# open stream to the data file
f = open('data.txt', 'r')

# read the data as a string
data = f.read()

# close stream to the data file
f.close()

# split the data on line breaks, separating data
# s.t. each pack represents one element in the list
packs = data.split("\n")

# confirm all packs contain an even number of items
n_items_per_pack = [len(p) % 2 for p in packs]

if sum(n_items_per_pack) != 0:
	raise Exception("At least one pack has an odd number of items!")

# split items per compartment
compartments = []

for p in packs:
	n_items = len(p)
	idx = int(n_items / 2)
	compartments.append([p[:idx], p[idx:]])

# find unique item shared across compartments
intersections = [list(set(c1).intersection(c2)) for c1, c2 in compartments]

# confirm a single unique item is shared across compartments in each pack
for i in intersections:
	if len(i) != 1:
		raise Exception("At least 1 intersection includes 2+ unique items.")

# switch to 1-dimensional list given above confirmation
intersections = [i[0] for i in intersections]

# assign score offsets based on letter case
upper_offset = -ord("A") + 27
lower_offset = -ord("a") + 1

# initialize the sum of the shared components' priorities
priority_sum = 0

# calculated the sum of the shared components' priorities
for i in intersections:
	offset = upper_offset if i.isupper() else lower_offset
	priority_sum += ord(i) + offset

print("The sum of the shared components' priorities in scenario 1: ",
	  priority_sum)


###############################################################################
# Solution 2
###############################################################################

# open stream to the data file
f = open('data.txt', 'r')

# read the data as a string
data = f.read()

# close stream to the data file
f.close()

# split the data on line breaks, separating data
# s.t. each pack represents one element in the list
packs = data.split("\n")

# confirm there is a multiple of 3 elves
if len(packs) % 3 != 0:
	raise Exception("The number of elves is not a multiple of 3!")

# separate elves by group
i = 0
group, groups = [], []

for p in packs:
	group.append(p)
	i += 1

	if i % 3 == 0:
		groups.append(group)
		group = []

intersections = [list(set(c1).intersection(c2).intersection(c3)) for c1, c2, c3 in groups]

# confirm a single unique item is shared across compartments in each pack
for i in intersections:
	if len(i) != 1:
		raise Exception("At least 1 intersection includes 2+ unique items.")

# switch to 1-dimensional list given above confirmation
intersections = [i[0] for i in intersections]

# assign score offsets based on letter case
upper_offset = -ord("A") + 27
lower_offset = -ord("a") + 1

# initialize the sum of the shared components' priorities
priority_sum = 0

# calculated the sum of the shared components' priorities
for i in intersections:
	offset = upper_offset if i.isupper() else lower_offset
	priority_sum += ord(i) + offset

print("The sum of the shared components' priorities in scenario 2: ",
	  priority_sum)