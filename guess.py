#!/usr/bin/python
from random import randint

min = 1
max = 100
r = randint(min, max)
counter = 0

print "Hello!"
print "Pick a random number between %d and %d" % (min, max)

done = False
while not done:
	guess = int(raw_input("Guess a number: "))
	counter += 1

	if (guess == r):
		done = True
		print "Correct!  You guessed it in %d tries!" % counter
	elif (guess > r):
		print "A little high"
	else:
		print "A little low"

