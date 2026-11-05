###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")


    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("Incorrect PIN.")
    elif choice == '6':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print('Would you like to change pin?')
            print('yes = 1 , go back = 0')
            num_temp = int(input('Enter number:'))
            if num_temp == 1:
                new_pin = input("Enter Your new PIN")
                new_pin = pin
                print(f'Your new pin is {pin}')
            else:
                continue 
        else:
            print("Invalid PIN")  
    else:
        print("Invalid option. Please try again.")
