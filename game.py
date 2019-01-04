import random

# Generate random number between 1 and 100
rand_num = random.randint(1, 100)
MAX_GUESSES = 10
num_guesses = 0

while num_guesses < MAX_GUESSES:
	print("Guesses left: {}".format(MAX_GUESSES - num_guesses))
	# Set guess to user input if user inputs a whole number
	try:
		guess = int(input("Guess a whole number between 1 and 100: "))
	except ValueError:
		print("That is not a whole number. Try again.")
		continue
	# Verify that the user's guess is within the range 1 to 100 inclusive
	if guess < 1 or guess > 100:
		print(str(guess) + " is not between 1 and 100. Try again.")
		continue
	# User input is a whole number; provide feedback as to how close the user's guess is to the random number
	else:
		num_guesses += 1
		if guess > rand_num:
			print("{} is too high. Try again.".format(guess))
		elif guess < rand_num:
			print("{} is too low. Try again.".format(guess))
		else:
			print("{} is correct!".format(guess))
			break
# Checks if the user correctly guessed the number or if they ran out of guesses
if num_guesses >= 10 and guess != rand_num:
	print("Out of guesses. Play again sometime.")
else:
	print("Congratulations, you win!")
