#vs fixed ticket code
age = int(input("Enter your age: "))
matinee = input("Is this a matinee? (yes/no): ").lower()

if age < 5:
    price = 0.00
elif age < 12:
    price = 8.00
elif age < 65:
    price = 12.00
else:
    price = 9

if matinee == "yes":
    price = price - 3.00


print(f"Ticket price: ${price:.2f}")