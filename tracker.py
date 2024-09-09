import tkinter as tk
from tkinter import messagebox

# Define a list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    amount = float(amount_entry.get())
    category = category_entry.get()
    date = date_entry.get()
    expense = {'amount': amount, 'category': category, 'date': date}
    expenses.append(expense)
    messagebox.showinfo("Info", "Expense added successfully!")
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Function to view all expenses
def view_expenses():
    expenses_text.delete(1.0, tk.END)
    for expense in expenses:
        expenses_text.insert(tk.END, f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}\n")

# Function to calculate total expenses
def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    total_label.config(text=f"Total Expenses: {total}")

# Set up the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Create input fields
tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Date:").grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

# Create buttons
tk.Button(root, text="Add Expense", command=add_expense).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="View Expenses", command=view_expenses).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Total Expenses", command=total_expenses).grid(row=5, column=0, columnspan=2)

# Create text area to display expenses
expenses_text = tk.Text(root, height=10, width=50)
expenses_text.grid(row=6, column=0, columnspan=2)

# Create label to display total expenses
total_label = tk.Label(root, text="Total Expenses: 0")
total_label.grid(row=7, column=0, columnspan=2)

# Run the application
root.mainloop()
