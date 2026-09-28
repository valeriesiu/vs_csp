# VS, nesting notes

for number in range(1,21):
    if number % 15==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        

siblings= ["Sebastian", "Matthew", "Valerie"]
count=1
while count <= len(siblings):
    print(f"{count}. {siblings[count]}")
    count +=1
else:
    print("There are no siblings")