#VS password strength checker

characters= False
uppercase= False
lowercase=False
number=False
symbol=False
count=0
strength="Weak"

password=input("What is your password?:")

for letter in password:
    if len(password):
        length=True

for letter in password:
    if letter .isupper():
        uppercase= True

for letter in password:
    if letter .islower():
        lowercase=True

for letter in password:
    if letter .isnumeric():
        number=True

for letter in "!@#$%^&*()~`":
    symbol=True

if length:
    count+=1

if uppercase:
    count+=1

if lowercase:
    count+=1

if number:
    count+=1

if symbol:
    count+=1

if count == 5:
    strength="strong"

elif count >= 3:
    strength= "getting there"

else:
    strength="weak"

print(f"Your password is" {strength})


    