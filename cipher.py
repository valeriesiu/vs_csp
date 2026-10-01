#VS, caesar cipher

#ord stands for the ascii number

choice=input("enter whether you would like to either decrypt or encrypt your message.:  ").lower.strip()
message=input("type in the message ->")
shift=int(input("what amount would you like to shift by? ")

while True:
choice=input("type in whether you would like to encrypt or decrypt a message: ").lower()
    if choice != "encrypt" and choice != "decrypt":
        print("this is not what i asked, make sure youve typed it correctly.")
    
    elif choice == "encrypt" and choice != "decrypt":
        message=input("what is your message??: ")
    else:
        break
