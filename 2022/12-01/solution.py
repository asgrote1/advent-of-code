###############################################################################
# Solution 1
###############################################################################

# open stream to the data file
f = open('data.txt', 'r')

# read the data as a string
data = f.read()

# split the data on double line breaks, separating
# data s.t. each elf's food items are represented
# by a newline-separated string.
food_items = data.split("\n\n")

# split each elf's food items on line breaks s.t.
# each elf's food item is 1 element in its 
# corresponding list
food_items_per_elf = [f.split() for f in food_items]

# calculate the total calories carried by each elf.
calories_per_elf = [sum(list(map(int, f))) for f in food_items_per_elf]

# print the calories carried by the elf carrying the most.
print("Total calories of the elf carrying the most: ", max(calories_per_elf))

# close stream to the data file
f.close()


###############################################################################
# Solution 2
###############################################################################

# create list to store highest n calories totals
n = 3
max_n = []

# append the n highest calorie totals to max_n; could track the removed
# items and re-insert them at the appropriate index
for i in range(n):
	max_n.append(max(calories_per_elf))
	calories_per_elf.remove(max_n[i])

# print the total calories carried by the 3 elves that individually
# carry the most
print("Total calories across the 3 elves with most individually: ", sum(max_n))

