#VS, number information 


for number in range (1,21):
    if number % 2 == 0:
        if number % 5 == 0:
            print(f"{number} is even and can be divided by 5.")
        else: 
            print (f"{number} is even but cannot be divided by 5.")
    else:
        if number % 5 == 0:
            print (f"{number} is odd and can be divided by 5")
        else:
            print (f"{number} is odd and cannot be divided by 5")