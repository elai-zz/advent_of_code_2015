import itertools
weights = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
# weights = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
candidate_sets = []

def find_equal_groups():
	for i in range(2, 7):
		permutations = list(itertools.combinations(weights, i))
		for permutation in permutations:
			if sum(permutation) == 512:
				candidate_sets.append(permutation)

def find_least_quantum():
	shortest_length_tuples = []
	shortest = 10
	for candidate_set in candidate_sets:
		if len(candidate_set) == shortest:
			shortest_length_tuples.append(candidate_set)
		elif len(candidate_set) < shortest:
			shortest = len(candidate_set)
			shortest_length_tuples = [candidate_set]

	quantum = 900000000000

	for shortest_group in shortest_length_tuples:
		local_quantum = get_prod(shortest_group)
		if local_quantum < quantum:
			quantum = local_quantum

	return quantum

def get_prod(input_t):
	acc = 1
	for i in range(len(input_t)):
		acc = acc * input_t[i]
	return acc


find_equal_groups()
print find_least_quantum()
