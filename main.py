import tkinter as tk
from commands import check_balance

# create the main Window
root = tk.Tk()

# add a title to main window
root.title("ATM Simulator")
# specify main window size
root.geometry("500x400")

# Add account number entry
account_number_entry = tk.Entry(root, width=50)
account_number_entry.pack(side="top")

# Add check balance button
check_balance_btn =tk.Button(root, text="Chack Balance", command=lambda : check_balance(account_number=account_number_entry.get()))
check_balance_btn.pack(side="top")

# Add deposit button
deposit_btn =tk.Button(root, text="Deposit")
deposit_btn.pack(side="bottom")

# Open the main window
root.mainloop()