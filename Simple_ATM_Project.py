username="Shiva"
password="Password"

UName=input("Enter UserName:")
UPassword=input("Enter User Password:")

if(username==UName and password==UPassword):
    print("""
             Welcome to The HYD Bank
             Options Include:   
    """)
    print("""
        [ 1 ].Balance Enquiry
        [ 2 ].Deposit
        [ 3 ].Withdraw
        [ 4 ].Mini Statement
        [ 5 ].Exit
    """)
    SelectedOption=int(input("Please Choose the Transactions: "))

    UserAmount=10000

    if SelectedOption==1:
        print("Your Total Account Balance: ",UserAmount)

    elif SelectedOption == 2:
        depAmount = int(input("Enter the amount That you are depositing: "))
        UserAmount += depAmount
        print("Total amount:", UserAmount)

    elif SelectedOption == 3:
        withdraw = int(input("Enter the withdrawn amount:"))
        UserAmount -= withdraw
        print("Total amount:", UserAmount)

    elif SelectedOption == 4:
        print("SBI Mini Transaction Receipt")
        print("username:", username)
        print("Total amount:", UserAmount)
        print("Thanks for visiting...Have a Nice Day...!!!")

    elif SelectedOption == 5:
        print("Visit Again...!!!")
        exit()

else:
    print("Enter the Valid Credintials")