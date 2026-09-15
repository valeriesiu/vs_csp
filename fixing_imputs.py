#VS, fixing inputs


while True:
    color = input("Tell me a color: ").strip().capitalize()
    if color.isnumeric():
        print("That number is not a color!")
    elif " " in color:
        print("I said ONE WORD.")
    else:
          break
print(f"We painted the walls {color}!")