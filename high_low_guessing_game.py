import random

number = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.")
guess = int(input("Enter a number: "))

while number != guess:
  if guess < number:
    print ("Your effort is a bit low, go higher")
    guess = int(input("Enter a number ! "))
  elif guess > number:
    print ("Your effort is a bit high, go lower")
    guess = int(input("Enter a number ! "))
  else:
    print ("You did well!")
    break
