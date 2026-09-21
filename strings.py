#VS, strings notes

#string --> is any saved saved in quotation marks " " or ' '
name= input("What is your name: ").strip().capitalize()
age= input("How old are you?: ")
print(type(age))
print(name+ " "+ age)


sentence= "The quick brown fox jumped over the lazy dog."
print(sentence)
print(sentence.replace("dog", "monkey"))


print(len(name))
print(f"Your name is {name} that is {len (name)} letters long. Your first inital is {name[0]}")

#The "1" is an index number
#Slicing is when you take a big string and pull out a smaller piece. That smaller piece is called a substring
