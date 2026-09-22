#VS, Conditionals notes
#booleans are true or false
time = 1416
day="Tuesday" 

if time < 1200 and time >500:
    print("Good morning")
elif time < 1700:
    if day != "Saturday" and day != "Sunday":
        print("How has school been?")
   print("Good afternoon!")

elif time < 2000:
    print("Good evening")
else:
    print("Goodnight.")
#notice how the print underneath isnt indented? it means it isnt  in the conditional
print("Code is done")


#conditionals always begin with "if"
#then after you have the boolean statement. end the line with a : symbol remmeber that when that happens the next line should be indented
# the else always marks the end. But not all conditionals will have an else.
#and says that both conditions must be true
#nesting is when you put one thing insude of another thing . You can put a conditional inside another conditional