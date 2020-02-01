import random
import math
def guess(x):
	rand_20 = math.floor(random.random() * 20)
	print rand_20
	if(x == rand_20):
		return "You guessed right"
	elif(x > rand_20):
		return "You guessed too high"
	else:
		return "You guessed too low"
value = input("Type in your guess here => ")
print(guess(value))