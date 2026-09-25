#VS, loops notes
import random

count=1  # this is the starting point

while count <=10: #this is the stop point (boolean)
    print(count)
    count+=1 
# increase iterator (The numner of times youve done the thing)
#iteration is the thing your doing
#the last thing of your while loop should be increasing the iterator

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck. . .")
    ducks+=1
print('GOOSE!!!!!!!')

#continue sends you to the beginning of the loop

#complex data type= holds other data in it
siblings = ["Sebastian", "Matthew", "Valerie"] #When making a list is has to be STRAIGHT brackets. Everything must be seperated by commas and words in quotatrions
print(siblings[2])
#adding to a list
name=input("Enter your name:")

siblings.append(name)

siblings.insert(3, "vienna")

print(siblings)

for sibling in siblings:
    print(sibling)
#remove from list

siblings.pop(3) # make sure you add an index nunber or it will just remove the last number from the list
#for loops
for num in range(1,11,2):    #range will build a list for you, just tell it the start and stop point. you can even tell it what to count by
    print(num)

# the 1 is the start point. the 11 is the end point and lastly the 2 is what it is counting by



for num in range(1,25):
    if num% 15== 0:
        print("FizzBuzz")
    elif num % 3 ==0:
        print("Fuzz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(num)

        #one conditional that works for every possible instance in the loop
