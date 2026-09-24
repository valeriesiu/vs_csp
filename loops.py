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
