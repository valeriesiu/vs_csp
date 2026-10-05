#VS, hangman game

import random



with open ("words.txt", "r")as file:
    words = file.read().split(",")
answer=random.choice(words)

#save space for the win_lose.txt

wrong_guess=0
letters=""

print("""
_________
|     |
|     O
|    /|\\
|    /\\
|________
""")
for answer in range (1,answer+1):
    letter= input("welcome to hangman!! you have 6 attempts, what letter will you guess? -->")
if letter =! answer:
    print("""
_________
|     |
|     O
|    /|\\
|    /
|________

oh no he lost a leg, 
""")
    