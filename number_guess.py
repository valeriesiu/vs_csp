#VS, number guessing game

import random

min=1
max=100
attempts= 6

answer=random.randint(min,max)

print("Guess a number between 1 and 100. You have 6 tries")

for attempt in range(1, attempts + 1):
    guess=int(input(f"What number do you guess?: "))
    if guess == answer:
        print(f"You got it right! it took {attempt} tries!")
        break
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("Too low! try again.")
else:
    print(f"Youve ran out of attempts. The answer was {answer}.")
