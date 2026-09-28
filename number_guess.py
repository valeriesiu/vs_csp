#VS, number guessing game

import random

answer=random.randint(1,100)
attempt= 0

while attempt < 6:
    attempt = int(input("Pick a number between 1 and 100: "))
    attempt = attempt + 1

    if attempt == answer:
        print(f"You got it right! It took {attempt} tries!")
        break
    elif attempt < answer:
        print("Guess again higher.")
    else:
        print("Guess agan lower.")

if attempt != answer:
    print(f"You ran out of tries. The answer was {answer}")
