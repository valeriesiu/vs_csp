#VS, caesar cipher

#ord stands for the ascii number

choice=input("enter whether you would like to either decrypt or encrypt your message.:  ").lower().strip()
message=input("type in the message here -> ")
shift = int(input("What amount would you like to shift by? type it here -> "))

def scrambled(message, shift):
    shifted = ""
    for char in message:
        if char.isupper():                        
            shifted =+ (
        char((ord(char) - ord('A') + shift) % 26 + ord('A'))
        )  #remeber the percent sign sort of wraps the text by its ascii value
        elif char.islower():
            shifted += (chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            shifted += char

    return shifted

if choice =="decrypt":
    shifted = scrambled (message, -shift)
    print(f"your text is now --> {shifted}")
elif choice == "encrypt":
    shifted = scrambled( message,shift)
    print(f"your message is now --> {shifted}")
