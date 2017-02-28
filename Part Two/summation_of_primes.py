def is_prime(x):
	# Value of x must be at least greater than 1 to be prime
	if x > 1:
		# Iterate through a range of 2 to value of x + 1. This makes the range inclusive on both ends
		for i in range (2, x + 1):
			# Check whether x has remainder of 0 when divided by iteself (x) or 1
			if x % i == 0 and i != x and i != 1:
				return False
			# Return True if x is divisible only by itself and 1
			else:
				return True
	# Return False when x is 1, 0, or negative
	else:
		return False

def get_primes(x):
	list = []
	condition = True
	while condition:
		# Check if x is prime number
		if is_prime(x):
			# put into list and increment
			list.append(x)
			x = x + 1
		# else check if x greater than 2 mil, if so get out of while loop
		elif x > 2000000:
			condition = False
		# increment x if number isn't prime and isn't greater than 2 mil
		else:
			x = x + 1
	# Print out list
	print(list)
	return list
	
def sum_primes(list):
	sum = 0
	# Iterate through list and sum up each prime number
	for i in list:
		sum = sum + i
	return sum

def main():
	user_prime = input('Enter the starting number to generate primes: ')
	# Print out total sum
	print('Total sum of each prime number from ' + str(user_prime) + ' to 2 million is: ' + str(sum_primes(get_primes(int(user_prime)))))

if __name__ == "__main__":
	main()
