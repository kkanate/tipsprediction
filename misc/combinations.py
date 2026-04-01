# Import packages ----

import itertools

# Create list of values ----

letters = ["a", "b", "c", "d", "e"]
col_names = []

for l in range(1, len(letters) + 1):
    for comb in itertools.combinations(letters, l):
        col_names.append(list(comb))

col_names
