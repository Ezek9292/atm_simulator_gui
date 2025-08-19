from tkinter import messagebox
import csv
def check_balance(account_number):
    # open csv file
    csv_file = open(file="accounts.csv", mode="r")
    # read csv file
    accounts = csv.DictReader(csv_file)
    # print(list(accounts))
    for account in accounts:
        if account_number == account["account_number"]:
            # show balance
            messagebox.showinfo(title="Check Balance", message=f"Your balance is {account["balance"]}")
            return
    # Show user an account not found
    messagebox.showerror(title="Check Balance", message=f"Account number {account_number} does not exist")