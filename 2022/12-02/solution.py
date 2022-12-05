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
# s.t. each round represents on element in the list
rounds_str = data.split("\n")

# delete the last item (and empty string)
del rounds_str[-1]

# split the element representing each round into a list
rounds_lst = [r.split() for r in rounds_str]

# construct a dict mapping opponent's selection to rock (r),
# paper (p), or scissors (s)
opp_selector = {
	"A": "r",  # rock
	"B": "p",  # paper
	"C": "s",  # scissors
}

# construct a dict mapping my selection to rock (r), paper (p),
# or scissors (s)
my_selector = {
	"X": "r",  # rock
	"Y": "p",  # paper
	"Z": "s",  # scissors
}

# construct dict mapping my selection to a score
selection_scores = {
	"r": 1,
	"p": 2,
	"s": 3,
}

# construct dict mapping round outcome to a score
outcome_scores = {
	"w": 6,
	"d": 3,
	"l": 0,
}

# initialize score as 0
score = 0

# iterate through each round, adjusting the score as necessary
for r in rounds_lst:
	# determine selections
	opp_selection = opp_selector[r[0]]
	my_selection = my_selector[r[1]]
	
	# add my selection's score
	score += selection_scores[my_selection]
	
	# set outcome based on selections
	if (my_selection == "r" and opp_selection == "s") or\
	   (my_selection == "p" and opp_selection == "r") or\
	   (my_selection == "s" and opp_selection == "p"):
		outcome = "w"
	
	elif (my_selection == "r" and opp_selection == "r") or\
	     (my_selection == "p" and opp_selection == "p") or\
	     (my_selection == "s" and opp_selection == "s"):
		outcome = "d"
	
	else:
		outcome= "l"
	
	# add outcome score
	score += outcome_scores[outcome]

# print the total score under scenario 1
print("Total score under scenario 1:", score)


###############################################################################
# Solution 2
###############################################################################

# construct a dict mapping intended outcome to loss (l), win (w), and draw (d)
outcome_selector = {
	"X": "l",
	"Y": 'd',
	"Z": 'w',
}

# reset score to 0
score = 0

# iterate through each round, adjusting the score as necessary
for r in rounds_lst:
	# determine opponent selection and target outcome
	opp_selection = opp_selector[r[0]]
	outcome = outcome_selector[r[1]]
	
	# add outcome score
	score += outcome_scores[outcome]
	
	# set selection based on intended outcome
	if (outcome == "w" and opp_selection == "r") or\
	   (outcome == "d" and opp_selection == "p") or\
	   (outcome == "l" and opp_selection == "s"):
		selection = "p"
	elif (outcome == "w" and opp_selection == "s") or\
	     (outcome == "d" and opp_selection == "r") or\
	     (outcome == "l" and opp_selection == "p"):
		selection = "r"
	else:
		selection = "s"
	
	# add my selection's score
	score += selection_scores[selection]

# print the total score under scenario 2
print("Total score under scenario 2:", score)

