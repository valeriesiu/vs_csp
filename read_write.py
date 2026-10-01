#VS, read and write into files


#hover over the file, right click and select "copy relative path"
  #file path (how you get to the file)
                    #the "r" determines what you do with the file. r= read while w= write
                        #as file means the name of the file in the code
with open("practice.txt", "r") as file:
    content = file.read()
    #doing the ".read()" is a method that gives user what is written on the file
    content=content + "\ncredits to my mind"
    #make sure its a variable so you can PRINT the message
    print(content)

#with open is the keyword to open th file.
with open("practice.txt","a") as file:     #when using "a" means append which adds content to the end. this is how you also add stuff to a list.
#"r" read the file
#"w" write over the file
#"a" append ; adds content to the end of the file
    file.write("woahhh the weather is so nice today the sky is crystalline")
    #!!!!WHEN YOU WRITE ONTO A FILE IT REPLACES THE CONTENT IN THAT FILE!!!!

with open("practice.txt", "r") as file:
    content = file.read()
    content="chapter1;\n" + content + "and i feel so refreshed this is so funnn"
    file.write("\n woahhie the weather is so nice today the sky is crystal clear")
    