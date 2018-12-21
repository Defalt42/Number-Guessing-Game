import random

# Generate random number between 1 and 100
rand_num = random.randint(1, 100)

while True:
	guess = int(input("Guess a whole number between 1 and 100: "))

	if guess < 1 or guess > 100:
		print(guess + " is not between 1 and 100. Try again.")
		continue
	else:
		if guess > rand_num:
			print("{} is too high. Try again.".format(guess))
		elif guess < rand_num:
			print("{} is too low. Try again.".format(guess))
		else:
			print("{} is correct!".format(guess))
			break

	
