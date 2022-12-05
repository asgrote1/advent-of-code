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
# s.t. each elf pair represents one element in the list
pairs = data.split("\n")

# split the elf pairs into lists s.t. each element
# represents one elf's cleaning assignment
assignments = [p.split(",") for p in pairs]

# confirm that each pair split into 2 assignments
n_violations = 0

for a in assignments:
    if len(a) != 2:
        raise Exception("At least one 'pair' is not a pair of 2!")

# split assignments into a min/max element
extremes = []

for a in assignments:
    _extremes = []
    for elf in a:
        _extremes.append([int(e) for e in elf.split("-")])

    extremes.append(_extremes)

# confirm the asserted min/max arrays are all length 2
for e in extremes:
    for elf in e:
        if len(elf) != 2:
            raise Exception("At least 1 min/max array has 3+ elements!")

# confirm asserted min/max are related as implied
for e in extremes:
    for elf in e:
        if elf[0] > elf[1]:
            raise Exception("At least one 'min' is actually a max!")


# determine the number of pairs for which one elf's assignments are entirely
# contained in the other's assignments...
#
# each element of extremes is a 2-element list, representing the 2 elves in a
# corresponding pair. The values stored represent the min/max sections to
# which each elf is assigned. With this convention, check if the first (second)
# elf's assignments are a subset of the second (first) elf's assignments. If
# yes, increment the counter.
def is_subset(a, b):
    """Determine if a is a subset of b.

    Args:
        a (int[]): An array of form [min, max].
        b (int[]): An array of form [min, max].

    Returns: Boolean
    """
    # a in b?
    if a[0] >= b[0] and a[1] <= b[1]:
        return True

    else:
        return False


n_subsets = 0

for e in extremes:
    e1 = [e[0][0], e[0][1]]
    e2 = [e[1][0], e[1][1]]

    if is_subset(e1, e2) or is_subset(e2, e1):
        n_subsets += 1

print("The number of pairs in which one assignment of a subset of the other: ",
      n_subsets)


###############################################################################
# Solution 2
###############################################################################

# determine the number of pairs for which one elf's assignments intersect
# other's assignments...
#
# each element of extremes is a 2-element list, representing the 2 elves in a
# corresponding pair. The values stored represent the min/max sections to
# which each elf is assigned. With this convention, check if the first (second)
# elf's assignments overlap with the second (first) elf's assignments. If
# yes, increment the counter.
def is_overlap(a, b):
    """Determine if a is a subset of b.

    Args:
        a (int[]): An array of form [min, max].
        b (int[]): An array of form [min, max].

    Returns: Boolean
    """
    # a.min in [b.min, b.max]?
    if b[0] <= a[0] and a[0] <= b[1]:
        return True

    # a.max in [b.min, b.max]?
    elif b[0] <= a[1] and a[0] <= b[1]:
        return True

    else:
        return False


n_overlap = 0

for e in extremes:
    e1 = [e[0][0], e[0][1]]
    e2 = [e[1][0], e[1][1]]

    if is_overlap(e1, e2) or is_overlap(e2, e1):
        n_overlap += 1

print("The number of pairs in which the assignments overlap: ", n_overlap)
