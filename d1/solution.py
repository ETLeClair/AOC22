#AOC22 Day 1

array = []
sum_array = []
max_val = 0
f = open("input", "r")
for x in f:
	array.append(x)
new_array = [y.strip() for y in array]
sumval = 0
for z in new_array:
	if z != '':
		sumval += int(z)
	else:
		max_val = sumval
		sum_array.append(max_val)
		sumval = 0
sum_array.sort()

print(sum(sum_array[-1:]))
print(sum(sum_array[-3:]))
