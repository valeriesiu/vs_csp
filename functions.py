#VS, functions notes

#first thing you should do is write your variables
#second thing is that you should establish the functions your using
#third thing is any outputs for the user


#the variables

def stupid_proof(money):
    return True:
    try:
        amount=float(input(f"What is your monthly {money}?: "))
        return amount

income=float(input("What is your monthly income?"))
rent=float(input("What is your monthly rent?"))
utilities=float(input("What is your monthly utilties?"))
groceries=float(input("What is your monthly groceries?"))
transportation=float(input("What is your monthly transportation?"))
savings=income*.1

#establish the functioms
#def is short for define KEYWORD THAT DEFINES FUNCTIONS
#name your function, should be named the same way you name variable functions 
#variable holds pieces of information, while a function is an action
def calc_percent(income,bill):   #After the variable name make sure theres a parenthesis! inside put parameters. sometimes you have some sometimes there none.
    #parameters are pieces of information needed to for the variable to run
    #end with a : every piece of function will be indented
    #there can be alot of stuff happening in the function, in those code it is just multiplying
    return round(bill/income*100)  # the formula to solve a percentage
# the "reuturn" kind of works like an output to your CODE, not the user
#function wont do anything until you call its name. || right there the "calc_percent" is the function being called
# an arugment is the value for the parameters when you call the function.
 #outputs for the user
print(f"Your rent is {rent:.2f} that is {calc_percent}")
print(f"Your utilities is {utilities:.2f} that is {calc_percent}")
print(f"Your groceries is {groceries:.2f} that is {calc_percent}")
print(f"Your transportation is {transportation:.2f} that is {calc_percent}")
print(f"You could save {savings:.2f} that is {calc_percent(income,savings)}% of your income. ")
print(f"You have ${income-rent-utilities-groceries-transportation-savings:.2f} left to spend/")

