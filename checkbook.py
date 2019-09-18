#!/usr/local/anaconda3/bin/python
import json

#there should be a json file in the same directory as this py file with the JSON representation
#of the dictionary loaded a few lines down.
json_file = 'customers.json'

with open(json_file, "r") as f: 
    customers = json.load(f)
# the bank of users for testing. 2 dicts in a list
# customers = [
# {'name':'aone', 'balance':1000},    
# {'name':'btwo', 'balance':500}
# ]

def check_user(user):
    user_names = [i['name'] for i in customers]
    return user in user_names

def create_user(user):
    balance = int(input("How much do you have to start your account? "))
    new_user = {
        'name': user,
        'balance' : balance
    }
    customers.append(new_user)

# scaffolding for using sqlite
# def insert_customer(emp):
#     with conn:
#         c.execute("INSERT INTO customers VALUES (:name, :balance)", {'name': emp.first, 'balance': emp.last})


def see_balance(user, user_list):
    user_balance = [i['balance'] for i in user_list if i['name'] == user]
    return user_balance

def add_to_balance(user, amount):
    for i in customers: 
        if i['name'] == user: 
            i['balance'] += amount 
#     I'm gonna have to make this persistent. Maybe add a transactions table structure.
#     transaction_list.append(amount)

#Will only let you go negative once. Make a big withdrawal and run for it.
def subtract_from_balance(user, amount):
    for i in customers: 
        if i['name'] == user:
            if i['balance'] < 1:
                print("Your balance is not large enough to support a withdrawal.") 
            else:
                i['balance'] -= amount

#SKUNKWORKS: lets make a transaction history
#def show_transactions():



def print_menu():
    print("\n")
    print( 30 * "-" , "MENU" , 30 * "-")
    print( "1. View Current Balance")
    print( "2. Make A Deposit")
    print( "3. Make A Withdrawal")
    print( "4. Exit")
    print( 67 * "-")


##############################
transaction_list = []


loop=True      

current_user = input("What is your user name? ")
if check_user(current_user):
    print(f"Welcome back {current_user}")
else:
    print(" A new user!")
    create_user(current_user)

# for i in customers:
#     if i['balance'] < 1 and i['name'] == current_user:
#         print ("Please deposit more money before using the withdrawal function. ")
        


while loop:          ## While loop which will keep going until loop = False
    #test to see if account is in arrears 
    for i in customers:
        if i['balance'] < 1 and i['name'] == current_user:
            print ("Please deposit more money before using the withdrawal function. ".upper())
            break
    
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-4]: "))
     
    if choice==1:     
        print("Menu 1 has been selected") 
        current_balance = see_balance(current_user, customers)
        print(f"Your current balance is ${str(current_balance)[1:-1]}")
    
    elif choice==2:
        print("Menu 2 has been selected")
        amount = int(input("How much are you depositing to your account? "))
        add_to_balance(current_user, amount)
        current_balance = see_balance(current_user, customers)
        print(f"Your current balance is ${str(current_balance)[1:-1]}")
    
    elif choice==3:
        print("Menu 3 has been selected")
        amount = int(input("How much are you withdrawing from your account? "))
        subtract_from_balance(current_user, amount)
        current_balance = see_balance(current_user, customers)
        print(f"Your current balance is ${str(current_balance)[1:-1]}")
    
    # elif choice==4:
    #     print("Menu 4 has been selected")
    #     print("More features to come!")
        ## The exit choice to break the while loop
    elif choice==4:
        print("Menu 4 has been selected")
        print("Good bye")
        break

        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")

#save the changes
with open('customers.json', 'w') as f:  
    json.dump(customers, f)