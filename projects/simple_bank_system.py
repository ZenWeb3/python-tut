# Algorithm
# Display options for user to choose 
# set current balance to 0
# Create a function for deposit 
# create a function for withdrawal
# create a function to check balance 

user_name = input("please enter your name ")
print("********************************")
print()
print("Hello", user_name,", Welcome to zen banking system.")
print("What do you want to do today?")
def user_pick() :
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")

user_pick()

print()
print("********************************")

user_option = int(input("Choose your option "))

balance = 0
# check balance 
if user_option == 1 :
    print ("Your current balance is",balance)

if user_option == 2 :
    user_deposit = int(input("Enter amount to deposit: "))
    if user_deposit >= 5 :
        balance += user_deposit
        print("Your current balance is ",balance)
        user_pick()
        print()
            
    else :
        print ("Your deposit amount is too small, deposit must be more than 5")
        user_pick()

if user_option == 3 :
    user_withdrawal = int(input("Enter the amount you want to withdraw "))
    if user_withdrawal >= balance :
        balance -= user_withdrawal
        print("Your current balance is ",balance)
    else :
        print("Insufficient funds ")
        user_pick()