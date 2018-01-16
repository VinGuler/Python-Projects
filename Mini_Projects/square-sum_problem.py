import math

"""
This is a work in progress.

Trying to find a sequence up to some number n,
that has this rule:
an + an+1 = x**2
Meaning: the sum of every 2 neighbor numbers in the sequence
must be a power of 2. -> (i.e: 1, 3, 22 -> 1+3 = 2^2, 3+22 = 5^2)

Algorithm:

- Add int(n) to an Array
- Check all the numbers to find the next number with which:
--------------- n+m = x -> sqrt(x) = type(int) ----- 
- Add that number (m) to the Array
- Check next numbers to find a new number that does this thing with (m)
- If it does, add id to the empty side of m in the Array

"""

# Validating that 2 number n and m sum up to a power of 2
def check_valid_sum(n, m):
	sqroot = math.sqrt(n+m)  
	return (sqroot == math.floor(sqroot))

# The returned list does not include the limit
def create_num_list(limit):
	numbers = []
	for num in range(1, limit):
		numbers.append(num)
	return numbers

# Moving an element (e) from a recieved list(from_list)
# To a second recieved list(to_list) in index(index) 
def move_element(e, from_list, to_list, index):
	if e in from_list:
		to_list.insert(index, e)
		from_list.remove(e)

# Main function
def main():
	all_nums = create_num_list(16)
	no_match = []
	new_nums = []

	STARTING_NUMBER = 1
	MAX_ITERATIONS = 20
	# Counter to stop the loop just in case it goes bonanza
	count = 0;

	# This function modifies all_nums and new_nums !!!
	move_element(STARTING_NUMBER, all_nums, new_nums, 0)

	# There are still numbers in all_nums and we're not doing to many iterations
	while (len(all_nums) > 0) and (count < MAX_ITERATIONS):
		count += 1
		# Checking number at the end of the all_nums
		# With the number at the end of the new_nums
		n = all_nums[len(all_nums)-1]
		m = new_nums[len(new_nums)-1]
		# If n is a valid number add it to the end of new_nums
		if check_valid_sum(n, m):
			move_element(n, all_nums, new_nums, len(new_nums))
		# Else -> add it to the end of no_match list
		else:
			move_element(n, all_nums, no_match, len(no_match))
		# Printing the current iterations' UN_MATCHED numbers
		print(str(count) + ". Un matched : " + str(no_match))

	no_match.sort()
	# Showing info
	print("___ Summery ___")
	print("All numbers: " + str(all_nums))
	print("Un matched : " + str(no_match))
	print("New numbers: " + str(new_nums))
	print("Iterations : " + str(count))

main()




















