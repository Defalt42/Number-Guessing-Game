import random

# Generate random number between 1 and 100
rand_num = random.randint(1, 100)
MAX_GUESSES = 10
num_guesses = 0

while num_guesses < MAX_GUESSES:
	print("Guesses left: {}".format(MAX_GUESSES - num_guesses))
	try:
		guess = int(input("Guess a whole number between 1 and 100: "))
	except ValueError:
		print("That is not a whole number. Try again.")
		continue

	if guess < 1 or guess > 100:
		print(str(guess) + " is not between 1 and 100. Try again.")
		continue
	else:
		num_guesses += 1
		if guess > rand_num:
			print("{} is too high. Try again.".format(guess))
		elif guess < rand_num:
			print("{} is too low. Try again.".format(guess))
		else:
			print("{} is correct!".format(guess))
			break
if num_guesses >= 10 and guess != rand_num:
	print("Out of guesses. Play again sometime.")
else:
	print("Congratulations, you win!")
