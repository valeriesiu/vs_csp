#VS password strength checker

password=input("What is your password?:")

length = len(password) >= 8
lower = False
upper = False
symbol= False
number = False
strength= 0


for letter in password:

    if letter .isupper():
        upper= True


    elif letter .islower():
        lower=True


    elif letter .isnumeric():
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
    strength="Strong password!"

print(f"Your password strength is a {strength}")

if strength != "strong":
    missing_items=[]

    if not length:
        missing_items.append("Make sure theres atleast 8 characters")
    if not upper:
        missing_items.append("Make sure theres an uppercase letter.")
    if not number:
        missing_items.append("Make sure that theres a number.")
    if not symbol:
        missing_items.append("Make sure youve added a symbol.")

    print(f"In order to strengthen your password, {','.join(missing_items)}")

    