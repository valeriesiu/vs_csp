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

    elif letter in "~#$%^&@!()*?":
        symbol= True

print(f"Have a minimum of 8 characters: {length}")
print(f"Your password should have an uppercase: {upper}")
print(f"Your password should include a lowercase {lower}")
print(f"Password should include a symbol: {symbol}")
print(f"Password should include a number: {number}")

score = sum ([length,lower,upper,symbol,number])

if score <=2:
    strength="Weak password"
elif score <=4:
    strength="Medium, your getting there."
else:
    strength="Strong password!"

print(f"Your password strength is a {strength}")

if strength != "Strong password!":
    missing_items=[]

    if not length:
        missing_items.append("Make sure theres atleast 8 characters")
    if not upper:
        missing_items.append("Make sure theres an uppercase letter.")
    if not number:
        missing_items.append("Make sure that theres a number.")
    if not symbol:
        missing_items.append("Make sure youve added a symbol.")
    if not lower:
        missing_items.append("Make sure theres a lowercase letter. ")

    print(f"In order to strengthen your password, {','.join(missing_items)}")

    
