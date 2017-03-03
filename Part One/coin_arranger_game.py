# This could have easily been more modularized, but anyway...
def moveHandler(coin_string):
	condition = True
	# While loop to ensure valid pair
	while condition:
		# Get whitespace string for origin
		fcp = input('\nSpace to the left coins position of the two coins you want to move: \n' + coin_string + '\n')
		# Get whitespace length, store that into an int
		from_cursor_position = len(fcp)
		# If cursor position is out of bounds, or if cursor is placed on a gap -- the program will ask to try again
		if from_cursor_position + 1 >= len(coin_string) or coin_string[from_cursor_position] == '-' or coin_string[from_cursor_position + 1] == '-':
			print("Can't retrieve that pair. Try again.")
		else:
			condition = False

	# Slice selected part of string, store into string
	moved_pair = coin_string[from_cursor_position:from_cursor_position+2]
	print('This is the pair you selected: ' + moved_pair)

	

	condition2 = True
	# while loop to validate correct movement of coins
	while condition2:
		# Get whitespace string for destination
		tcp = input('Space to the left position of where you want to move: \n' + coin_string + '\n')
		# Get whitespace length, store that into an int
		to_cursor_position = len(tcp)


		gap = False
		# if there is a coin gap in the string
		if '--' in coin_string:
			gap = True
		else:
			# Check if user spaces all the way to the end of the list: this is a valid placement
			if to_cursor_position+1 >= len(coin_string):
				break
			else:
				print("You can't move there. Try again.")
			# Check if user spaces to the right of the list: this is a valid placement
			if to_cursor_position == 0:
				break
		# While there is a coin gap
		while gap:
			try:
				# Check if user spaces to the left of two - -, signaling a coin gap: this is a valid placement
				if coin_string[to_cursor_position + 1] == '-' and coin_string[to_cursor_position + 2] == '-':
					condition2 = False
					break
				else:
					print("You can't move there. Try again.")
					break
			#Handle when user spaces cursor to the end of the list (with gap)
			except IndexError:
				print("You can't move there. Try again.")
				pass
				break
		
	# Turn coin string into a list
	coin_list = list(coin_string)
	coin_list_length = len(coin_list)

	# Change origin positions to -
	coin_list[from_cursor_position] = '-'
	coin_list[from_cursor_position+1] = '-'

	# Insert moved_pair via .insert() into the list if user selects the end of the row
	if (to_cursor_position +1) >= coin_list_length:
		coin_list.insert(to_cursor_position+1, moved_pair)
	# Insert moved_pair in the beginning of the list
	elif (to_cursor_position == 0):
		coin_list = [moved_pair] + coin_list
	# If user did not selected at the end of the list, individually insert coins into list
	else:
		coin_list[to_cursor_position+1] = moved_pair[0:1]
		coin_list[to_cursor_position+2] = moved_pair[1:2]
	# Change list back to string to display to user
	coin_string = ''.join([str(i) for i in coin_list])
	print('Result: ' + coin_string)

	# Return coin_string to be modified in the loop
	return coin_string



	
def main():
	coins = 'HHHHHTTTTT'
	turn_count = 1
	condition = True
	while condition: 
		print('\n---Turn '+str(turn_count)+'---')
		coins = moveHandler(coins)

		# handles turns, after five turns it exits the while loop
		turn_count = turn_count + 1
		
		if turn_count is 6:
			# Check is user gets either of the two solutions
			if (coins == 'HTHTHTHTHT') or (coins == 'THTHTHTHTH'):
				# I've never actually beat it
				print("Congratulations! You win!")
			else:
				print("Game over. You have failed miserably.")
			condition = False


if __name__ == "__main__":
	main()