grid = [[20151125, 18749137, 17289845, 30943339, 10071777, 33511524],
[31916031, 21629792, 16929656,  7726640, 15514188,  4041754],
[16080970,  8057251,  1601130,  7981243, 11661866, 16474243],
[24592653, 32451966, 21345942,  9380097, 10600672, 31527494],
[   77061, 17552253, 28094349,  6899651,  9250759, 31663883],
[33071741,  6796745, 25397450, 24659492,  1534922, 27995004]]

# 1: 20151125
code_array = [0, 20151125] + [0] * 17850360

# (r, c): 1
location_dict = {}

def traverse_grid_and_populate_loc_dict():
	last_seen = 0
	diag_length = 1
	curr = 0

	while last_seen < 100000000:
		r = diag_length
		c = 1
		while curr < diag_length:
			last_seen += 1
			location_dict[(r, c)] = last_seen
			if r == 2947 and c == 3029:
				return
			curr += 1
			r -= 1
			c += 1
		diag_length += 1
		curr = 0


def calculate_code_dict():
	for i in range(2, len(code_array)-1):
		prev = code_array[i-1]
		temp = prev * 252533
		res = temp % 33554393
		code_array[i] = res 

def get_code_number_based_on_loc(r, c):
	return code_array[location_dict[(r,c)]-1]

calculate_code_dict()
print code_array[17850354]
