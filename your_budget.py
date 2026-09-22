#VS, your budget 

while True:
    try:
        income=float(input("What is your income?:" ))
        break
    except:
        print("That isnt what I asked.")

while True:
    try:
      rent=float(input("What is your monthly rent/mortage?: "))
      break
    except:
        print("This is not what I asked you.")

while True:
    try:
      utilities=float(input("How much do you spend per month on utilities?: "))
      break
    except:
        print("This is not what I asked you.")

while True:
    try:
      groceries=float(input("How much do you spend per month on groceries?: "))
      break
    except:
        print("This is not what I asked you.")

while True:
    try:
      transportation=float(input("How much do you spend per month on transportation?: "))
      break
    except:
        print("This is not what I asked you.")

print(f"Your rent is ${rent:.2f} and that would be {int(rent/income*100)} of your income.")
print(f"Your utilities is ${utilities:.2f} and that would be {int(utilities/income*100)} of your income.")
print(f"Your groceries is ${groceries:.2f} and that would be {int(groceries/income*100)} of your income.")
print(f"Your transporation is ${transportation:.2f} and that would be {int(transportation/income*100)} of your income.")

savings = income/10
leftover = income-(rent+utilities+groceries+transportation+savings)
print(f"You should have ${savings:.2f} a month. Which would be 10 percent of your income.")
print(f"You should have ${leftover:.2f} extra money for the month!")
