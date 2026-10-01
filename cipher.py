#VS, caesar cipher

#ord stands for the ascii number

choice=input("enter whether you would like to either decrypt or encrypt your message.:  ").lower().strip()
message=input("type in the message here ->")
shift=int(input("what amount would you like to shift by? "))

def scramble (message,shift):
    shifted=""
    for chr in message:
        if chr.isupper()
        if chr.islower()