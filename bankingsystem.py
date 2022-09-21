def account_add():
    name = str(input("Enter the name of the user: "))
    account_no = int(input("Enter the account number: "))
    balance = int(input("Enter balance: "))
    account_info = {
        "name": name,
        "account_no": account_no,
        "balance": balance
    }
    return account_info

def add_money(account_info):
  amount = int(input("Enter amount"))
  account_info["balance"] = { account_info["balance"]+amount}
  return add_money

def Withdraw(account_info):
  withdraw_amount = int(input("Enter withdraw amount"))
  account_info["balance"] = { account_info["balance"]+withdraw_amount}
  return Withdraw

def display_balance(account_info):
  return display_balance(["balance"])

def main():

  account_info = account_add()

  while True:

    print("1, Add account")
    print("2, Add money to account")
    print("3, withdraw money from account")
    print("4, display balance")
    print("5, Exit")
    choice = int(input("Enter Choice"))
    if choice == 1:
      account_add(account_info)
    
    if choice == 2:
      add_money(account_info)
    elif choice == 3:
      Withdraw(account_info)
    elif choice == 4: 
      display_balance(account_info)
    elif choice == 5:
      breakpoint
    else:
      print("Invalid Choice")

    if __name__ == "__main__":
        main()


  