playing = True

while playing == True: 
    number = int(input("Enter a number to convert to hexadecimal: "))
    hexadecimal = hex(number)[2:].upper()

    print("Your number in hexidecimal is", hexadecimal)

    restart = input("Would you like to continue or quit? ('C' to continue, 'Q' to quit): ")
    if restart == "C":
        playing = True
        number = 0
    elif restart == "Q":
        playing = False

        print("You quit the program.")
        number = 0
        break
# By rafaelcaruana
