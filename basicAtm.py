pin=1234
#=================================
def check_balance():
       global user_current_balance
       user_current_balance=4000
       print(f"your current balance is {user_current_balance}")
#=================================
def withdraw_cash():
       user_current_balance=4000
       balance=int( input("enter the balance that you want to withdraw : "))     
       if balance<user_current_balance:
           user_current_balance-=balance
           print(f"you have withdrawn {balance}")   
           print(f"your current balance is {user_current_balance}")
       else:
           print("you have entered a balance greater than you have !")
#==================================
def deposit_cash():
       user_current_balance=4000
       balance=int( input("enter the balance that you want to deposit : "))  
       user_current_balance+=balance
       print(f"you have deposit {balance}")  
       print(f"your current balance is {user_current_balance}")
#===================================
def  change_pin():
        new_pin=int(input("enter the new pin : "))
        pin=new_pin
        print(f"the new PIN is {new_pin}")
#=====================================
def end_app():
        print("you are finish the program !")
        exit()
#======================================        
def main():
    print("="*50)
    print("""
1- Check Balance
2- Withdraw Cash
3- Deposit Cash
4- Change PIN
5- Exit
""")
    choice=input("enter the choice that you want  : ")
    if choice == '1':
        check_balance()
    elif choice=='2':
       withdraw_cash()
    elif choice =='3':
       deposit_cash()
    elif choice =='4'   :
        change_pin()
    elif choice=='5':
        end_app()
    else:
         print("Invalid choice. Please try again.")
         main()    
#===============================================
#===============================================

def check_pass():
    attempts=0
    while attempts <4:
        user_pin=int(input("Enter your PIN , you have 4 attempts : "))
        if user_pin==pin:
            print("right PIN !")
            main()
            break
        else:
            print("wrong PIN !")
            attempts+=1
            
#===================================================
#===================================================

check_pass()

