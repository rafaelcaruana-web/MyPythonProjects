loop = 0
balance = 1000
cashinhand = 1000
while loop != 1:
    WAmount = 0
    DAmount = 0


   
    print("Bank Balance £",balance)


   
    print("You have £",cashinhand, "in cash.")


    print("Type 'W' to withdraw, 'D' to deposit, and 'Q' to quit.")


    Option = input()


    if Option == "W":
        print("How much would you like to Withdraw?")
        WAmount = int(input())
       
        if WAmount > balance and balance!= 0:
            print("Insufficient Funds!")
       
        else:
            print("You withdrew £",WAmount, "from your account.")
            balance = balance - WAmount
            cashinhand = cashinhand + WAmount
       
    elif Option == "D":
        print("How much do you want to deposit?")
        DAmount = int(input())
       
        if DAmount > balance and balance != 0:
            print("Insufficient Funds!")
       
        else:
            print("You deposited £",DAmount, "into your account.")
            balance = balance + DAmount
            cashinhand = cashinhand - DAmount
    elif Option == "Q":
        print("You quit the program.")
        break
    else:
       break
